import pytest

@pytest.mark.usefixtures("libq")
class Safe:
  def __init__(self, libq, init_cap):
    self.libq = libq
    self.ptr = libq.qua_vector_create(init_cap)

  def __del__(self):
    if self.ptr != None:
      self.libq.qua_vector_destroy(self.ptr)

@pytest.fixture()
def qv(request, libq):
  return Safe(libq, request.param)

@pytest.mark.parametrize('init_cap', [
  pytest.param(0, marks=pytest.mark.xfail(strict=True)),
  1,
  2,
  3,
  4
])
def test_qua_vector_create(libq, init_cap):
  assert libq.qua_vector_create(init_cap) != None

# @pytest.mark.parametrize('qv, expected', [
#   (0, 0),
#   (1, 0),
#   (2, 0),
#   (3, 0),
#   (4, 0),
# ], indirect=['qv'])
# def test_qua_vector_size(libq, qv, expected):
#   assert libq.qua_vector_size(qv.ptr) == expected
