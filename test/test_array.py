import ctypes
import unittest

libq = ctypes.CDLL('build/src/libquasar.so')

libq.qua_array_create.restype = ctypes.c_void_p
libq.qua_array_get.restype = ctypes.c_void_p

class ArrayTest(unittest.TestCase):
  def setUp(self):
    self.qa = libq.qua_array_create(5)

  def tearDown(self):
    if self.qa != 0:
      libq.qua_array_destroy(self.qa)

  def test_qua_array_create(self):
    # size: 0 => NULL
    self.assertEqual(libq.qua_array_create(0), None)
    # size: >0 => valid
    self.assertNotEqual(libq.qua_array_create(1), None)

  def test_qua_array_size(self):
    # qa: NULL => 0
    self.assertEqual(libq.qua_array_size(None), 0)
    # qa: valid => !0
    self.assertEqual(libq.qua_array_size(self.qa), 5)

  def test_qua_array_get(self):
    # qa: NULL => NULL
    self.assertEqual(libq.qua_array_get(None, 0), None)
    # qa: valid, index: >size => NULL
    self.assertEqual(libq.qua_array_get(self.qa, 5), None)
    # qa: valid, index: valid => object
    libq.qua_array_set(self.qa, 0, 1337)
    self.assertEqual(libq.qua_array_get(self.qa, 0), 1337)

  def test_qua_array_set(self):
    # qa: NULL => false
    self.assertEqual(libq.qua_array_set(None, 0, None), False)
    # qa: valid, index: >size => false
    self.assertEqual(libq.qua_array_set(self.qa, 5, 111), False)
    # qa: valid, index: valid => true
    self.assertEqual(libq.qua_array_set(self.qa, 0, 222), True)
    self.assertEqual(libq.qua_array_set(self.qa, 1, 333), True)
    self.assertEqual(libq.qua_array_get(self.qa, 0), 222)
    self.assertEqual(libq.qua_array_get(self.qa, 1), 333)

  def test_qua_array_destroy(self):
    # qa: NULL => false
    self.assertEqual(libq.qua_array_destroy(None), False)
    # qa: valid => true
    self.assertEqual(libq.qua_array_destroy(self.qa), True)
    self.qa = None
