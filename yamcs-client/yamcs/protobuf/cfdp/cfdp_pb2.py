# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yamcs/protobuf/cfdp/cfdp.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yamcs/protobuf/cfdp/cfdp.proto',
  package='yamcs.protobuf.cfdp',
  syntax='proto2',
  serialized_options=_b('\n\022org.yamcs.protobuf'),
  serialized_pb=_b('\n\x1eyamcs/protobuf/cfdp/cfdp.proto\x12\x13yamcs.protobuf.cfdp\x1a\x1fgoogle/protobuf/timestamp.proto\"3\n\nRemoteFile\x12\x10\n\x08\x66ilepath\x18\x01 \x02(\t\x12\x13\n\x0bisDirectory\x18\x02 \x02(\x08\"\xb8\x02\n\x0cTransferInfo\x12\x15\n\rtransactionId\x18\x01 \x01(\x04\x12-\n\tstartTime\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\x05state\x18\x03 \x01(\x0e\x32\".yamcs.protobuf.cfdp.TransferState\x12\x0e\n\x06\x62ucket\x18\x04 \x01(\t\x12\x12\n\nobjectName\x18\x05 \x01(\t\x12\x12\n\nremotePath\x18\x06 \x01(\t\x12\x39\n\tdirection\x18\x07 \x01(\x0e\x32&.yamcs.protobuf.cfdp.TransferDirection\x12\x11\n\ttotalSize\x18\x08 \x01(\x04\x12\x17\n\x0fsizeTransferred\x18\t \x01(\x04\x12\x10\n\x08reliable\x18\n \x01(\x08\"\x8d\x03\n\x15\x43reateTransferRequest\x12\x39\n\tdirection\x18\x01 \x01(\x0e\x32&.yamcs.protobuf.cfdp.TransferDirection\x12\x0e\n\x06\x62ucket\x18\x02 \x01(\t\x12\x12\n\nobjectName\x18\x03 \x01(\t\x12\x12\n\nremotePath\x18\x04 \x01(\t\x12S\n\x0f\x64ownloadOptions\x18\x05 \x01(\x0b\x32:.yamcs.protobuf.cfdp.CreateTransferRequest.DownloadOptions\x12O\n\ruploadOptions\x18\x06 \x01(\x0b\x32\x38.yamcs.protobuf.cfdp.CreateTransferRequest.UploadOptions\x1aH\n\rUploadOptions\x12\x11\n\toverwrite\x18\x01 \x01(\x08\x12\x12\n\ncreatePath\x18\x02 \x01(\x08\x12\x10\n\x08reliable\x18\x03 \x01(\x08\x1a\x11\n\x0f\x44ownloadOptions\"(\n\x13\x45\x64itTransferRequest\x12\x11\n\toperation\x18\x01 \x01(\t\"L\n\x15ListTransfersResponse\x12\x33\n\x08transfer\x18\x01 \x03(\x0b\x32!.yamcs.protobuf.cfdp.TransferInfo\"a\n\x17ListRemoteFilesResponse\x12\x12\n\nremotePath\x18\x01 \x02(\t\x12\x32\n\tfilepaths\x18\x02 \x03(\x0b\x32\x1f.yamcs.protobuf.cfdp.RemoteFile*-\n\x11TransferDirection\x12\n\n\x06UPLOAD\x10\x01\x12\x0c\n\x08\x44OWNLOAD\x10\x02*C\n\rTransferState\x12\x0b\n\x07RUNNING\x10\x01\x12\n\n\x06PAUSED\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\x12\r\n\tCOMPLETED\x10\x04\x42\x14\n\x12org.yamcs.protobuf')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_TRANSFERDIRECTION = _descriptor.EnumDescriptor(
  name='TransferDirection',
  full_name='yamcs.protobuf.cfdp.TransferDirection',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UPLOAD', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWNLOAD', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1075,
  serialized_end=1120,
)
_sym_db.RegisterEnumDescriptor(_TRANSFERDIRECTION)

TransferDirection = enum_type_wrapper.EnumTypeWrapper(_TRANSFERDIRECTION)
_TRANSFERSTATE = _descriptor.EnumDescriptor(
  name='TransferState',
  full_name='yamcs.protobuf.cfdp.TransferState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAUSED', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=3, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1122,
  serialized_end=1189,
)
_sym_db.RegisterEnumDescriptor(_TRANSFERSTATE)

TransferState = enum_type_wrapper.EnumTypeWrapper(_TRANSFERSTATE)
UPLOAD = 1
DOWNLOAD = 2
RUNNING = 1
PAUSED = 2
FAILED = 3
COMPLETED = 4



