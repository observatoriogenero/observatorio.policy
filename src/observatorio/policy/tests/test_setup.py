# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from observatorio.policy.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of observatorio.policy into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if observatorio.policy is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('observatorio.policy'))

    def test_uninstall(self):
        """Test if observatorio.policy is cleanly uninstalled."""
        self.installer.uninstallProducts(['observatorio.policy'])
        self.assertFalse(self.installer.isProductInstalled('observatorio.policy'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IObservatorioPolicyLayer is registered."""
        from observatorio.policy.interfaces import IObservatorioPolicyLayer
        from plone.browserlayer import utils
        self.failUnless(IObservatorioPolicyLayer in utils.registered_layers())
