# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2019 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


"""Pytest configuration."""

from __future__ import absolute_import, print_function

import pytest
from flask import Flask

from invenio_csl_rest import InvenioCSLREST
from invenio_csl_rest.views import blueprint


@pytest.yield_fixture()
def app():
    """Flask application fixture."""
    app = Flask('testapp')
    app.config.update(
        SERVER_NAME='localhost',
        TESTING=True
    )
    ext = InvenioCSLREST(app)
    app.register_blueprint(blueprint)

    assert ext.content_version

    with app.app_context():
        yield app


@pytest.fixture()
def csl_styles(monkeypatch):
    """CSL styles fixture."""
    def sample_styles():
        styles = {
            'apa': 'American Psychological Association',
            'nature': 'Nature',
            'science': 'Science Magazine'
        }
        return styles
    monkeypatch.setattr('invenio_csl_rest.ext.get_all_styles', sample_styles)
