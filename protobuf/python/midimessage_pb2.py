# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: midimessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='midimessage.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11midimessage.proto\"\x9c\x01\n\x0fPortDescription\x12-\n\tdirection\x18\x01 \x01(\x0e\x32\x1a.PortDescription.Direction\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x16\n\x0e\x63reate_dynamic\x18\x03 \x01(\x08\x12\x0b\n\x03key\x18\x04 \x01(\x05\"\'\n\tDirection\x12\x06\n\x02IN\x10\x00\x12\x07\n\x03OUT\x10\x01\x12\t\n\x05INOUT\x10\x02\"+\n\x08PortList\x12\x1f\n\x05ports\x18\x01 \x03(\x0b\x32\x10.PortDescription\"B\n\x10PublishedMessage\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x0e\n\x06sender\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\x0c\"O\n\x10SubscribeRequest\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x13\n\x0brequestNode\x18\x02 \x01(\t\x12\x17\n\x0fis_subscription\x18\x03 \x01(\x08\"\xa5\x01\n\x0fMessageMetadata\x12\x0c\n\x04port\x18\x01 \x01(\r\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x15\n\rfriendly_name\x18\x03 \x01(\t\x12\x11\n\tis_master\x18\x04 \x01(\x08\x12\x18\n\x10software_package\x18\x05 \x01(\t\x12\x18\n\x10software_version\x18\x06 \x01(\t\x12\x18\n\x05ports\x18\x07 \x01(\x0b\x32\t.PortList\"\x8e\x01\n\x05\x45rror\x12\x12\n\nerror_type\x18\x01 \x01(\t\x12&\n\x08severity\x18\x02 \x01(\x0e\x32\x14.Error.ErrorSeverity\"I\n\rErrorSeverity\x12\x0f\n\x0b\x44\x45PRECATION\x10\x00\x12\x0b\n\x07WARNING\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\x0f\n\x0b\x43\x41TASTROPHE\x10\x03\")\n\x08MidiData\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\x9d\x04\n\x0bMidiMessage\x12\x12\n\nmessage_id\x18\x01 \x01(\t\x12\x14\n\x0clast_message\x18\x02 \x01(\t\x12/\n\x0cmessage_type\x18\x05 \x01(\x0e\x32\x19.MidiMessage.MessageTypes\x12,\n\x10message_metadata\x18\x06 \x01(\x0b\x32\x10.MessageMetadataH\x00\x12\x17\n\x05\x65rror\x18\x07 \x01(\x0b\x32\x06.ErrorH\x00\x12\x1e\n\tmidi_data\x18\x08 \x01(\x0b\x32\t.MidiDataH\x00\x12\x17\n\racked_message\x18\t \x01(\tH\x00\x12\x1a\n\x05ports\x18\n \x01(\x0b\x32\t.PortListH\x00\x12.\n\x11published_message\x18\x0b \x01(\x0b\x32\x11.PublishedMessageH\x00\x12.\n\x11subscribe_request\x18\x0c \x01(\x0b\x32\x11.SubscribeRequestH\x00\"\xab\x01\n\x0cMessageTypes\x12\x11\n\rHOST_ANNOUNCE\x10\x00\x12\x0f\n\x0bHOST_RETIRE\x10\x01\x12\x14\n\x10RESEND_REQUESTED\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\r\n\tMIDI_DATA\x10\x04\x12\x07\n\x03\x41\x43K\x10\x05\x12\x10\n\x0cPORT_REQUEST\x10\x06\x12\x15\n\x11PUBLISHED_MESSAGE\x10\x07\x12\x15\n\x11SUBSCRIBE_REQUEST\x10\x08\x42\t\n\x07payloadb\x06proto3')
)



_PORTDESCRIPTION_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='PortDescription.Direction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INOUT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=139,
  serialized_end=178,
)
_sym_db.RegisterEnumDescriptor(_PORTDESCRIPTION_DIRECTION)

_ERROR_ERRORSEVERITY = _descriptor.EnumDescriptor(
  name='ErrorSeverity',
  full_name='Error.ErrorSeverity',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEPRECATION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATASTROPHE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=612,
  serialized_end=685,
)
_sym_db.RegisterEnumDescriptor(_ERROR_ERRORSEVERITY)

_MIDIMESSAGE_MESSAGETYPES = _descriptor.EnumDescriptor(
  name='MessageTypes',
  full_name='MidiMessage.MessageTypes',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HOST_ANNOUNCE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOST_RETIRE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESEND_REQUESTED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIDI_DATA', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACK', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PORT_REQUEST', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PUBLISHED_MESSAGE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUBSCRIBE_REQUEST', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1090,
  serialized_end=1261,
)
_sym_db.RegisterEnumDescriptor(_MIDIMESSAGE_MESSAGETYPES)


