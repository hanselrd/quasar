import ctypes
import pytest

@pytest.fixture
def libq(scope="module"):
  libq = ctypes.CDLL("build/src/libquasar.so")
  libq.qua_array_create.restype = ctypes.c_void_p
  libq.qua_array_get.restype = ctypes.c_void_p
  return libq
