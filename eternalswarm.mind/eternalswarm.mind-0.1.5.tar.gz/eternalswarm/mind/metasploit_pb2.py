# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metasploit.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import models_pb2 as models__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='metasploit.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x10metasploit.proto\x1a\x0cmodels.proto\"-\n\x0e\x43onsoleMessage\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"-\n\rSessionOutput\x12\x0b\n\x03sid\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"C\n\x07\x43onsole\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06prompt\x18\x02 \x01(\t\x12\x0c\n\x04\x62usy\x18\x03 \x01(\x08\x12\x0e\n\x06log_id\x18\x04 \x01(\x05\")\n\x0b\x43onsoleList\x12\x1a\n\x08\x63onsoles\x18\x01 \x03(\x0b\x32\x08.Console\"Q\n\x11\x43onsoleOutputList\x12\r\n\x05total\x18\x01 \x01(\x05\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x1e\n\x06output\x18\x03 \x03(\x0b\x32\x0e.ConsoleOutput\"<\n\rConsoleOutput\x12\x0e\n\x06output\x18\x01 \x01(\t\x12\x0b\n\x03\x63id\x18\x02 \x01(\t\x12\x0e\n\x06prompt\x18\x03 \x01(\t\"\xe8\x02\n\x11MetasploitSession\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x14\n\x0ctunnel_local\x18\x03 \x01(\t\x12\x13\n\x0btunnel_peer\x18\x04 \x01(\t\x12\x13\n\x0bvia_exploit\x18\x05 \x01(\t\x12\x13\n\x0bvia_payload\x18\x06 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x07 \x01(\t\x12\x0c\n\x04info\x18\x08 \x01(\t\x12\x11\n\tworkspace\x18\t \x01(\t\x12\x14\n\x0csession_host\x18\n \x01(\t\x12\x14\n\x0csession_port\x18\x0b \x01(\x05\x12\x13\n\x0btarget_host\x18\x0c \x01(\t\x12\x10\n\x08username\x18\r \x01(\t\x12\x0c\n\x04uuid\x18\x0e \x01(\t\x12\x14\n\x0c\x65xploit_uuid\x18\x0f \x01(\t\x12\x0e\n\x06routes\x18\x10 \x01(\t\x12\x0c\n\x04\x61rch\x18\x11 \x01(\t\x12\x10\n\x08platform\x18\x12 \x01(\t\x12\x0e\n\x06log_id\x18\x13 \x01(\x05\"=\n\x15MetasploitSessionList\x12$\n\x08sessions\x18\x01 \x03(\x0b\x32\x12.MetasploitSession2\xa0\x04\n\nMetasploit\x12*\n\x08ListJobs\x12\r.EmptyRequest\x1a\r.EmptyMessage\"\x00\x12,\n\x0cListExploits\x12\x0b.Pagination\x1a\r.EmptyMessage\"\x00\x12-\n\x0cListConsoles\x12\r.EmptyRequest\x1a\x0c.ConsoleList\"\x00\x12\x37\n\x0cListSessions\x12\r.EmptyRequest\x1a\x16.MetasploitSessionList\"\x00\x12\"\n\nGetConsole\x12\x08.Console\x1a\x08.Console\"\x00\x12\x36\n\nGetSession\x12\x12.MetasploitSession\x1a\x12.MetasploitSession\"\x00\x12*\n\rCreateConsole\x12\r.EmptyRequest\x1a\x08.Console\"\x00\x12(\n\x0bStopConsole\x12\x08.Console\x1a\r.EmptyMessage\"\x00\x12\x36\n\x11ListConsoleOutput\x12\x0b.Pagination\x1a\x12.ConsoleOutputList\"\x00\x12\x32\n\x0eWriteToConsole\x12\x0f.ConsoleMessage\x1a\r.EmptyMessage\"\x00\x12\x32\n\x0eWriteToSession\x12\x0f.ConsoleMessage\x1a\r.EmptyMessage\"\x00\x62\x06proto3'
  ,
  dependencies=[models__pb2.DESCRIPTOR,])




_CONSOLEMESSAGE = _descriptor.Descriptor(
  name='ConsoleMessage',
  full_name='ConsoleMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ConsoleMessage.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='ConsoleMessage.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=34,
  serialized_end=79,
)


_SESSIONOUTPUT = _descriptor.Descriptor(
  name='SessionOutput',
  full_name='SessionOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sid', full_name='SessionOutput.sid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='SessionOutput.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=81,
  serialized_end=126,
)


