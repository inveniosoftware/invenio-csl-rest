# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2019 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""REST API for Citation Style Language styles."""

from __future__ import absolute_import, print_function

from flask import Blueprint, current_app, jsonify
from invenio_rest import ContentNegotiatedMethodView
from werkzeug.http import generate_etag
from werkzeug.local import LocalProxy

current_ext = LocalProxy(lambda: current_app.extensions['invenio-csl-rest'])

blueprint = Blueprint(
    'invenio_csl_rest',
    __name__,
    url_prefix='/csl',
    template_folder='templates',
    static_folder='static',
)


class StylesResource(ContentNegotiatedMethodView):
    """Resource for CSL styles.

    We're extending `ContentNegotiatedMethodView` only because we need some of
    its methods to check the ETag and the Last-Modified headers.

    Note: Currently this endpoint just returns the whole dict of styles,
    hoping that the client is utilizing cache mechanisms in order to avoid
    multiple transfers of the same data all the time.
    """

    def get(self, q=None, page=None):
        """Get styles."""
        # Check cache to exit early if needed
        etag = generate_etag(current_ext.content_version.encode('utf8'))
        self.check_etag(etag, weak=True)

        # Build response
        res = jsonify(current_ext.styles)
        res.set_etag(etag)

        return res

styles_view = StylesResource.as_view('styles')
blueprint.add_url_rule('/styles', view_func=styles_view)
