#!/usr/bin/env python
#coding=utf-8

import sys
sys.path.append('./src')
from distutils.core import setup
from baidupan import __version__
setup(name='baidupan',
      version=__version__,
      description='A baidu netdisk api sdk',
      long_description=open('README.md').read(),
      author='solos',
      author_email='solos@solos.so',
      packages=['baidupan'],
      package_dir={'baidupan': 'src/baidupan'},
      package_data={'baidupan': ['stuff']},
      license='BSD',
      platforms=['any'],
      url='https://github.com/solos/baidupan')
