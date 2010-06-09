#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2007-2008 Nathanael C. Fritz
# All Rights Reserved
#
# This software is licensed as described in the README file,
# which you should have received as part of this distribution.
#

try:
    import setuptools
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

from setuptools import setup, find_packages, Extension, Feature

VERSION          = '100609r1'
DESCRIPTION      = 'SleekXMPP is an elegant Python library for XMPP (aka Jabber, Google Talk, etc).'
LONG_DESCRIPTION = """
SleekXMPP is an elegant Python library for XMPP (aka Jabber, Google Talk, etc).
"""

CLASSIFIERS      = [ 'Intended Audience :: Developers',
                     'License :: OSI Approved :: MIT',
                     'Programming Language :: Python',
                     'Topic :: Software Development :: Libraries :: Python Modules',
                   ]

setup(
    name             = "sleekxmpp",
    version          = VERSION,
    description      = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    author       = 'Nathanael Fritz',
    author_email = 'fritzy [at] netflint.net',
    url          = 'http://code.google.com/p/sleekxmpp',
    license      = 'MIT',
    platforms    = [ 'any' ],
    packages     = find_packages(),
    requires     = [ 'tlslite', 'pythondns' ],
    )