_CONSOLE = _descriptor.Descriptor(
  name='Console',
  full_name='Console',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Console.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prompt', full_name='Console.prompt', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='busy', full_name='Console.busy', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_id', full_name='Console.log_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=128,
  serialized_end=195,
)


_CONSOLELIST = _descriptor.Descriptor(
  name='ConsoleList',
  full_name='ConsoleList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='consoles', full_name='ConsoleList.consoles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=197,
  serialized_end=238,
)


_CONSOLEOUTPUTLIST = _descriptor.Descriptor(
  name='ConsoleOutputList',
  full_name='ConsoleOutputList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total', full_name='ConsoleOutputList.total', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='ConsoleOutputList.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output', full_name='ConsoleOutputList.output', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=240,
  serialized_end=321,
)


_CONSOLEOUTPUT = _descriptor.Descriptor(
  name='ConsoleOutput',
  full_name='ConsoleOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='output', full_name='ConsoleOutput.output', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cid', full_name='ConsoleOutput.cid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prompt', full_name='ConsoleOutput.prompt', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=323,
  serialized_end=383,
)


_METASPLOITSESSION = _descriptor.Descriptor(
  name='MetasploitSession',
  full_name='MetasploitSession',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='MetasploitSession.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='MetasploitSession.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tunnel_local', full_name='MetasploitSession.tunnel_local', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tunnel_peer', full_name='MetasploitSession.tunnel_peer', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='via_exploit', full_name='MetasploitSession.via_exploit', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='via_payload', full_name='MetasploitSession.via_payload', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desc', full_name='MetasploitSession.desc', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='MetasploitSession.info', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workspace', full_name='MetasploitSession.workspace', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_host', full_name='MetasploitSession.session_host', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session_port', full_name='MetasploitSession.session_port', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_host', full_name='MetasploitSession.target_host', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='MetasploitSession.username', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='MetasploitSession.uuid', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exploit_uuid', full_name='MetasploitSession.exploit_uuid', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='routes', full_name='MetasploitSession.routes', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arch', full_name='MetasploitSession.arch', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='platform', full_name='MetasploitSession.platform', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_id', full_name='MetasploitSession.log_id', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=386,
  serialized_end=746,
)


_METASPLOITSESSIONLIST = _descriptor.Descriptor(
  name='MetasploitSessionList',
  full_name='MetasploitSessionList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sessions', full_name='MetasploitSessionList.sessions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=748,
  serialized_end=809,
)

_CONSOLELIST.fields_by_name['consoles'].message_type = _CONSOLE
_CONSOLEOUTPUTLIST.fields_by_name['output'].message_type = _CONSOLEOUTPUT
_METASPLOITSESSIONLIST.fields_by_name['sessions'].message_type = _METASPLOITSESSION
DESCRIPTOR.message_types_by_name['ConsoleMessage'] = _CONSOLEMESSAGE
DESCRIPTOR.message_types_by_name['SessionOutput'] = _SESSIONOUTPUT
DESCRIPTOR.message_types_by_name['Console'] = _CONSOLE
DESCRIPTOR.message_types_by_name['ConsoleList'] = _CONSOLELIST
DESCRIPTOR.message_types_by_name['ConsoleOutputList'] = _CONSOLEOUTPUTLIST
DESCRIPTOR.message_types_by_name['ConsoleOutput'] = _CONSOLEOUTPUT
DESCRIPTOR.message_types_by_name['MetasploitSession'] = _METASPLOITSESSION
DESCRIPTOR.message_types_by_name['MetasploitSessionList'] = _METASPLOITSESSIONLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConsoleMessage = _reflection.GeneratedProtocolMessageType('ConsoleMessage', (_message.Message,), {
  'DESCRIPTOR' : _CONSOLEMESSAGE,
  '__module__' : 'metasploit_pb2'
  # @@protoc_insertion_point(class_scope:ConsoleMessage)
  })
_sym_db.RegisterMessage(ConsoleMessage)

SessionOutput = _reflection.GeneratedProtocolMessageType('SessionOutput', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONOUTPUT,
  '__module__' : 'metasploit_pb2'
  # @@protoc_insertion_point(class_scope:SessionOutput)
  })
_sym_db.RegisterMessage(SessionOutput)

Console = _reflection.GeneratedProtocolMessageType('Console', (_message.Message,), {
  'DESCRIPTOR' : _CONSOLE,
  '__module__' : 'metasploit_pb2'
  # @@protoc_insertion_point(class_scope:Console)
  })
