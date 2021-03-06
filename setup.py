import sys
from distutils.core import setup, Extension


lirc_ext = Extension(
    'lirc',
    include_dirs=['/usr/include/lirc/'],
    libraries=['lirc_client'],
    library_dirs=['/usr/lib'],
    sources=['lirc/lirc.c']
)

setup(
    name='python-lirc',
    version='1.2.3',
    description='Python bindings for LIRC.',
    author='Thomas Preston',
    author_email='thomasmarkpreston@gmail.com',
    license='GPLv3+',
    url='https://github.com/tompreston/python-lirc',
    ext_modules=[lirc_ext],
    long_description=open('README.md').read() + open('CHANGELOG').read(),
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3 or "
        "later (AGPLv3+)",
        "Programming Language :: Cython",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='lirc cython remote ir infrared',
)
