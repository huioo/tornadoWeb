#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib


if type('') is not type(b''):
    bytes_type = bytes
    unicode_type = str
    basestring_type = str
else:
    bytes_type = str
    unicode_type = unicode
    basestring_type = basestring


_UTF8_TYPES = (bytes_type, type(None))
_TO_UNICODE_TYPES = (unicode_type, type(None))


def utf8(text):
    """
        Converts a string argument to a byte string.

        If the argument is already a byte string or None, it is returned unchanged.
        Otherwise it must be a unicode string and is encoded as utf8.
    """
    if isinstance(text, _UTF8_TYPES):
        return text
    assert isinstance(text, unicode_type), \
        "Expected bytes, unicode, or None; got %r" % type(text)
    return text.encode("utf-8")


def to_unicode(text):
    """
        Converts a string argument to a unicode string.

        If the argument is already a unicode string or None, it is returned
        unchanged.  Otherwise it must be a byte string and is decoded as utf8.
    """
    if isinstance(text, _TO_UNICODE_TYPES):
        return text
    assert isinstance(text, bytes_type), \
        "Expected bytes, unicode, or None; got %r" % type(text)
    return text.decode("utf-8", 'ignore')

