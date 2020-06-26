# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.inventory.v1 import network_policy_pb2 as spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2


class NetworkPolicyStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.inventory.v1.NetworkPolicy/create',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.CreateNetworkPolicyRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyInfo.FromString,
                )
        self.update = channel.unary_unary(
                '/spaceone.api.inventory.v1.NetworkPolicy/update',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.UpdateNetworkPolicyRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyInfo.FromString,
                )
        self.pin_data = channel.unary_unary(
                '/spaceone.api.inventory.v1.NetworkPolicy/pin_data',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.PinNetworkPolicyDataRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyInfo.FromString,
                )
        self.delete = channel.unary_unary(
                '/spaceone.api.inventory.v1.NetworkPolicy/delete',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.get = channel.unary_unary(
                '/spaceone.api.inventory.v1.NetworkPolicy/get',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.GetNetworkPolicyRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyInfo.FromString,
                )
        self.list = channel.unary_unary(
                '/spaceone.api.inventory.v1.NetworkPolicy/list',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPoliciesInfo.FromString,
                )
        self.stat = channel.unary_unary(
                '/spaceone.api.inventory.v1.NetworkPolicy/stat',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                )


class NetworkPolicyServicer(object):
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

    def pin_data(self, request, context):
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


def add_NetworkPolicyServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.CreateNetworkPolicyRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.UpdateNetworkPolicyRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyInfo.SerializeToString,
            ),
            'pin_data': grpc.unary_unary_rpc_method_handler(
                    servicer.pin_data,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.PinNetworkPolicyDataRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.GetNetworkPolicyRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPoliciesInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.inventory.v1.NetworkPolicy', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NetworkPolicy(object):
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.NetworkPolicy/create',
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.CreateNetworkPolicyRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.NetworkPolicy/update',
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.UpdateNetworkPolicyRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def pin_data(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.NetworkPolicy/pin_data',
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.PinNetworkPolicyDataRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.NetworkPolicy/delete',
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.NetworkPolicy/get',
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.GetNetworkPolicyRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.NetworkPolicy/list',
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyQuery.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPoliciesInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.NetworkPolicy/stat',
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__policy__pb2.NetworkPolicyStatQuery.SerializeToString,
            google_dot_protobuf_dot_struct__pb2.Struct.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
