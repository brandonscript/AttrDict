"""
Tests for the AttrMap class.
"""
from nose.tools import assert_equal


def test_repr():
    """
    repr(AttrMap)
    """
    from attrdict.mapping import AttrMap

    assert_equal(repr(AttrMap()), "AttrMap({})")
    assert_equal(repr(AttrMap({'foo': 'bar'})), "AttrMap({'foo': 'bar'})")
    assert_equal(
        repr(AttrMap({1: {'foo': 'bar'}})), "AttrMap({1: {'foo': 'bar'}})"
    )
    assert_equal(
        repr(AttrMap({1: AttrMap({'foo': 'bar'})})),
        "AttrMap({1: AttrMap({'foo': 'bar'})})"
    )
