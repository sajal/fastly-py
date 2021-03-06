import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "fastly",
    version = "0.0.1",
    author = "Fastly?",
    author_email="support@fastly.com",
    description = ("Fastly python API"),
    license = "dunno",
    keywords = "fastly api",
    url = "https://github.com/fastly/fastly-py",
    packages=['fastly', 'test'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved??? :: BSD License???",
    ],
)