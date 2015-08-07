# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from setuptools import setup


with open('README.md') as readme:
    description = readme.read()


setup(
    name = 'dj-saml-idp',
    version = '0.19.0',
    author = 'Sebastian Vetter',
    author_email = 'sebastian@mobify.com',
    description = 'SAML 2.0 IdP for Django',
    long_description = description,
    install_requires = [
        'Django>=1.4',
        'M2Crypto>=0.20.1',
        'BeautifulSoup>=3.2.0'],
    license = 'MIT',
    packages = ['saml2idp', 'saml2idp.tests'],
    package_dir = {'saml2idp': 'idptest/saml2idp'},
    package_data = {'saml2idp': ['templates/saml2idp/*.html',
                                 'templates/saml2idp/*.xml']},
    url = 'http://github.com/mobify/dj-saml-idp',
    zip_safe = True,
)
