# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2019 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""REST API for Citation Style Language styles."""

from __future__ import absolute_import, print_function

from citeproc_styles import __version__ as styles_version
from citeproc_styles import get_all_styles
from werkzeug.utils import cached_property

from .version import __version__ as rest_api_version


class _InvenioCSLRESTState(object):
    """State object."""

    def __init__(self, app):
        self.app = app

    @cached_property
    def styles(self):
        """Get a dictionary of CSL styles."""
        styles = get_all_styles()
        whitelist = self.app.config.get('CSL_STYLES_WHITELIST')
        if whitelist:
            return {k: v for k, v in styles.items() if k in whitelist}
        return styles

    @cached_property
    def content_version(self):
        """Get the version of the content of this extension.

        Note: The ETags of responses that are being produced by the REST API,
        are based on this string, since the `citeproc-py-styles` package, holds
        static files that are only updated whenever a new version is released.
        In combination with the package version, we get a unique identifier for
        the content that is being served.
        """
        return u":".join((rest_api_version, styles_version))


class InvenioCSLREST(object):
    """Invenio-CSL-REST extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self._state = self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        state = _InvenioCSLRESTState(app)
        app.extensions['invenio-csl-rest'] = state
        return state

    def __getattr__(self, name):
        """Proxy to state object."""
        return getattr(self._state, name, None)