_REMOTEFILE = _descriptor.Descriptor(
  name='RemoteFile',
  full_name='yamcs.protobuf.cfdp.RemoteFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filepath', full_name='yamcs.protobuf.cfdp.RemoteFile.filepath', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isDirectory', full_name='yamcs.protobuf.cfdp.RemoteFile.isDirectory', index=1,
      number=2, type=8, cpp_type=7, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=139,
)


_TRANSFERINFO = _descriptor.Descriptor(
  name='TransferInfo',
  full_name='yamcs.protobuf.cfdp.TransferInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactionId', full_name='yamcs.protobuf.cfdp.TransferInfo.transactionId', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='yamcs.protobuf.cfdp.TransferInfo.startTime', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='yamcs.protobuf.cfdp.TransferInfo.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bucket', full_name='yamcs.protobuf.cfdp.TransferInfo.bucket', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectName', full_name='yamcs.protobuf.cfdp.TransferInfo.objectName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remotePath', full_name='yamcs.protobuf.cfdp.TransferInfo.remotePath', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction', full_name='yamcs.protobuf.cfdp.TransferInfo.direction', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalSize', full_name='yamcs.protobuf.cfdp.TransferInfo.totalSize', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sizeTransferred', full_name='yamcs.protobuf.cfdp.TransferInfo.sizeTransferred', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reliable', full_name='yamcs.protobuf.cfdp.TransferInfo.reliable', index=9,
      number=10, type=8, cpp_type=7, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=454,
)


_CREATETRANSFERREQUEST_UPLOADOPTIONS = _descriptor.Descriptor(
  name='UploadOptions',
  full_name='yamcs.protobuf.cfdp.CreateTransferRequest.UploadOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='overwrite', full_name='yamcs.protobuf.cfdp.CreateTransferRequest.UploadOptions.overwrite', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='createPath', full_name='yamcs.protobuf.cfdp.CreateTransferRequest.UploadOptions.createPath', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reliable', full_name='yamcs.protobuf.cfdp.CreateTransferRequest.UploadOptions.reliable', index=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=763,
  serialized_end=835,
)

_CREATETRANSFERREQUEST_DOWNLOADOPTIONS = _descriptor.Descriptor(
  name='DownloadOptions',
  full_name='yamcs.protobuf.cfdp.CreateTransferRequest.DownloadOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=837,
  serialized_end=854,
)

_CREATETRANSFERREQUEST = _descriptor.Descriptor(
  name='CreateTransferRequest',
  full_name='yamcs.protobuf.cfdp.CreateTransferRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='direction', full_name='yamcs.protobuf.cfdp.CreateTransferRequest.direction', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bucket', full_name='yamcs.protobuf.cfdp.CreateTransferRequest.bucket', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='objectName', full_name='yamcs.protobuf.cfdp.CreateTransferRequest.objectName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remotePath', full_name='yamcs.protobuf.cfdp.CreateTransferRequest.remotePath', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='downloadOptions', full_name='yamcs.protobuf.cfdp.CreateTransferRequest.downloadOptions', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uploadOptions', full_name='yamcs.protobuf.cfdp.CreateTransferRequest.uploadOptions', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATETRANSFERREQUEST_UPLOADOPTIONS, _CREATETRANSFERREQUEST_DOWNLOADOPTIONS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=457,
  serialized_end=854,
)


_EDITTRANSFERREQUEST = _descriptor.Descriptor(
  name='EditTransferRequest',
  full_name='yamcs.protobuf.cfdp.EditTransferRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='yamcs.protobuf.cfdp.EditTransferRequest.operation', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=856,
  serialized_end=896,
)


_LISTTRANSFERSRESPONSE = _descriptor.Descriptor(
  name='ListTransfersResponse',
  full_name='yamcs.protobuf.cfdp.ListTransfersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transfer', full_name='yamcs.protobuf.cfdp.ListTransfersResponse.transfer', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=898,
  serialized_end=974,
)


_LISTREMOTEFILESRESPONSE = _descriptor.Descriptor(
  name='ListRemoteFilesResponse',
  full_name='yamcs.protobuf.cfdp.ListRemoteFilesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='remotePath', full_name='yamcs.protobuf.cfdp.ListRemoteFilesResponse.remotePath', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filepaths', full_name='yamcs.protobuf.cfdp.ListRemoteFilesResponse.filepaths', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=976,
  serialized_end=1073,
)

