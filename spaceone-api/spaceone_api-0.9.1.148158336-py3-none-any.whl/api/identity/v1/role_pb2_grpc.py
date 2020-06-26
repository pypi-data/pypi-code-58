# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.identity.v1 import role_pb2 as spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2


class RoleStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.identity.v1.Role/create',
                request_serializer=spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.CreateRoleRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RoleInfo.FromString,
                )
        self.update = channel.unary_unary(
                '/spaceone.api.identity.v1.Role/update',
                request_serializer=spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.UpdateRoleRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RoleInfo.FromString,
                )
        self.delete = channel.unary_unary(
                '/spaceone.api.identity.v1.Role/delete',
                request_serializer=spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RoleRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.get = channel.unary_unary(
                '/spaceone.api.identity.v1.Role/get',
                request_serializer=spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.GetRoleRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RoleInfo.FromString,
                )
        self.list = channel.unary_unary(
                '/spaceone.api.identity.v1.Role/list',
                request_serializer=spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RoleQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RolesInfo.FromString,
                )
        self.stat = channel.unary_unary(
                '/spaceone.api.identity.v1.Role/stat',
                request_serializer=spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RoleStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                )


class RoleServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
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


def add_RoleServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.CreateRoleRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RoleInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.UpdateRoleRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RoleInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RoleRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.GetRoleRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RoleInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RoleQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RolesInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RoleStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.identity.v1.Role', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Role(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.identity.v1.Role/create',
            spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.CreateRoleRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RoleInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.identity.v1.Role/update',
            spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.UpdateRoleRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RoleInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.identity.v1.Role/delete',
            spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RoleRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.identity.v1.Role/get',
            spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.GetRoleRequest.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RoleInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.identity.v1.Role/list',
            spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RoleQuery.SerializeToString,
            spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RolesInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.identity.v1.Role/stat',
            spaceone_dot_api_dot_identity_dot_v1_dot_role__pb2.RoleStatQuery.SerializeToString,
            google_dot_protobuf_dot_struct__pb2.Struct.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
