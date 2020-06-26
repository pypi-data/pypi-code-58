# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Provides an object to pass configuration to Glean.
"""


from typing import Optional


from . import net


# The default server pings are sent to
DEFAULT_TELEMETRY_ENDPOINT = "https://incoming.telemetry.mozilla.org"


# The default number of events to store before sending
DEFAULT_MAX_EVENTS = 500


class Configuration:
    """
    Configuration values for Glean.
    """

    def __init__(
        self,
        server_endpoint: str = DEFAULT_TELEMETRY_ENDPOINT,
        channel: Optional[str] = None,
        max_events: int = DEFAULT_MAX_EVENTS,
        log_pings: bool = False,
        ping_tag: Optional[str] = None,
        ping_uploader: Optional[net.BaseUploader] = None,
        allow_multiprocessing: bool = True,
    ):
        """
        Args:
            server_endpoint (str): Optional. The server pings are sent to.
                Defaults to `DEFAULT_TELEMETRY_ENDPOINT`.
            channel (str): Optional. The release channel the application is on,
                if known.
            max_events (int): Optional.The number of events to store before
                force-sending. Defaults to `DEFAULT_MAX_EVENTS`.
            log_pings (bool): Optional. Whether to log ping contents to the
                console. Defaults to `False`.
            ping_tag (str): Optional. String tag to be applied to headers when
                uploading pings for debug view.
            ping_uploader (glean.net.BaseUploader): Optional. The ping uploader
                implementation. Defaults to `glean.net.HttpClientUploader`.
            allow_multiprocessing (bool): When True (default), use a subprocess
                to offload some work (such as ping uploading).
        """
        self._server_endpoint = server_endpoint
        self._channel = channel
        self._max_events = max_events
        self._log_pings = log_pings
        self._ping_tag = ping_tag
        if ping_uploader is None:
            ping_uploader = net.HttpClientUploader()
        self._ping_uploader = ping_uploader
        self._allow_multiprocessing = allow_multiprocessing

    @property
    def server_endpoint(self) -> str:
        """The server pings are sent to."""
        return self._server_endpoint

    @server_endpoint.setter
    def server_endpoint(self, value: str):
        self._server_endpoint = value

    @property
    def channel(self) -> Optional[str]:
        """The release channel the application is on, if known."""
        return self._channel

    @channel.setter
    def channel(self, value: str):
        from ._builtins import metrics

        self._channel = value

        metrics.glean.internal.metrics.app_channel.set(value)

    @property
    def max_events(self) -> int:
        """The number of events to store before force-sending."""
        return self._max_events

    # max_events can't be changed after Glean is initialized

    @property
    def log_pings(self) -> bool:
        """Whether to log ping contents to the console."""
        return self._log_pings

    @log_pings.setter
    def log_pings(self, value: bool):
        self._log_pings = value

    @property
    def ping_tag(self) -> Optional[str]:
        """String tag to be applied to headers when uploading pings for debug view."""
        return self._ping_tag

    @ping_tag.setter
    def ping_tag(self, value: str):
        self._ping_tag = value

    @property
    def ping_uploader(self) -> net.BaseUploader:
        """The ping uploader implementation."""
        return self._ping_uploader

    @ping_uploader.setter
    def ping_uploader(self, value: net.BaseUploader):
        self._ping_uploader = value


__all__ = ["Configuration"]
