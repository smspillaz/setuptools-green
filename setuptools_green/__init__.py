# /setuptools_green/__init__.py
#
# Provides a setuptools command for running tests using the "green"
# test runner.
#
# See /LICENCE.md for Copyright information
"""Provide a setuptools command for running tests with green."""

import sys

from distutils.errors import DistutilsArgError

import setuptools


class GreenTestCommand(setuptools.Command):

    """Provide a test command using green."""

    def __init__(self, *args, **kwargs):
        """Initialize instance variables."""
        setuptools.Command.__init__(self, *args, **kwargs)
        self.quiet = False
        self.target = None

    def run(self):   # suppress(unused-function)
        """Run tests using green."""
        import green.cmdline
        import green.config

        green.config.sys.argv = ["", "-t"]

        if self.target:
            green.config.sys.argv.append(self.target)

        if not self.quiet:
            green.config.sys.argv.append("-vvv")

        sys.exit(green.cmdline.main())

    def initialize_options(self):  # suppress(unused-function)
        """Set all options to their initial values."""
        self.quiet = False
        self.target = None

    def finalize_options(self):  # suppress(unused-function)
        """Finalize options."""
        if not isinstance(self.quiet, bool):
            raise DistutilsArgError("""--quiet takes no additional """
                                    """arguments.""")

        if not (isinstance(self.target, str) or self.target is None):
            raise DistutilsArgError("""--target=TARGET: TARGET must be a """
                                    """string.""")

    user_options = [  # suppress(unused-variable)
        ("quiet", None, "Don't show test descriptions when running"),
        ("target=", None, "Name of subdirectory where tests are to be found")
    ]
    # suppress(unused-variable)
    description = "run tests using the 'green' test runner"
