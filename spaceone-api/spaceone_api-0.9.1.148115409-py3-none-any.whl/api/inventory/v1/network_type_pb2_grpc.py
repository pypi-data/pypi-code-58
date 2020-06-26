# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.inventory.v1 import network_type_pb2 as spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2


class NetworkTypeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.inventory.v1.NetworkType/create',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.CreateNetworkTypeRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypeInfo.FromString,
                )
        self.update = channel.unary_unary(
                '/spaceone.api.inventory.v1.NetworkType/update',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.UpdateNetworkTypeRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypeInfo.FromString,
                )
        self.delete = channel.unary_unary(
                '/spaceone.api.inventory.v1.NetworkType/delete',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypeRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.get = channel.unary_unary(
                '/spaceone.api.inventory.v1.NetworkType/get',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.GetNetworkTypeRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypeInfo.FromString,
                )
        self.list = channel.unary_unary(
                '/spaceone.api.inventory.v1.NetworkType/list',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypeQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypesInfo.FromString,
                )
        self.stat = channel.unary_unary(
                '/spaceone.api.inventory.v1.NetworkType/stat',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypeStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                )


class NetworkTypeServicer(object):
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


def add_NetworkTypeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.CreateNetworkTypeRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypeInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.UpdateNetworkTypeRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypeInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypeRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.GetNetworkTypeRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypeInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypeQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypesInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypeStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.inventory.v1.NetworkType', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NetworkType(object):
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.NetworkType/create',
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.CreateNetworkTypeRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypeInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.NetworkType/update',
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.UpdateNetworkTypeRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypeInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.NetworkType/delete',
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypeRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.NetworkType/get',
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.GetNetworkTypeRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypeInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.NetworkType/list',
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypeQuery.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypesInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.NetworkType/stat',
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__type__pb2.NetworkTypeStatQuery.SerializeToString,
            google_dot_protobuf_dot_struct__pb2.Struct.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
