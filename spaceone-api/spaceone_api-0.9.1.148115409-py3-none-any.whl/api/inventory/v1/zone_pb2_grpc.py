# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.inventory.v1 import zone_pb2 as spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2


class ZoneStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.inventory.v1.Zone/create',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.CreateZoneRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneInfo.FromString,
                )
        self.update = channel.unary_unary(
                '/spaceone.api.inventory.v1.Zone/update',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.UpdateZoneRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneInfo.FromString,
                )
        self.delete = channel.unary_unary(
                '/spaceone.api.inventory.v1.Zone/delete',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.get = channel.unary_unary(
                '/spaceone.api.inventory.v1.Zone/get',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.GetZoneRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneInfo.FromString,
                )
        self.add_member = channel.unary_unary(
                '/spaceone.api.inventory.v1.Zone/add_member',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneMemberRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneMemberInfo.FromString,
                )
        self.modify_member = channel.unary_unary(
                '/spaceone.api.inventory.v1.Zone/modify_member',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneMemberRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneMemberInfo.FromString,
                )
        self.remove_member = channel.unary_unary(
                '/spaceone.api.inventory.v1.Zone/remove_member',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.RemoveZoneMemberRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.list_members = channel.unary_unary(
                '/spaceone.api.inventory.v1.Zone/list_members',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneMemberQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneMembersInfo.FromString,
                )
        self.list = channel.unary_unary(
                '/spaceone.api.inventory.v1.Zone/list',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZonesInfo.FromString,
                )
        self.stat = channel.unary_unary(
                '/spaceone.api.inventory.v1.Zone/stat',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                )


class ZoneServicer(object):
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

    def add_member(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def modify_member(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def remove_member(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list_members(self, request, context):
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


def add_ZoneServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.CreateZoneRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.UpdateZoneRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.GetZoneRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneInfo.SerializeToString,
            ),
            'add_member': grpc.unary_unary_rpc_method_handler(
                    servicer.add_member,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneMemberRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneMemberInfo.SerializeToString,
            ),
            'modify_member': grpc.unary_unary_rpc_method_handler(
                    servicer.modify_member,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneMemberRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneMemberInfo.SerializeToString,
            ),
            'remove_member': grpc.unary_unary_rpc_method_handler(
                    servicer.remove_member,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.RemoveZoneMemberRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'list_members': grpc.unary_unary_rpc_method_handler(
                    servicer.list_members,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneMemberQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneMembersInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZonesInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.inventory.v1.Zone', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Zone(object):
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.Zone/create',
            spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.CreateZoneRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.Zone/update',
            spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.UpdateZoneRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.Zone/delete',
            spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.Zone/get',
            spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.GetZoneRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def add_member(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.Zone/add_member',
            spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneMemberRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneMemberInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def modify_member(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.Zone/modify_member',
            spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneMemberRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneMemberInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def remove_member(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.Zone/remove_member',
            spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.RemoveZoneMemberRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def list_members(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.Zone/list_members',
            spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneMemberQuery.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneMembersInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.Zone/list',
            spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneQuery.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZonesInfo.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.Zone/stat',
            spaceone_dot_api_dot_inventory_dot_v1_dot_zone__pb2.ZoneStatQuery.SerializeToString,
            google_dot_protobuf_dot_struct__pb2.Struct.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
