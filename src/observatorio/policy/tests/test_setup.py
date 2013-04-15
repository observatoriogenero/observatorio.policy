# -*- coding: utf-8 -*-

import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from observatorio.policy.config import PROJECTNAME
from observatorio.policy.testing import INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID


DEPENDENCIAS = ['brasil.gov.barra',
         'brasil.gov.vcge',
         'collective.portlet.banners',
         'collective.galleria',
         'collective.oembed',
         'collective.embedly',
         'collective.cover',
         'eea.daviz',
         'Products.EasyNewsletter',
         'collective.watcherlist',
         'Solgema.fullcalendar',
         'collective.azindexpage',
         'eea.facetednavigation',
         'collective.linguafaq',
         'collective.pdfpeek',
         'collective.newsticker',
         'collective.portlet.feedmixer',
         'raptus.autocompletewidget',
         'collective.portlet.keywordmatches',
         'collective.googleanalytics',
         'sc.contentrules.groupbydate',
         'collective.contentgovernance',
         'collective.twitter.action',
         'collective.quickupload',
         'collective.simplesocial',
         'collective.twitter.portlets',
         'collective.wasthisuseful',
         'collective.polls',
         'Products.PloneFormGen',
         'Products.PloneBoard',]

class TestInstall(unittest.TestCase):
    """Test installation of observatorio.policy into Plone."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi = getToolByName(self.portal, 'portal_quickinstaller')

    def test_installed(self):
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME))

    def test_dependencies_installed(self):
        for dependencia in DEPENDENCIAS:
            self.assertTrue(self.qi.isProductInstalled(dependencia))

#    # browserlayer.xml
#    def test_browserlayer(self):
#        """Test that IObservatorioPolicyLayer is registered."""
#        from observatorio.policy.interfaces import IObservatorioPolicyLayer
#        from plone.browserlayer import utils
#        self.failUnless(IObservatorioPolicyLayer in utils.registered_layers())


class UninstallTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))
