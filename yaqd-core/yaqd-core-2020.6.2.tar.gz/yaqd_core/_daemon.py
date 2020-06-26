#! /usr/bin/env python3

__all__ = ["Base"]

import argparse
import asyncio
import functools
import inspect
import json
import logging as logging_
import pathlib
import signal
import sys
import time
from typing import Dict, List, Optional, Any, Union, Sequence, Set

import appdirs  # type: ignore
import pkg_resources
import toml

from .__version__ import __version__, __avro_version__
from ._protocol import Protocol
from . import logging
from .exceptions import InvalidRequest, MethodNotFound

logger = logging.getLogger("yaqd_core")


class classproperty(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, owner):
        return self.f(owner)


class Base:
    _daemons: List["Base"] = []
    _kind: str = "base"
    _branch: Optional[str] = None

    def __init__(
        self, name: str, config: Dict[str, Any], config_filepath: pathlib.Path
    ):
        """Create a yaq daemon.

        Parameters
        ----------
        name: str
            A name for this daemon
        config: dict
            Configuration parameters
        config_filepath: str
            The path for the configuration (not used internally, availble to clients)
        """
        self.name = name
        self._config = config
        self._config_filepath = config_filepath
        self._state_filepath = (
            pathlib.Path(appdirs.user_data_dir("yaqd-state", "yaq"))
            / self._kind
            / f"{self.name}-state.toml"
        )
        self.logger = logging.getLogger(self.name)
        if "log_level" in self._config:
            self.logger.setLevel(logging.name_to_level[self._config["log_level"]])
        if self._config.get("log_to_file"):
            fh = logging_.FileHandler(
                self._state_filepath.with_name(
                    f"{self.name}-{time.strftime('%Y-%m-%dT%H:%M:%S%z')}.log"
                )
            )
            fh.setFormatter(logging.formatter)
            self.logger.addHandler(fh)
        self.logger.info(f"Config File Path = {self._config_filepath}")
        self.logger.info(f"State File Path = {self._state_filepath}")
        self.logger.info(f"TCP Port = {config['port']}")
        self._clients: List[str] = []

        self.serial = config.get("serial", None)
        self.make = config.get("make", None)
        self.model = config.get("model", None)

        self._busy_sig = asyncio.Event()
        self._not_busy_sig = asyncio.Event()

        self._loop = asyncio.get_event_loop()

        try:
            self._state_filepath.parent.mkdir(parents=True, exist_ok=True)
            with self._state_filepath.open("rt") as f:
                state = toml.load(f)
        except (toml.TomlDecodeError, FileNotFoundError):
            state = {}

        self._load_state(state)
        self._tasks = [
            self._loop.create_task(self.save_state()),
            self._loop.create_task(self.update_state()),
        ]

    @classproperty
    def _avro_protocol(cls):
        return json.loads(
            pkg_resources.resource_string(cls.__module__, f"{cls._kind}.avpr")
        )

    @classproperty
    def _version(cls) -> str:
        return (
            f"{cls._avro_protocol.get('version')}" + f"+{cls._branch}"
            if cls._branch
            else ""
        )

    @classmethod
    def main(cls):
        """Run the event loop."""
        loop = asyncio.get_event_loop()
        if sys.platform.startswith("win"):
            signals = ()
        else:
            signals = (signal.SIGHUP, signal.SIGTERM, signal.SIGINT)
        for s in signals:
            loop.add_signal_handler(
                s, lambda s=s: asyncio.create_task(cls.shutdown_all(s, loop))
            )

        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--config",
            "-c",
            default=(
                pathlib.Path(appdirs.user_config_dir("yaqd", "yaq"))
                / cls._kind
                / "config.toml"
            ),
            action="store",
            help="Path to the configuration toml file.",
        )
        parser.add_argument(
            "--verbose",
            "-v",
            action="store_const",
            dest="log_level",
            const="debug",
            help="Alias for --log-level=debug",
        )
        parser.add_argument(
            "--log-level",
            "-l",
            action="store",
            dest="log_level",
            choices=[
                "debug",
                "info",
                "notice",
                "warning",
                "error",
                "critical",
                "alert",
                "emergency",
            ],
            help="Set the log level explicitly",
        )

        parser.add_argument("--version", action="store_true")

        args = parser.parse_args()

        if args.log_level:
            logging.setLevel(logging.name_to_level[args.log_level])

        if args.version:
            print(f"'{cls._kind}' version {cls._version}")
            print(f"avro version {__avro_version__}")
            print(f"yaqd_core version {__version__}")
            print(f"Python {sys.version}")
            sys.exit(0)

        config_filepath = pathlib.Path(args.config)
        config_file = toml.load(config_filepath)

        main_task = loop.create_task(cls._main(config_filepath, config_file, args))
        try:
            loop.run_forever()
        except asyncio.exceptions.CancelledError:
            pass
        finally:
            loop.close()

    @classmethod
    async def _main(cls, config_filepath, config_file, args=None):
        """Parse command line arguments, start event loop tasks."""
        loop = asyncio.get_running_loop()
        cls.__servers = []
        for section in config_file:
            try:
                config = cls._parse_config(config_file, section, args)
            except ValueError:
                continue
            logger.debug(f"Starting {section} with {config}")
            await cls._start_daemon(section, config, config_filepath)

        while cls.__servers:
            awaiting = cls.__servers
            cls.__servers = []
            await asyncio.wait(awaiting)
            await asyncio.sleep(1)
        loop.stop()

    @classmethod
    async def _start_daemon(cls, name, config, config_filepath):
        loop = asyncio.get_running_loop()
        daemon = cls(name, config, config_filepath)
        cls._daemons.append(daemon)

        # This function is here to namespace `daemon` so it doesn't
        # get overridden for the lambda
        def server(daemon):
            return lambda: Protocol(daemon)

        ser = await loop.create_server(
            server(daemon), config.get("host", ""), config.get("port", None)
        )
        daemon._server = ser
        cls.__servers.append(ser.serve_forever())

    @classmethod
    def _parse_config(cls, config_file, section, args=None):
        if section == "shared-settings":
            raise ValueError(f"Section name '{section}' reserved")
        config = {}
        for name, type_ in cls._avro_protocol.get("config", {}).items():
            if "default" in type_:
                config[name] = type_["default"]
        config.update(config_file.get("shared-settings", {}).copy())
        config.update(config_file[section])
        if args:
            try:
                if args.log_level:
                    config.update(log_level=args.log_level)
            except AttributeError:
                pass

        if not config.get("enable", True):
            logger.info(f"Section '{section}' is disabled")
            raise ValueError(f"Section '{section}' is disabled")
        return config

    @classmethod
    async def shutdown_all(cls, sig, loop):
        """Gracefully shutdown the asyncio loop.

        Gathers all current tasks, and allows daemons to perform cleanup tasks.

        Adapted from https://www.roguelynn.com/words/asyncio-graceful-shutdowns/
        Original code is licensed under the MIT license, and sublicensed here.
        """
        logger.info(f"Received signal {sig.name}...")
        tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
        logger.info(f"Cancelling {len(tasks)} outstanding tasks")
        [task.cancel() for task in tasks]
        # This is done after cancelling so that shutdown tasks which require the loop
        # are not themselves cancelled.
        [d.close() for d in cls._daemons]
        tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
        await asyncio.gather(*tasks, return_exceptions=True)
        [d._save_state() for d in cls._daemons]
        if hasattr(signal, "SIGHUP") and sig == signal.SIGHUP:
            config_filepath = [d._config_filepath for d in cls._daemons][0]
            config_file = toml.load(config_filepath)
            await cls._main(config_filepath, config_file)
        loop.stop()

    def shutdown(self, restart=False):
        self.logger.info(f"Shutting Down {self.name}")
        self.logger.info(f"Cancelling {len(self._tasks)} outstanding tasks")
        [task.cancel() for task in self._tasks]
        self.close()
        self._server.close()
        if restart:
            config_filepath = self._config_filepath
            config_file = toml.load(config_filepath)
            try:
                config = type(self)._parse_config(config_file, self.name)
                self._loop.create_task(
                    type(self)._start_daemon(self.name, config, config_filepath)
                )
            except ValueError as e:
                self.logger.error(e.message)

    def _connection_made(self, peername: str) -> None:
        self._clients.append(peername)
        self.logger.debug(f"_connection_made {self._clients}")

    def _connection_lost(self, peername: str) -> None:
        self._clients.remove(peername)
        self.logger.debug(f"_connection_lost {self._clients}")

    def _save_state(self) -> None:
        """Write the current state to disk."""
        with open(self._state_filepath, "wt") as f:
            f.write(self.get_state())

    async def save_state(self):
        """Schedule writing the current state to disk.

        Note: Current implementation only writes while busy (and once after busy)
        """
        while True:
            while self._busy:
                self._save_state()
                await asyncio.sleep(0.1)
            self._save_state()
            await self._busy_sig.wait()

    def get_config_filepath(self) -> str:
        """Retrieve the current filepath of the configuration."""
        return str(self._config_filepath.absolute())

    def get_config(self) -> str:
        """Retrieve the current configuration, including any defaults."""
        return toml.dumps(self._config)

    def id(self) -> Dict[str, Optional[str]]:
        """Dictionary of identifying information for the daemon."""
        return {
            "name": self.name,
            "kind": self._kind,
            "make": self.make,
            "model": self.model,
            "serial": self.serial,
        }

    @property
    def _busy(self) -> bool:
        """Indicates the current 'busy' state for use in internal functions.

        Setting busy can be done with `self._busy = <True|False>`.
        Async tasks can wait for either sense using `await self._[not_]busy_sig.wait()`.
        """
        return self._busy_sig.is_set()

    @_busy.setter
    def _busy(self, value):
        if value:
            self._busy_sig.set()
            self._not_busy_sig.clear()
        else:
            self._not_busy_sig.set()
            self._busy_sig.clear()

    def busy(self) -> bool:
        """Boolean representing if the daemon is busy (state updated) or not."""
        return self._busy

    # The following functions (plus __init__) are what most daemon need to implement

    async def update_state(self):
        """Continually monitor and update the current daemon state."""
        pass

    def get_state(self) -> str:
        """Return the current daemon state."""
        return toml.dumps(self._state)

    def _load_state(self, state):
        """Load an initial state from a dictionary (typically read from the state.toml file).

        Must be tolerant of missing fields, including entirely empty initial states.
        Raise an exception if state is invalid.

        Parameters
        ----------
        state: dict
            The saved state to load.
        """
        self._state = state
        for name, type_ in self._avro_protocol.get("state", {}).items():
            self._state.setdefault(name, type_.get("default", None))

    def close(self):
        pass
