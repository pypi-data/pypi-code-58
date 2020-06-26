# -*- coding: utf-8 -*-

# Copyright (c) 2011-2020, Camptocamp SA
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# The views and conclusions contained in the software and documentation are those
# of the authors and should not be interpreted as representing official policies,
# either expressed or implied, of the FreeBSD Project.


import logging
from typing import Any, Dict, List, Optional, Union  # noqa

import sqlalchemy.ext.declarative
import sqlalchemy.ext.declarative.api
import sqlalchemy.orm  # noqa
import zope.event

try:
    from pyramid.i18n import TranslationStringFactory

    _ = TranslationStringFactory("c2cgeoportal_admin")
except ModuleNotFoundError:
    pass


# Should be filed on application initialisation
DBSession: sqlalchemy.orm.Session = None
Base: sqlalchemy.ext.declarative.api.ConcreteBase = sqlalchemy.ext.declarative.declarative_base()
DBSessions: Dict[str, sqlalchemy.orm.Session] = {}


LOG = logging.getLogger(__name__)


class InvalidateCacheEvent:
    pass


def cache_invalidate_cb(*args: List[Any]) -> None:
    _cache_invalidate_cb()


try:
    from c2cwsgiutils import broadcast

    @broadcast.decorator()
    def _cache_invalidate_cb() -> None:
        zope.event.notify(InvalidateCacheEvent())


except ModuleNotFoundError:
    LOG.error("c2cwsgiutils broadcast not found")
