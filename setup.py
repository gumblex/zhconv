import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='zhconv',
    version='1.1.0',
    description="A simple implementation of Chinese S-T conversion.",
    author='Dingyuan Wang',
    author_email='abcdoyle888@gmail.com',
    py_modules=['zhconv'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    url='https://github.com/gumblex/zhconv',
    data_files=[('', ['zhcdict.json'])]
)