_TRANSFERINFO.fields_by_name['startTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRANSFERINFO.fields_by_name['state'].enum_type = _TRANSFERSTATE
_TRANSFERINFO.fields_by_name['direction'].enum_type = _TRANSFERDIRECTION
_CREATETRANSFERREQUEST_UPLOADOPTIONS.containing_type = _CREATETRANSFERREQUEST
_CREATETRANSFERREQUEST_DOWNLOADOPTIONS.containing_type = _CREATETRANSFERREQUEST
_CREATETRANSFERREQUEST.fields_by_name['direction'].enum_type = _TRANSFERDIRECTION
_CREATETRANSFERREQUEST.fields_by_name['downloadOptions'].message_type = _CREATETRANSFERREQUEST_DOWNLOADOPTIONS
_CREATETRANSFERREQUEST.fields_by_name['uploadOptions'].message_type = _CREATETRANSFERREQUEST_UPLOADOPTIONS
_LISTTRANSFERSRESPONSE.fields_by_name['transfer'].message_type = _TRANSFERINFO
_LISTREMOTEFILESRESPONSE.fields_by_name['filepaths'].message_type = _REMOTEFILE
DESCRIPTOR.message_types_by_name['RemoteFile'] = _REMOTEFILE
DESCRIPTOR.message_types_by_name['TransferInfo'] = _TRANSFERINFO
DESCRIPTOR.message_types_by_name['CreateTransferRequest'] = _CREATETRANSFERREQUEST
DESCRIPTOR.message_types_by_name['EditTransferRequest'] = _EDITTRANSFERREQUEST
DESCRIPTOR.message_types_by_name['ListTransfersResponse'] = _LISTTRANSFERSRESPONSE
DESCRIPTOR.message_types_by_name['ListRemoteFilesResponse'] = _LISTREMOTEFILESRESPONSE
DESCRIPTOR.enum_types_by_name['TransferDirection'] = _TRANSFERDIRECTION
DESCRIPTOR.enum_types_by_name['TransferState'] = _TRANSFERSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RemoteFile = _reflection.GeneratedProtocolMessageType('RemoteFile', (_message.Message,), dict(
  DESCRIPTOR = _REMOTEFILE,
  __module__ = 'yamcs.protobuf.cfdp.cfdp_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.cfdp.RemoteFile)
  ))
_sym_db.RegisterMessage(RemoteFile)

TransferInfo = _reflection.GeneratedProtocolMessageType('TransferInfo', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFERINFO,
  __module__ = 'yamcs.protobuf.cfdp.cfdp_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.cfdp.TransferInfo)
  ))
_sym_db.RegisterMessage(TransferInfo)

CreateTransferRequest = _reflection.GeneratedProtocolMessageType('CreateTransferRequest', (_message.Message,), dict(

  UploadOptions = _reflection.GeneratedProtocolMessageType('UploadOptions', (_message.Message,), dict(
    DESCRIPTOR = _CREATETRANSFERREQUEST_UPLOADOPTIONS,
    __module__ = 'yamcs.protobuf.cfdp.cfdp_pb2'
    # @@protoc_insertion_point(class_scope:yamcs.protobuf.cfdp.CreateTransferRequest.UploadOptions)
    ))
  ,

  DownloadOptions = _reflection.GeneratedProtocolMessageType('DownloadOptions', (_message.Message,), dict(
    DESCRIPTOR = _CREATETRANSFERREQUEST_DOWNLOADOPTIONS,
    __module__ = 'yamcs.protobuf.cfdp.cfdp_pb2'
    # @@protoc_insertion_point(class_scope:yamcs.protobuf.cfdp.CreateTransferRequest.DownloadOptions)
    ))
  ,
  DESCRIPTOR = _CREATETRANSFERREQUEST,
  __module__ = 'yamcs.protobuf.cfdp.cfdp_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.cfdp.CreateTransferRequest)
  ))
_sym_db.RegisterMessage(CreateTransferRequest)
_sym_db.RegisterMessage(CreateTransferRequest.UploadOptions)
_sym_db.RegisterMessage(CreateTransferRequest.DownloadOptions)

EditTransferRequest = _reflection.GeneratedProtocolMessageType('EditTransferRequest', (_message.Message,), dict(
  DESCRIPTOR = _EDITTRANSFERREQUEST,
  __module__ = 'yamcs.protobuf.cfdp.cfdp_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.cfdp.EditTransferRequest)
  ))
_sym_db.RegisterMessage(EditTransferRequest)

ListTransfersResponse = _reflection.GeneratedProtocolMessageType('ListTransfersResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTTRANSFERSRESPONSE,
  __module__ = 'yamcs.protobuf.cfdp.cfdp_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.cfdp.ListTransfersResponse)
  ))
_sym_db.RegisterMessage(ListTransfersResponse)

ListRemoteFilesResponse = _reflection.GeneratedProtocolMessageType('ListRemoteFilesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTREMOTEFILESRESPONSE,
  __module__ = 'yamcs.protobuf.cfdp.cfdp_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.cfdp.ListRemoteFilesResponse)
  ))
_sym_db.RegisterMessage(ListRemoteFilesResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
