"""
Tests for the AttrDefault class.
"""
from nose.tools import assert_equal, assert_raises
from six import PY2


def test_method_missing():
    """
    default values for AttrDefault
    """
    from attrdict.default import AttrDefault

    default_none = AttrDefault()
    default_list = AttrDefault(list, sequence_type=None)
    default_double = AttrDefault(lambda value: value * 2, pass_key=True)

    assert_raises(AttributeError, lambda: default_none.foo)
    assert_raises(KeyError, lambda: default_none['foo'])
    assert_equal(default_none, {})

    assert_equal(default_list.foo, [])
    assert_equal(default_list['bar'], [])
    assert_equal(default_list, {'foo': [], 'bar': []})

    assert_equal(default_double.foo, 'foofoo')
    assert_equal(default_double['bar'], 'barbar')
    assert_equal(default_double, {'foo': 'foofoo', 'bar': 'barbar'})


def test_repr():
    """
    repr(AttrDefault)
    """
    from attrdict.default import AttrDefault

    assert_equal(repr(AttrDefault(None)), "AttrDefault(None, False, {})")

    # list's repr changes between python 2 and python 3
    type_or_class = 'type' if PY2 else 'class'

    assert_equal(
        repr(AttrDefault(list)),
        type_or_class.join(("AttrDefault(<", " 'list'>, False, {})"))
    )

    assert_equal(
        repr(AttrDefault(list, {'foo': 'bar'}, pass_key=True)),
        type_or_class.join(
            ("AttrDefault(<", " 'list'>, True, {'foo': 'bar'})")
        )
    )
