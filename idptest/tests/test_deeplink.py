# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
"""
Tests for the demo AttributeProcessor and IdP-initiated deep-linking.
"""
from . import base


class TestDeepLink(base.SamlTestCase):
    SP_CONFIG = {
        'acs_url': 'http://127.0.0.1:9000/sp/acs/',
        'processor': 'saml2idp.demo.Processor',
        'links': {
            'deeplink': 'http://127.0.0.1:9000/sp/%s/',
        }
    }
    DEEPLINK = 'http://127.0.0.1:8000/idp/init/deeplink/test/'
    EXPECTED_RELAY_STATE = 'http://127.0.0.1:9000/sp/test/'

    def test_deeplink(self):
        self._hit_saml_view(self.DEEPLINK)
        relaystate = self._html_soup.findAll('input', {'name': 'RelayState'})[0]
        self.assertEqual(self.EXPECTED_RELAY_STATE, relaystate['value'])


class TestDeepLinkWithAttributes(TestDeepLink):
    SP_CONFIG = {
        'acs_url': 'http://127.0.0.1:9000/sp/acs/',
        'processor': 'saml2idp.demo.AttributeProcessor',
        'links': {
            'attr': 'http://127.0.0.1:9000/sp/%s/',
        },
    }
    DEEPLINK = 'http://127.0.0.1:8000/idp/init/attr/test/'
    EXPECTED_RELAY_STATE = 'http://127.0.0.1:9000/sp/test/'

    def test_deeplink(self):
        super(TestDeepLinkWithAttributes, self).test_deeplink()
        attributes = self._saml_soup.find_all('saml:Attribute')

        # Assert.
        self.assertEqual(len(attributes), 1)
        self.assertEqual(attributes[0]['Name'], 'foo')
        value = attributes[0].findAll('saml:AttributeValue')[0]
        self.assertEqual(value.text, 'bar')
