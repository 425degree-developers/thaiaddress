"""thaiaddress: A python parser for Thai address"""

# PEP0440 compatible formatted version, see:
# https://www.python.org/dev/peps/pep-0440/
#
# Generic release markers:
#   X.Y
#   X.Y.Z   # For bugfix releases
#
# Admissible pre-release markers:
#   X.YaN   # Alpha release
#   X.YbN   # Beta release
#   X.YrcN  # Release Candidate
#   X.Y     # Final release
#
# Dev branch marker is: 'X.Y.devN' where N is an integer.
#

__version__ = "0.1.2"

from .parser import parse
from .utils import (
    preprocess,
    is_stopword,
    merge_tokens,
    merge_labels,
)
from .train import (
    train,
)
