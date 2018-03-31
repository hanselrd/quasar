import ctypes
import unittest

class ArrayTest(unittest.TestCase):
  def setUp(self):
    self.libq = ctypes.CDLL('build/src/libquasar.so')
    self.qa = 0

  def tearDown(self):
    if self.qa != 0:
      self.libq.qua_array_destroy(self.qa)

  def test_qua_array_create_zero(self):
    self.assertEqual(self.libq.qua_array_create(0), 0)

  def test_qua_array_create_nonzero(self):
    self.qa = self.libq.qua_array_create(1)
    self.assertNotEqual(self.qa, 0)

  def test_qua_array_size_null(self):
    self.qa = self.libq.qua_array_create(2)
    self.assertEqual(self.libq.qua_array_size(self.qa), 2)
