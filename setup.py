import sys

from os.path import os
import re


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


pkg_file = os.path.join(os.path.split(__file__)[0], "src", "email_parser", "__init__.py")

m = re.search(r"__version__\s*=\s*\"([\d.]+)\"", open(pkg_file).read())
if not m:
    print("Cannot find version of package", file=sys.stderr)
    sys.exit(1)

version = m.group(1)


setup(
    name="analisa monitor",
    version=version,
    description="""A tool to automatically monitor analisa \
          whether it has stop running or not""",
    url="",
    package_dir={"": "src", "utils": "src/analisa_monitor/utils"},
    packages=["analisa_monitor", "analisa_monitor.utils"],
    scripts=["src/run.py"],
    author="David Boateng Adams",
    author_email="david.adams@petratrust.com",
    license="GPL v3",
    provides=["analisa_monitor", "analisa_monitor.utils"],
    keywords=["email", "IMAP", "attachment"],
    classifiers=[
        "Development Status :: 1 - Beta",
        "Environment :: Console",
        """License :: OSI Approved \
                       :: GNU General Public License v3 (GPLv3)""",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.7",
        "Topic :: Communications :: Email",
    ],
)
