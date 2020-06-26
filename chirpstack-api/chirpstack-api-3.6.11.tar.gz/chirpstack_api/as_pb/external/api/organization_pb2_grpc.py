# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from chirpstack_api.as_pb.external.api import organization_pb2 as chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class OrganizationServiceStub(object):
    """OrganizationService is the service managing the organization access.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/api.OrganizationService/List',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.ListOrganizationRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.ListOrganizationResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/api.OrganizationService/Get',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.GetOrganizationRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.GetOrganizationResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/api.OrganizationService/Create',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.CreateOrganizationRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.CreateOrganizationResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/api.OrganizationService/Update',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.UpdateOrganizationRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Delete = channel.unary_unary(
                '/api.OrganizationService/Delete',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.DeleteOrganizationRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ListUsers = channel.unary_unary(
                '/api.OrganizationService/ListUsers',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.ListOrganizationUsersRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.ListOrganizationUsersResponse.FromString,
                )
        self.GetUser = channel.unary_unary(
                '/api.OrganizationService/GetUser',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.GetOrganizationUserRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.GetOrganizationUserResponse.FromString,
                )
        self.AddUser = channel.unary_unary(
                '/api.OrganizationService/AddUser',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.AddOrganizationUserRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.UpdateUser = channel.unary_unary(
                '/api.OrganizationService/UpdateUser',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.UpdateOrganizationUserRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.DeleteUser = channel.unary_unary(
                '/api.OrganizationService/DeleteUser',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.DeleteOrganizationUserRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class OrganizationServiceServicer(object):
    """OrganizationService is the service managing the organization access.
    """

    def List(self, request, context):
        """Get organization list.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Get data for a particular organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Create a new organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Update an existing organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete an organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUsers(self, request, context):
        """Get organization's user list.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUser(self, request, context):
        """Get data for a particular organization user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddUser(self, request, context):
        """Add a new user to an organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Update a user in an organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Delete a user from an organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrganizationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.ListOrganizationRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.ListOrganizationResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.GetOrganizationRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.GetOrganizationResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.CreateOrganizationRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.CreateOrganizationResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.UpdateOrganizationRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.DeleteOrganizationRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ListUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUsers,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.ListOrganizationUsersRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.ListOrganizationUsersResponse.SerializeToString,
            ),
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.GetOrganizationUserRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.GetOrganizationUserResponse.SerializeToString,
            ),
            'AddUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AddUser,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.AddOrganizationUserRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.UpdateOrganizationUserRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'DeleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUser,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.DeleteOrganizationUserRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.OrganizationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OrganizationService(object):
    """OrganizationService is the service managing the organization access.
    """

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.OrganizationService/List',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.ListOrganizationRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.ListOrganizationResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.OrganizationService/Get',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.GetOrganizationRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.GetOrganizationResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.OrganizationService/Create',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.CreateOrganizationRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.CreateOrganizationResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.OrganizationService/Update',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.UpdateOrganizationRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.OrganizationService/Delete',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.DeleteOrganizationRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.OrganizationService/ListUsers',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.ListOrganizationUsersRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.ListOrganizationUsersResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.OrganizationService/GetUser',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.GetOrganizationUserRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.GetOrganizationUserResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.OrganizationService/AddUser',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.AddOrganizationUserRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.OrganizationService/UpdateUser',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.UpdateOrganizationUserRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.OrganizationService/DeleteUser',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_organization__pb2.DeleteOrganizationUserRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