_PORTDESCRIPTION = _descriptor.Descriptor(
  name='PortDescription',
  full_name='PortDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='direction', full_name='PortDescription.direction', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='PortDescription.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_dynamic', full_name='PortDescription.create_dynamic', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='PortDescription.key', index=3,
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
    _PORTDESCRIPTION_DIRECTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=178,
)


_PORTLIST = _descriptor.Descriptor(
  name='PortList',
  full_name='PortList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ports', full_name='PortList.ports', index=0,
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
  serialized_start=180,
  serialized_end=223,
)


_PUBLISHEDMESSAGE = _descriptor.Descriptor(
  name='PublishedMessage',
  full_name='PublishedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic', full_name='PublishedMessage.topic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender', full_name='PublishedMessage.sender', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='PublishedMessage.message', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=225,
  serialized_end=291,
)


_SUBSCRIBEREQUEST = _descriptor.Descriptor(
  name='SubscribeRequest',
  full_name='SubscribeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic', full_name='SubscribeRequest.topic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requestNode', full_name='SubscribeRequest.requestNode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_subscription', full_name='SubscribeRequest.is_subscription', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=293,
  serialized_end=372,
)


_MESSAGEMETADATA = _descriptor.Descriptor(
  name='MessageMetadata',
  full_name='MessageMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port', full_name='MessageMetadata.port', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='MessageMetadata.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='friendly_name', full_name='MessageMetadata.friendly_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_master', full_name='MessageMetadata.is_master', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='software_package', full_name='MessageMetadata.software_package', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='software_version', full_name='MessageMetadata.software_version', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ports', full_name='MessageMetadata.ports', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=375,
  serialized_end=540,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_type', full_name='Error.error_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='severity', full_name='Error.severity', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ERROR_ERRORSEVERITY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=543,
  serialized_end=685,
)


_MIDIDATA = _descriptor.Descriptor(
  name='MidiData',
  full_name='MidiData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='MidiData.channel', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='MidiData.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=687,
  serialized_end=728,
)


_MIDIMESSAGE = _descriptor.Descriptor(
  name='MidiMessage',
  full_name='MidiMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_id', full_name='MidiMessage.message_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_message', full_name='MidiMessage.last_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message_type', full_name='MidiMessage.message_type', index=2,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message_metadata', full_name='MidiMessage.message_metadata', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='MidiMessage.error', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='midi_data', full_name='MidiMessage.midi_data', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acked_message', full_name='MidiMessage.acked_message', index=6,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ports', full_name='MidiMessage.ports', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='published_message', full_name='MidiMessage.published_message', index=8,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscribe_request', full_name='MidiMessage.subscribe_request', index=9,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MIDIMESSAGE_MESSAGETYPES,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='MidiMessage.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=731,
  serialized_end=1272,
)

_PORTDESCRIPTION.fields_by_name['direction'].enum_type = _PORTDESCRIPTION_DIRECTION
_PORTDESCRIPTION_DIRECTION.containing_type = _PORTDESCRIPTION
_PORTLIST.fields_by_name['ports'].message_type = _PORTDESCRIPTION
_MESSAGEMETADATA.fields_by_name['ports'].message_type = _PORTLIST
_ERROR.fields_by_name['severity'].enum_type = _ERROR_ERRORSEVERITY
_ERROR_ERRORSEVERITY.containing_type = _ERROR
_MIDIMESSAGE.fields_by_name['message_type'].enum_type = _MIDIMESSAGE_MESSAGETYPES
_MIDIMESSAGE.fields_by_name['message_metadata'].message_type = _MESSAGEMETADATA
_MIDIMESSAGE.fields_by_name['error'].message_type = _ERROR
_MIDIMESSAGE.fields_by_name['midi_data'].message_type = _MIDIDATA
_MIDIMESSAGE.fields_by_name['ports'].message_type = _PORTLIST
_MIDIMESSAGE.fields_by_name['published_message'].message_type = _PUBLISHEDMESSAGE
_MIDIMESSAGE.fields_by_name['subscribe_request'].message_type = _SUBSCRIBEREQUEST
_MIDIMESSAGE_MESSAGETYPES.containing_type = _MIDIMESSAGE
_MIDIMESSAGE.oneofs_by_name['payload'].fields.append(
  _MIDIMESSAGE.fields_by_name['message_metadata'])
_MIDIMESSAGE.fields_by_name['message_metadata'].containing_oneof = _MIDIMESSAGE.oneofs_by_name['payload']
_MIDIMESSAGE.oneofs_by_name['payload'].fields.append(
  _MIDIMESSAGE.fields_by_name['error'])
