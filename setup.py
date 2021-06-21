# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='transposon_classifier_rfsb',
    version='0.1.0',
    description='Interacting with gentli from python',
    long_description=open(path.join(here, "README.md")).read(),
    long_description_content_type="text/markdown",
    url='https://github.com/iliasbukraa/transposon_classifier_rfsb',
    author='Ilias Bukraa',
    author_email='',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='database',
    packages=find_packages(),
    python_requires='>=3',
    install_requires=[],
    package_data={'transposon_classifier_rfsb': []},
    package_dir={'transposon_classifier_rfsb': 'transposon_classifier_rfsb'},
    include_package_data=True,
)
