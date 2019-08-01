# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2019 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
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