_MIDIMESSAGE.fields_by_name['error'].containing_oneof = _MIDIMESSAGE.oneofs_by_name['payload']
_MIDIMESSAGE.oneofs_by_name['payload'].fields.append(
  _MIDIMESSAGE.fields_by_name['midi_data'])
_MIDIMESSAGE.fields_by_name['midi_data'].containing_oneof = _MIDIMESSAGE.oneofs_by_name['payload']
_MIDIMESSAGE.oneofs_by_name['payload'].fields.append(
  _MIDIMESSAGE.fields_by_name['acked_message'])
_MIDIMESSAGE.fields_by_name['acked_message'].containing_oneof = _MIDIMESSAGE.oneofs_by_name['payload']
_MIDIMESSAGE.oneofs_by_name['payload'].fields.append(
  _MIDIMESSAGE.fields_by_name['ports'])
_MIDIMESSAGE.fields_by_name['ports'].containing_oneof = _MIDIMESSAGE.oneofs_by_name['payload']
_MIDIMESSAGE.oneofs_by_name['payload'].fields.append(
  _MIDIMESSAGE.fields_by_name['published_message'])
_MIDIMESSAGE.fields_by_name['published_message'].containing_oneof = _MIDIMESSAGE.oneofs_by_name['payload']
_MIDIMESSAGE.oneofs_by_name['payload'].fields.append(
  _MIDIMESSAGE.fields_by_name['subscribe_request'])
_MIDIMESSAGE.fields_by_name['subscribe_request'].containing_oneof = _MIDIMESSAGE.oneofs_by_name['payload']
DESCRIPTOR.message_types_by_name['PortDescription'] = _PORTDESCRIPTION
DESCRIPTOR.message_types_by_name['PortList'] = _PORTLIST
DESCRIPTOR.message_types_by_name['PublishedMessage'] = _PUBLISHEDMESSAGE
DESCRIPTOR.message_types_by_name['SubscribeRequest'] = _SUBSCRIBEREQUEST
DESCRIPTOR.message_types_by_name['MessageMetadata'] = _MESSAGEMETADATA
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.message_types_by_name['MidiData'] = _MIDIDATA
DESCRIPTOR.message_types_by_name['MidiMessage'] = _MIDIMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PortDescription = _reflection.GeneratedProtocolMessageType('PortDescription', (_message.Message,), dict(
  DESCRIPTOR = _PORTDESCRIPTION,
  __module__ = 'midimessage_pb2'
  # @@protoc_insertion_point(class_scope:PortDescription)
  ))
_sym_db.RegisterMessage(PortDescription)

PortList = _reflection.GeneratedProtocolMessageType('PortList', (_message.Message,), dict(
  DESCRIPTOR = _PORTLIST,
  __module__ = 'midimessage_pb2'
  # @@protoc_insertion_point(class_scope:PortList)
  ))
_sym_db.RegisterMessage(PortList)

PublishedMessage = _reflection.GeneratedProtocolMessageType('PublishedMessage', (_message.Message,), dict(
  DESCRIPTOR = _PUBLISHEDMESSAGE,
  __module__ = 'midimessage_pb2'
  # @@protoc_insertion_point(class_scope:PublishedMessage)
  ))
_sym_db.RegisterMessage(PublishedMessage)

SubscribeRequest = _reflection.GeneratedProtocolMessageType('SubscribeRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIBEREQUEST,
  __module__ = 'midimessage_pb2'
  # @@protoc_insertion_point(class_scope:SubscribeRequest)
  ))
_sym_db.RegisterMessage(SubscribeRequest)

MessageMetadata = _reflection.GeneratedProtocolMessageType('MessageMetadata', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGEMETADATA,
  __module__ = 'midimessage_pb2'
  # @@protoc_insertion_point(class_scope:MessageMetadata)
  ))
_sym_db.RegisterMessage(MessageMetadata)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(
  DESCRIPTOR = _ERROR,
  __module__ = 'midimessage_pb2'
  # @@protoc_insertion_point(class_scope:Error)
  ))
_sym_db.RegisterMessage(Error)

MidiData = _reflection.GeneratedProtocolMessageType('MidiData', (_message.Message,), dict(
  DESCRIPTOR = _MIDIDATA,
  __module__ = 'midimessage_pb2'
  # @@protoc_insertion_point(class_scope:MidiData)
  ))
_sym_db.RegisterMessage(MidiData)

MidiMessage = _reflection.GeneratedProtocolMessageType('MidiMessage', (_message.Message,), dict(
  DESCRIPTOR = _MIDIMESSAGE,
  __module__ = 'midimessage_pb2'
  # @@protoc_insertion_point(class_scope:MidiMessage)
  ))
_sym_db.RegisterMessage(MidiMessage)


# @@protoc_insertion_point(module_scope)
