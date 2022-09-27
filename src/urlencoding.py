import ctypes, platform

if platform.system() == "Linux":
  _lib = ctypes.CDLL("liburlencoding.so")
elif platform.system() == "Windows":
  _lib = ctypes.CDLL("liburlencoding.dll")
elif platform.system() == "Darwin":
  _lib = ctypes.CDLL("liburlencoding.dylib")
else:
  _lib = ctypes.CDLL("liburlencoding")

_lib.url_encoding_encode.argtypes = [ctypes.c_char_p]

_lib.url_encoding_encode.restype = ctypes.c_void_p

_lib.url_encoding_encode_binary.argtypes = [ctypes.c_char_p, ctypes.c_size_t]

_lib.url_encoding_encode_binary.restype = ctypes.c_void_p

_lib.url_encoding_decode.argtypes = [ctypes.c_char_p]

_lib.url_encoding_decode.restype = ctypes.c_void_p

_lib.url_encoding_decode_binary.argtypes = [ctypes.c_char_p, ctypes.c_size_t]

_lib.url_encoding_decode_binary.restype = ctypes.c_void_p

_lib.url_encoding_free.argtypes = [ctypes.c_void_p]

_lib.url_encoding_free.restype = None

def encode(data):
  res = _lib.url_encoding_encode(data.encode("utf-8"))
  if not res:
    return ""
  str = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8")
  _lib.url_encoding_free(res)
  return str

def encode_binary(data):
  res = _lib.url_encoding_encode_binary(data.encode("utf-8"), len(data))
  if not res:
    return ""
  str = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8")
  _lib.url_encoding_free(res)
  return str

def decode(data):
  res = _lib.url_encoding_decode(data.encode("utf-8"))
  if not res:
    return ""
  str = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8")
  _lib.url_encoding_free(res)
  return str

def decode_binary(data):
  res = _lib.url_encoding_decode_binary(data.encode("utf-8"), len(data))
  if not res:
    return ""
  str = ctypes.cast(res, ctypes.c_char_p).value.decode("utf-8")
  _lib.url_encoding_free(res)
  return str