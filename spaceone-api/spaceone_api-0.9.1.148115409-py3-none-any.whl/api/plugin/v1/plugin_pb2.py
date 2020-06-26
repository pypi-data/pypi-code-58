# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/plugin/v1/plugin.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='spaceone/api/plugin/v1/plugin.proto',
  package='spaceone.api.plugin.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#spaceone/api/plugin/v1/plugin.proto\x12\x16spaceone.api.plugin.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\"w\n\x15PluginEndpointRequest\x12\x11\n\tplugin_id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\'\n\x06labels\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x04 \x01(\t\"d\n\x14PluginFailureRequest\x12\x15\n\rsupervisor_id\x18\x01 \x01(\t\x12\x11\n\tplugin_id\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x11\n\tdomain_id\x18\x04 \x01(\t\"8\n\x0ePluginEndpoint\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\t2\xba\x02\n\x06Plugin\x12\xa0\x01\n\x13get_plugin_endpoint\x12-.spaceone.api.plugin.v1.PluginEndpointRequest\x1a&.spaceone.api.plugin.v1.PluginEndpoint\"2\x82\xd3\xe4\x93\x02,\"*/plugin/v1/plugin/{plugin_id}/get-endpoint\x12\x8c\x01\n\x0enotify_failure\x12,.spaceone.api.plugin.v1.PluginFailureRequest\x1a\x16.google.protobuf.Empty\"4\x82\xd3\xe4\x93\x02.\x1a,/plugin/v1/plugin/{plugin_id}/notify-failureb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_PLUGINENDPOINTREQUEST = _descriptor.Descriptor(
  name='PluginEndpointRequest',
  full_name='spaceone.api.plugin.v1.PluginEndpointRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='plugin_id', full_name='spaceone.api.plugin.v1.PluginEndpointRequest.plugin_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='spaceone.api.plugin.v1.PluginEndpointRequest.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='spaceone.api.plugin.v1.PluginEndpointRequest.labels', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.plugin.v1.PluginEndpointRequest.domain_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=271,
)


_PLUGINFAILUREREQUEST = _descriptor.Descriptor(
  name='PluginFailureRequest',
  full_name='spaceone.api.plugin.v1.PluginFailureRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='supervisor_id', full_name='spaceone.api.plugin.v1.PluginFailureRequest.supervisor_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='plugin_id', full_name='spaceone.api.plugin.v1.PluginFailureRequest.plugin_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='spaceone.api.plugin.v1.PluginFailureRequest.version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.plugin.v1.PluginFailureRequest.domain_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=373,
)


_PLUGINENDPOINT = _descriptor.Descriptor(
  name='PluginEndpoint',
  full_name='spaceone.api.plugin.v1.PluginEndpoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='spaceone.api.plugin.v1.PluginEndpoint.endpoint', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_token', full_name='spaceone.api.plugin.v1.PluginEndpoint.access_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=375,
  serialized_end=431,
)

_PLUGINENDPOINTREQUEST.fields_by_name['labels'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['PluginEndpointRequest'] = _PLUGINENDPOINTREQUEST
DESCRIPTOR.message_types_by_name['PluginFailureRequest'] = _PLUGINFAILUREREQUEST
DESCRIPTOR.message_types_by_name['PluginEndpoint'] = _PLUGINENDPOINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PluginEndpointRequest = _reflection.GeneratedProtocolMessageType('PluginEndpointRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINENDPOINTREQUEST,
  '__module__' : 'spaceone.api.plugin.v1.plugin_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.plugin.v1.PluginEndpointRequest)
  })
_sym_db.RegisterMessage(PluginEndpointRequest)

PluginFailureRequest = _reflection.GeneratedProtocolMessageType('PluginFailureRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINFAILUREREQUEST,
  '__module__' : 'spaceone.api.plugin.v1.plugin_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.plugin.v1.PluginFailureRequest)
  })
_sym_db.RegisterMessage(PluginFailureRequest)

PluginEndpoint = _reflection.GeneratedProtocolMessageType('PluginEndpoint', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINENDPOINT,
  '__module__' : 'spaceone.api.plugin.v1.plugin_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.plugin.v1.PluginEndpoint)
  })
_sym_db.RegisterMessage(PluginEndpoint)



_PLUGIN = _descriptor.ServiceDescriptor(
  name='Plugin',
  full_name='spaceone.api.plugin.v1.Plugin',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=434,
  serialized_end=748,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_plugin_endpoint',
    full_name='spaceone.api.plugin.v1.Plugin.get_plugin_endpoint',
    index=0,
    containing_service=None,
    input_type=_PLUGINENDPOINTREQUEST,
    output_type=_PLUGINENDPOINT,
    serialized_options=b'\202\323\344\223\002,\"*/plugin/v1/plugin/{plugin_id}/get-endpoint',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='notify_failure',
    full_name='spaceone.api.plugin.v1.Plugin.notify_failure',
    index=1,
    containing_service=None,
    input_type=_PLUGINFAILUREREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002.\032,/plugin/v1/plugin/{plugin_id}/notify-failure',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PLUGIN)

DESCRIPTOR.services_by_name['Plugin'] = _PLUGIN

# @@protoc_insertion_point(module_scope)
