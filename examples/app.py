# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2019 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


"""Minimal Flask application example for development.

Run example development server:

.. code-block:: console

   $ cd examples
   $ flask -a app.py --debug run

Open your browser at 'http://localhost:5000/csl/styles', and you should get a
JSON object containing all the available CSL Styles.
"""

from __future__ import absolute_import, print_function

from flask import Flask

from invenio_csl_rest import InvenioCSLREST

# Create Flask application
app = Flask(__name__)
InvenioCSLREST(app)
