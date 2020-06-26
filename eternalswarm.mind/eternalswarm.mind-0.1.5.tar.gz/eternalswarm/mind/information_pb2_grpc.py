# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import information_pb2 as information__pb2
from . import models_pb2 as models__pb2


class InformationStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
                '/Information/Ping',
                request_serializer=information__pb2.PingMessage.SerializeToString,
                response_deserializer=information__pb2.PongMessage.FromString,
                )
        self.GetInfo = channel.unary_unary(
                '/Information/GetInfo',
                request_serializer=information__pb2.InfoRequest.SerializeToString,
                response_deserializer=information__pb2.Info.FromString,
                )
        self.GetSettings = channel.unary_unary(
                '/Information/GetSettings',
                request_serializer=information__pb2.SettingsRequest.SerializeToString,
                response_deserializer=information__pb2.SettingsList.FromString,
                )
        self.SetSetting = channel.unary_unary(
                '/Information/SetSetting',
                request_serializer=information__pb2.Section.SerializeToString,
                response_deserializer=information__pb2.Setting.FromString,
                )
        self.GetLog = channel.unary_unary(
                '/Information/GetLog',
                request_serializer=information__pb2.LogRequest.SerializeToString,
                response_deserializer=information__pb2.Log.FromString,
                )
        self.EnableGRPCSSL = channel.unary_unary(
                '/Information/EnableGRPCSSL',
                request_serializer=information__pb2.Certificates.SerializeToString,
                response_deserializer=information__pb2.StatusMsg.FromString,
                )
        self.SetCallbackCerts = channel.unary_unary(
                '/Information/SetCallbackCerts',
                request_serializer=information__pb2.Certificates.SerializeToString,
                response_deserializer=information__pb2.StatusMsg.FromString,
                )
        self.RestartServices = channel.unary_unary(
                '/Information/RestartServices',
                request_serializer=information__pb2.RestartMessage.SerializeToString,
                response_deserializer=information__pb2.StatusMsg.FromString,
                )
        self.GetDroneCapabilities = channel.unary_unary(
                '/Information/GetDroneCapabilities',
                request_serializer=models__pb2.EmptyMessage.SerializeToString,
                response_deserializer=information__pb2.DroneCapabilities.FromString,
                )


class InformationServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInfo(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSettings(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSetting(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLog(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableGRPCSSL(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetCallbackCerts(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RestartServices(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDroneCapabilities(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InformationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=information__pb2.PingMessage.FromString,
                    response_serializer=information__pb2.PongMessage.SerializeToString,
            ),
            'GetInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInfo,
                    request_deserializer=information__pb2.InfoRequest.FromString,
                    response_serializer=information__pb2.Info.SerializeToString,
            ),
            'GetSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSettings,
                    request_deserializer=information__pb2.SettingsRequest.FromString,
                    response_serializer=information__pb2.SettingsList.SerializeToString,
            ),
            'SetSetting': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSetting,
                    request_deserializer=information__pb2.Section.FromString,
                    response_serializer=information__pb2.Setting.SerializeToString,
            ),
            'GetLog': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLog,
                    request_deserializer=information__pb2.LogRequest.FromString,
                    response_serializer=information__pb2.Log.SerializeToString,
            ),
            'EnableGRPCSSL': grpc.unary_unary_rpc_method_handler(
                    servicer.EnableGRPCSSL,
                    request_deserializer=information__pb2.Certificates.FromString,
                    response_serializer=information__pb2.StatusMsg.SerializeToString,
            ),
            'SetCallbackCerts': grpc.unary_unary_rpc_method_handler(
                    servicer.SetCallbackCerts,
                    request_deserializer=information__pb2.Certificates.FromString,
                    response_serializer=information__pb2.StatusMsg.SerializeToString,
            ),
            'RestartServices': grpc.unary_unary_rpc_method_handler(
                    servicer.RestartServices,
                    request_deserializer=information__pb2.RestartMessage.FromString,
                    response_serializer=information__pb2.StatusMsg.SerializeToString,
            ),
            'GetDroneCapabilities': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDroneCapabilities,
                    request_deserializer=models__pb2.EmptyMessage.FromString,
                    response_serializer=information__pb2.DroneCapabilities.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Information', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Information(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Information/Ping',
            information__pb2.PingMessage.SerializeToString,
            information__pb2.PongMessage.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Information/GetInfo',
            information__pb2.InfoRequest.SerializeToString,
            information__pb2.Info.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Information/GetSettings',
            information__pb2.SettingsRequest.SerializeToString,
            information__pb2.SettingsList.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetSetting(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Information/SetSetting',
            information__pb2.Section.SerializeToString,
            information__pb2.Setting.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLog(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Information/GetLog',
            information__pb2.LogRequest.SerializeToString,
            information__pb2.Log.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnableGRPCSSL(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Information/EnableGRPCSSL',
            information__pb2.Certificates.SerializeToString,
            information__pb2.StatusMsg.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetCallbackCerts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Information/SetCallbackCerts',
            information__pb2.Certificates.SerializeToString,
            information__pb2.StatusMsg.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RestartServices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Information/RestartServices',
            information__pb2.RestartMessage.SerializeToString,
            information__pb2.StatusMsg.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDroneCapabilities(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Information/GetDroneCapabilities',
            models__pb2.EmptyMessage.SerializeToString,
            information__pb2.DroneCapabilities.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
