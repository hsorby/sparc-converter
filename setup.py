import io
import os
import re

from setuptools import setup, find_namespace_packages


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'src', 'sparc', 'convert', '__init__.py')) as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')


def readfile(filename, split=False):
    with io.open(filename, encoding="utf-8") as stream:
        if split:
            return stream.read().split("\n")
        return stream.read()


readme = readfile("README.rst", split=True)
readme.append('License')
readme.append('=======')
readme.append('')
readme.append('::')
readme.append('')

software_licence = readfile("LICENSE")


requires = ['cmlibs.exporter >= 0.2.1']

setup(
    name='sparc-converter',
    version=version,
    description='Applications to convert SPARC data.',
    long_description='\n'.join(readme) + software_licence,
    long_description_content_type='text/x-rst',
    classifiers=[],
    author='Hugh Sorby',
    author_email='h.sorby@auckland.ac.nz',
    url='https://github.com/hsorby/sparc-converter.git',
    license='Apache Software License',
    license_files=("LICENSE",),
    packages=find_namespace_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "sparc-convert = sparc.convert.application:main",
        ]
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)
