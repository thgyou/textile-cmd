import sys
import distutils.core

long_description = """
Textile is a XHTML generator using a simple markup developed 
  by Dean Allen. See http://textile.thresholdstate.com/
pytextile is an implementation of Textile in Python. 
  See http://loopcore.com/python-textile/
This script wraps the pytextile library and provides direct usage
  from shell. See http://guido-leisker.de/Projects/Textile-cmd/
"""

distutils.core.setup( name = 'textile-cmd',
                      version = "0.1",
                      description = 'textile-cmd provides a wrapper for pytextile library',
                      long_description = long_description,
                      author = 'Guido Leisker',
                      author_email = 'guido@guido-leisker.de',
                      license = 'MIT',
                      platforms = 'all',
                      keywords = 'textile',
                      url = 'http://guido-leisker.de/Projects/Textile-cmd/',
                      scripts=['scripts/textile'],
                      package_dir = {'': '.'},
                      requires=['textile'],
                      )

