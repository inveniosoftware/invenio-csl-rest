# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2019 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""REST API for Citation Style Language styles."""

from __future__ import absolute_import, print_function

from .ext import InvenioCSLREST
from .version import __version__

__all__ = ('__version__', 'InvenioCSLREST')
