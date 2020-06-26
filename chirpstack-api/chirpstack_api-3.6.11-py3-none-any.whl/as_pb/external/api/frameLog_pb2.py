# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/as_pb/external/api/frameLog.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from chirpstack_api.common import common_pb2 as chirpstack__api_dot_common_dot_common__pb2
from chirpstack_api.gw import gw_pb2 as chirpstack__api_dot_gw_dot_gw__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chirpstack-api/as_pb/external/api/frameLog.proto',
  package='api',
  syntax='proto3',
  serialized_options=b'Z7github.com/brocaar/chirpstack-api/go/v3/as/external/api',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n0chirpstack-api/as_pb/external/api/frameLog.proto\x12\x03\x61pi\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\"chirpstack-api/common/common.proto\x1a\x1a\x63hirpstack-api/gw/gw.proto\"\x80\x01\n\x0eUplinkFrameLog\x12!\n\x07tx_info\x18\x01 \x01(\x0b\x32\x10.gw.UplinkTXInfo\x12!\n\x07rx_info\x18\x02 \x03(\x0b\x32\x10.gw.UplinkRXInfo\x12(\n\x10phy_payload_json\x18\x03 \x01(\tR\x0ephyPayloadJSON\"\x80\x01\n\x10\x44ownlinkFrameLog\x12#\n\x07tx_info\x18\x01 \x01(\x0b\x32\x12.gw.DownlinkTXInfo\x12(\n\x10phy_payload_json\x18\x02 \x01(\tR\x0ephyPayloadJSON\x12\x1d\n\ngateway_id\x18\x03 \x01(\tR\tgatewayID*\x1c\n\x08RXWindow\x12\x07\n\x03RX1\x10\x00\x12\x07\n\x03RX2\x10\x01\x42\x39Z7github.com/brocaar/chirpstack-api/go/v3/as/external/apib\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,chirpstack__api_dot_common_dot_common__pb2.DESCRIPTOR,chirpstack__api_dot_gw_dot_gw__pb2.DESCRIPTOR,])

_RXWINDOW = _descriptor.EnumDescriptor(
  name='RXWindow',
  full_name='api.RXWindow',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RX1', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RX2', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=448,
  serialized_end=476,
)
_sym_db.RegisterEnumDescriptor(_RXWINDOW)

RXWindow = enum_type_wrapper.EnumTypeWrapper(_RXWINDOW)
RX1 = 0
RX2 = 1



_UPLINKFRAMELOG = _descriptor.Descriptor(
  name='UplinkFrameLog',
  full_name='api.UplinkFrameLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_info', full_name='api.UplinkFrameLog.tx_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rx_info', full_name='api.UplinkFrameLog.rx_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phy_payload_json', full_name='api.UplinkFrameLog.phy_payload_json', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='phyPayloadJSON', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=187,
  serialized_end=315,
)


_DOWNLINKFRAMELOG = _descriptor.Descriptor(
  name='DownlinkFrameLog',
  full_name='api.DownlinkFrameLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_info', full_name='api.DownlinkFrameLog.tx_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phy_payload_json', full_name='api.DownlinkFrameLog.phy_payload_json', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='phyPayloadJSON', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gateway_id', full_name='api.DownlinkFrameLog.gateway_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='gatewayID', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=318,
  serialized_end=446,
)

_UPLINKFRAMELOG.fields_by_name['tx_info'].message_type = chirpstack__api_dot_gw_dot_gw__pb2._UPLINKTXINFO
_UPLINKFRAMELOG.fields_by_name['rx_info'].message_type = chirpstack__api_dot_gw_dot_gw__pb2._UPLINKRXINFO
_DOWNLINKFRAMELOG.fields_by_name['tx_info'].message_type = chirpstack__api_dot_gw_dot_gw__pb2._DOWNLINKTXINFO
DESCRIPTOR.message_types_by_name['UplinkFrameLog'] = _UPLINKFRAMELOG
DESCRIPTOR.message_types_by_name['DownlinkFrameLog'] = _DOWNLINKFRAMELOG
DESCRIPTOR.enum_types_by_name['RXWindow'] = _RXWINDOW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UplinkFrameLog = _reflection.GeneratedProtocolMessageType('UplinkFrameLog', (_message.Message,), {
  'DESCRIPTOR' : _UPLINKFRAMELOG,
  '__module__' : 'chirpstack_api.as_pb.external.api.frameLog_pb2'
  # @@protoc_insertion_point(class_scope:api.UplinkFrameLog)
  })
_sym_db.RegisterMessage(UplinkFrameLog)

DownlinkFrameLog = _reflection.GeneratedProtocolMessageType('DownlinkFrameLog', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLINKFRAMELOG,
  '__module__' : 'chirpstack_api.as_pb.external.api.frameLog_pb2'
  # @@protoc_insertion_point(class_scope:api.DownlinkFrameLog)
  })
_sym_db.RegisterMessage(DownlinkFrameLog)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
