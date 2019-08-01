# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2019 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


"""Module tests."""

from __future__ import absolute_import, print_function

from flask import Flask

from invenio_csl_rest import InvenioCSLREST


def test_version():
    """Test version import."""
    from invenio_csl_rest import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = InvenioCSLREST(app)
    assert 'invenio-csl-rest' in app.extensions

    app = Flask('testapp')
    ext = InvenioCSLREST()
    assert 'invenio-csl-rest' not in app.extensions
    ext.init_app(app)
    assert 'invenio-csl-rest' in app.extensions
