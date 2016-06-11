# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.


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