_sym_db.RegisterMessage(Console)

ConsoleList = _reflection.GeneratedProtocolMessageType('ConsoleList', (_message.Message,), {
  'DESCRIPTOR' : _CONSOLELIST,
  '__module__' : 'metasploit_pb2'
  # @@protoc_insertion_point(class_scope:ConsoleList)
  })
_sym_db.RegisterMessage(ConsoleList)

ConsoleOutputList = _reflection.GeneratedProtocolMessageType('ConsoleOutputList', (_message.Message,), {
  'DESCRIPTOR' : _CONSOLEOUTPUTLIST,
  '__module__' : 'metasploit_pb2'
  # @@protoc_insertion_point(class_scope:ConsoleOutputList)
  })
_sym_db.RegisterMessage(ConsoleOutputList)

ConsoleOutput = _reflection.GeneratedProtocolMessageType('ConsoleOutput', (_message.Message,), {
  'DESCRIPTOR' : _CONSOLEOUTPUT,
  '__module__' : 'metasploit_pb2'
  # @@protoc_insertion_point(class_scope:ConsoleOutput)
  })
_sym_db.RegisterMessage(ConsoleOutput)

MetasploitSession = _reflection.GeneratedProtocolMessageType('MetasploitSession', (_message.Message,), {
  'DESCRIPTOR' : _METASPLOITSESSION,
  '__module__' : 'metasploit_pb2'
  # @@protoc_insertion_point(class_scope:MetasploitSession)
  })
_sym_db.RegisterMessage(MetasploitSession)

MetasploitSessionList = _reflection.GeneratedProtocolMessageType('MetasploitSessionList', (_message.Message,), {
  'DESCRIPTOR' : _METASPLOITSESSIONLIST,
  '__module__' : 'metasploit_pb2'
  # @@protoc_insertion_point(class_scope:MetasploitSessionList)
  })
_sym_db.RegisterMessage(MetasploitSessionList)



_METASPLOIT = _descriptor.ServiceDescriptor(
  name='Metasploit',
  full_name='Metasploit',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=812,
  serialized_end=1356,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListJobs',
    full_name='Metasploit.ListJobs',
    index=0,
    containing_service=None,
    input_type=models__pb2._EMPTYREQUEST,
    output_type=models__pb2._EMPTYMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListExploits',
    full_name='Metasploit.ListExploits',
    index=1,
    containing_service=None,
    input_type=models__pb2._PAGINATION,
    output_type=models__pb2._EMPTYMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListConsoles',
    full_name='Metasploit.ListConsoles',
    index=2,
    containing_service=None,
    input_type=models__pb2._EMPTYREQUEST,
    output_type=_CONSOLELIST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListSessions',
    full_name='Metasploit.ListSessions',
    index=3,
    containing_service=None,
    input_type=models__pb2._EMPTYREQUEST,
    output_type=_METASPLOITSESSIONLIST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetConsole',
    full_name='Metasploit.GetConsole',
    index=4,
    containing_service=None,
    input_type=_CONSOLE,
    output_type=_CONSOLE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetSession',
    full_name='Metasploit.GetSession',
    index=5,
    containing_service=None,
    input_type=_METASPLOITSESSION,
    output_type=_METASPLOITSESSION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateConsole',
    full_name='Metasploit.CreateConsole',
    index=6,
    containing_service=None,
    input_type=models__pb2._EMPTYREQUEST,
    output_type=_CONSOLE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StopConsole',
    full_name='Metasploit.StopConsole',
    index=7,
    containing_service=None,
    input_type=_CONSOLE,
    output_type=models__pb2._EMPTYMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListConsoleOutput',
    full_name='Metasploit.ListConsoleOutput',
    index=8,
    containing_service=None,
    input_type=models__pb2._PAGINATION,
    output_type=_CONSOLEOUTPUTLIST,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='WriteToConsole',
    full_name='Metasploit.WriteToConsole',
    index=9,
    containing_service=None,
    input_type=_CONSOLEMESSAGE,
    output_type=models__pb2._EMPTYMESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='WriteToSession',
    full_name='Metasploit.WriteToSession',
    index=10,
    containing_service=None,
    input_type=_CONSOLEMESSAGE,
    output_type=models__pb2._EMPTYMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_METASPLOIT)

DESCRIPTOR.services_by_name['Metasploit'] = _METASPLOIT

# @@protoc_insertion_point(module_scope)
