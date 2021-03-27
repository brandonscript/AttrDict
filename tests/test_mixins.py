"""
Tests for the AttrDefault class.
"""
from nose.tools import assert_equal, assert_raises


def test_invalid_attributes():
    """
    Tests how set/delattr handle invalid attributes.
    """
    from attrdict.mapping import AttrMap

    mapping = AttrMap()

    # mapping currently has allow_invalid_attributes set to False
    def assign():
        """
        Assign to an invalid attribute.
        """
        mapping._key = 'value'

    assert_raises(TypeError, assign)
    assert_raises(AttributeError, lambda: mapping._key)
    assert_equal(mapping, {})

    mapping._setattr('_allow_invalid_attributes', True)

    assign()
    assert_equal(mapping._key, 'value')
    assert_equal(mapping, {})

    # delete the attribute
    def delete():
        """
        Delete an invalid attribute.
        """
        del mapping._key

    delete()
    assert_raises(AttributeError, lambda: mapping._key)
    assert_equal(mapping, {})

    # now with disallowing invalid
    assign()
    mapping._setattr('_allow_invalid_attributes', False)

    assert_raises(TypeError, delete)
    assert_equal(mapping._key, 'value')
    assert_equal(mapping, {})

    # force delete
    mapping._delattr('_key')
    assert_raises(AttributeError, lambda: mapping._key)
    assert_equal(mapping, {})


def test_constructor():
    """
    _constructor MUST be implemented.
    """
    from attrdict.mixins import Attr

    class AttrImpl(Attr):
        """
        An implementation of attr that doesn't implement _constructor.
        """
        pass

    assert_raises(NotImplementedError, lambda: AttrImpl._constructor({}, ()))
