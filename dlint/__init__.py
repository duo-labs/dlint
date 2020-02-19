from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from . import linters  # noqa F401
from . import multi  # noqa F401
from . import namespace  # noqa F401
from . import redos  # noqa F401
from . import test  # noqa F401
from . import tree  # noqa F401
from . import util  # noqa F401

__name__ = 'dlint'
__version__ = '0.10.2'
__description__ = (
    "Dlint is a tool for encouraging best coding practices "
    "and helping ensure Python code is secure."
)
__url__ = 'https://github.com/dlint-py/dlint'
__license__ = 'BSD-3-Clause'
