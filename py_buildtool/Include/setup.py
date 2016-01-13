try:
    from setuptools import setup
    from setuptools import Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension
setup(name='helloworld', version='1.1.1',  \
      ext_modules=[Extension('helloworld', ['hello.c'])])