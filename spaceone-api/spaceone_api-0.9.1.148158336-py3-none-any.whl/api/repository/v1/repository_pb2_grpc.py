# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.repository.v1 import repository_pb2 as spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2


class RepositoryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.register = channel.unary_unary(
                '/spaceone.api.repository.v1.Repository/register',
                request_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.CreateRepositoryRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoryInfo.FromString,
                )
        self.update = channel.unary_unary(
                '/spaceone.api.repository.v1.Repository/update',
                request_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.UpdateRepositoryRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoryInfo.FromString,
                )
        self.deregister = channel.unary_unary(
                '/spaceone.api.repository.v1.Repository/deregister',
                request_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoryRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.get = channel.unary_unary(
                '/spaceone.api.repository.v1.Repository/get',
                request_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.GetRepositoryRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoryInfo.FromString,
                )
        self.list = channel.unary_unary(
                '/spaceone.api.repository.v1.Repository/list',
                request_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoryQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoriesInfo.FromString,
                )
        self.stat = channel.unary_unary(
                '/spaceone.api.repository.v1.Repository/stat',
                request_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoryStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                )


class RepositoryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deregister(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RepositoryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'register': grpc.unary_unary_rpc_method_handler(
                    servicer.register,
                    request_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.CreateRepositoryRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoryInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.UpdateRepositoryRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoryInfo.SerializeToString,
            ),
            'deregister': grpc.unary_unary_rpc_method_handler(
                    servicer.deregister,
                    request_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoryRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.GetRepositoryRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoryInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoryQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoriesInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoryStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.repository.v1.Repository', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Repository(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.repository.v1.Repository/register',
            spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.CreateRepositoryRequest.SerializeToString,
            spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoryInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.repository.v1.Repository/update',
            spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.UpdateRepositoryRequest.SerializeToString,
            spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoryInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deregister(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.repository.v1.Repository/deregister',
            spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoryRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.repository.v1.Repository/get',
            spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.GetRepositoryRequest.SerializeToString,
            spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoryInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.repository.v1.Repository/list',
            spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoryQuery.SerializeToString,
            spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoriesInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def stat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.repository.v1.Repository/stat',
            spaceone_dot_api_dot_repository_dot_v1_dot_repository__pb2.RepositoryStatQuery.SerializeToString,
            google_dot_protobuf_dot_struct__pb2.Struct.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
