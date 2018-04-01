import pytest

@pytest.mark.usefixtures("libq")
class Safe:
  def __init__(self, libq, size):
    self.libq = libq
    self.ptr = libq.qua_array_create(size)

  def __del__(self):
    if self.ptr != None:
      self.libq.qua_array_destroy(self.ptr)

@pytest.fixture()
def qa(request, libq):
  return Safe(libq, request.param)

@pytest.mark.parametrize('size', [
  pytest.param(0, marks=pytest.mark.xfail(strict=True)),
  1,
  2,
  3,
  4
])
def test_qua_array_create(libq, size):
  assert libq.qua_array_create(size) != None

@pytest.mark.parametrize('qa, expected', [
  (0, 0),
  (1, 1),
  (2, 2),
  (3, 3),
  (4, 4),
], indirect=['qa'])
def test_qua_array_size(libq, qa, expected):
  assert libq.qua_array_size(qa.ptr) == expected

@pytest.mark.parametrize('qa, index, val, expected', [
  (0, 0, 12, None),
  (1, 0, 12, 12),
  (1, 1, 12, None)
], indirect=['qa'])
def test_qua_array_get(libq, qa, index, val, expected):
  libq.qua_array_set(qa.ptr, index, val)
  assert libq.qua_array_get(qa.ptr, index) == expected

@pytest.mark.parametrize('qa, index, val, expected', [
  (0, 0, 12, False),
  (1, 0, 12, True),
  (1, 1, 12, False)
], indirect=['qa'])
def test_qua_array_set(libq, qa, index, val, expected):
  assert libq.qua_array_set(qa.ptr, index, val) == expected

@pytest.mark.parametrize('qa, expected', [
  (0, False),
  (1, True),
  (2, True),
  (3, True),
  (4, True),
], indirect=['qa'])
def test_qua_array_destroy(libq, qa, expected):
  assert libq.qua_array_destroy(qa.ptr) == expected
  qa.ptr = None
