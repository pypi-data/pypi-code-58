__all__ = ["Client", "YaqDaemonException"]


import functools
import inspect
import io
import json
import socket
from threading import Lock
import types


from ._socket import Socket


class YaqDaemonException(Exception):
    pass


def reconnect(fun):
    """
    If the socket link is broken, try creating a new link and run the method again.
    """

    @functools.wraps(fun)
    def inner(self, *args, **kwargs):
        try:
            return fun(self, *args, **kwargs)
        except ConnectionError:
            self.connect_socket()
            return fun(self, *args, **kwargs)

    return inner


class Client:
    def __init__(self, port, host="127.0.0.1"):
        self._host = host
        self._port = port
        self._socket = Socket(self._host, self._port)
        self._id_counter = 0
        self._mutex = Lock()
        self.handshake()

    def handshake(self):
        def fun(comm, sig):
            def inner(self, *args, **kwargs):
                ba = sig.bind_partial(self, *args, **kwargs)
                ba.apply_defaults()
                return self.send(comm, *ba.args[1:], **ba.kwargs)

            inner.__signature__ = sig
            inner.__name__ = comm
            return inner

        with self._mutex:
            self._protocol = json.loads(self._socket.handshake())
            self.traits = self._protocol["traits"]
            self.version = self._protocol["version"]
            for name, props in self._protocol.get("messages", {}).items():
                if hasattr(self, name):
                    continue

                params = [inspect.Parameter("self", inspect.Parameter.POSITIONAL_ONLY)]
                for param in props.get("request", []):
                    params.append(
                        inspect.Parameter(
                            param["name"],
                            inspect.Parameter.POSITIONAL_OR_KEYWORD,
                            default=param.get("default", inspect.Parameter.empty),
                        )
                    )
                sig = inspect.Signature(params)
                method = fun(name, sig)
                method.__doc__ = props.get("doc")
                setattr(self, name, types.MethodType(method, self))

    def send(self, method, *args, **kwargs):
        with self._mutex:
            self._id_counter += 1
            return self._socket.message(
                method, self._protocol["messages"][method], *args, **kwargs
            )
