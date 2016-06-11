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
"""Views tests."""

import json

from flask import url_for


def test_styles_get(app, csl_styles):
    """Test get styles."""
    with app.test_client() as client:
        res = client.get(url_for('invenio_csl_rest.styles'))
        data = json.loads(res.get_data(as_text=True))

        assert res.status_code == 200

        assert 'apa' in data
        assert 'American Psychological Association' in data['apa']
        assert 'nature' in data
        assert 'Nature' in data['nature']
        assert 'science' in data
        assert 'Science Magazine' in data['science']


def test_whitelist(app, csl_styles):
    """Test styles whitelist."""
    app.config.update(CSL_STYLES_WHITELIST=['apa'])
    with app.test_client() as client:
        res = client.get(url_for('invenio_csl_rest.styles'))
        data = json.loads(res.get_data(as_text=True))

        assert 'apa' in data
        assert 'American Psychological Association' in data['apa']
        assert 'nature' not in data
        assert 'science' not in data


def test_http_caching(app, csl_styles):
    """Test styles whitelist."""
    with app.test_client() as client:
        res = client.get(url_for('invenio_csl_rest.styles'))
        etag = res.headers['Etag']

        res = client.get(url_for('invenio_csl_rest.styles'),
                         headers={'If-None-Match': etag})
        assert res.status_code == 304
