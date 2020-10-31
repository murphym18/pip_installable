import pytest
import vechelpers as vh

def test_vec3d_1():
    a = 1
    b = 2
    c = 3
    v = vh.vec3d(a, b, c)
    assert pytest.approx(a, v[0])
    assert pytest.approx(b, v[1])
    assert pytest.approx(v, v[2])

def test_distance0():
    o = vh.vec3d(0, 0, 0)
    assert pytest.approx(0, vh.distance(o, o))

def test_distance1():
    o = vh.vec3d(0, 0, 0)
    r = vh.vec3d(3, 4, 0)
    assert pytest.approx(5, vh.distance(o, r))
    assert pytest.approx(5, vh.distance(r, o))

