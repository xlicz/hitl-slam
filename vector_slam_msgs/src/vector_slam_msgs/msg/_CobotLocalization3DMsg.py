"""autogenerated by genpy from vector_slam_msgs/CobotLocalization3DMsg.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class CobotLocalization3DMsg(genpy.Message):
  _md5sum = "25565b272405f868405eb6f47a0058f7"
  _type = "vector_slam_msgs/CobotLocalization3DMsg"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float64 timeStamp
float32 x
float32 y
float32 z
float32 angle_w
float32 angle_x
float32 angle_y
float32 angle_z
float32 conf
string map

"""
  __slots__ = ['timeStamp','x','y','z','angle_w','angle_x','angle_y','angle_z','conf','map']
  _slot_types = ['float64','float32','float32','float32','float32','float32','float32','float32','float32','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       timeStamp,x,y,z,angle_w,angle_x,angle_y,angle_z,conf,map

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CobotLocalization3DMsg, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.timeStamp is None:
        self.timeStamp = 0.
      if self.x is None:
        self.x = 0.
      if self.y is None:
        self.y = 0.
      if self.z is None:
        self.z = 0.
      if self.angle_w is None:
        self.angle_w = 0.
      if self.angle_x is None:
        self.angle_x = 0.
      if self.angle_y is None:
        self.angle_y = 0.
      if self.angle_z is None:
        self.angle_z = 0.
      if self.conf is None:
        self.conf = 0.
      if self.map is None:
        self.map = ''
    else:
      self.timeStamp = 0.
      self.x = 0.
      self.y = 0.
      self.z = 0.
      self.angle_w = 0.
      self.angle_x = 0.
      self.angle_y = 0.
      self.angle_z = 0.
      self.conf = 0.
      self.map = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_d8f.pack(_x.timeStamp, _x.x, _x.y, _x.z, _x.angle_w, _x.angle_x, _x.angle_y, _x.angle_z, _x.conf))
      _x = self.map
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 40
      (_x.timeStamp, _x.x, _x.y, _x.z, _x.angle_w, _x.angle_x, _x.angle_y, _x.angle_z, _x.conf,) = _struct_d8f.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.map = str[start:end].decode('utf-8')
      else:
        self.map = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_d8f.pack(_x.timeStamp, _x.x, _x.y, _x.z, _x.angle_w, _x.angle_x, _x.angle_y, _x.angle_z, _x.conf))
      _x = self.map
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 40
      (_x.timeStamp, _x.x, _x.y, _x.z, _x.angle_w, _x.angle_x, _x.angle_y, _x.angle_z, _x.conf,) = _struct_d8f.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.map = str[start:end].decode('utf-8')
      else:
        self.map = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_d8f = struct.Struct("<d8f")
