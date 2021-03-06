from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

NAME = 'lormsq'
VERSION = '0.0.6'
DESCRIPTION = 'SQL ORM'
LONG_DESCRIPTION = 'SQL ORM'
VENDOR = 'alive2212'
AUTHOR_NAME = 'Babak'
AUTHOR_FAMILY = 'Nodoust'
AUTHOR_EMAIL = 'alive2212@gmail.com'

# Setting up
setup(
    name=NAME,
    version=VERSION,
    author="""{} ({} {})""".format(VENDOR, AUTHOR_NAME, AUTHOR_FAMILY),
    author_email="""<{}>""".format(AUTHOR_EMAIL),
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
