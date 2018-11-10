"""Central place for package metadata."""

from pkg_resources import DistributionNotFound, get_distribution

# NOTE: We use __title__ instead of simply __name__ since the latter would
#       interfere with a global variable __name__ denoting object's name.
__title__ = 'straining'
__summary__ = 'Application for cycling and running trainings'
__url__ = 'https://github.com/dblenkus/straining'

try:
    __version__ = get_distribution(__title__).version
except DistributionNotFound:
    # Package is not (yet) installed.
    pass

__author__ = 'Domen Blenkuš'
__email__ = 'domen@blenkus.com'

__license__ = 'Apache License (2.0)'
__copyright__ = '2018, ' + __author__

__all__ = (
    '__title__', '__summary__', '__url__', '__version__', '__author__',
    '__email__', '__license__', '__copyright__',
)
