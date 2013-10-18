from zope.interface import implements

from Products.CMFQuickInstallerTool.interfaces import INonInstallable


class HiddenProducts(object):
    implements(INonInstallable)

    def getNonInstallableProducts(self):
        return ['brasil.gov.barra',
                'brasil.gov.vcge',
                'collective.azindexpage',
                'collective.galleria',
                'collective.oembed',
                'collective.embedly',
                'collective.cover',
                'collective.contentgovernance',
                'collective.twitter.action',
                'collective.quickupload',
                'collective.simplesocial',
                'collective.twitter.portlets',
                'collective.wasthisuseful',
                'collective.polls',
                'collective.linguafaq',
                'collective.newsticker',
                'collective.portlet.relateditems',
                'collective.googleanalytics',
                'eea.daviz',
                'Products.EasyNewsletter',
                'collective.watcherlist',
                'Solgema.fullcalendar',
                'Solgema.ContextualContentMenu',
                'eea.facetednavigation',
                'raptus.autocompletewidget',
                'sc.contentrules.groupbydate',
                'Products.PloneFormGen',
                'Products.Ploneboard',
                'Products.DataGridField',
                'observatorio.conteudo',
                'observatorio.tema',
                'quintagroup.seoptimizer',
                'plone.app.tiles',
                'archetypes.linguakeywordwidget',
                'collective.configviews',
                'collective.js.galleria',
                'collective.gallery',
                'collective.twitter.accounts',
                'inqbus.plone.fastmemberproperties',
                'eea.jquery',
                'eea.exhibit',
                'eea.forms',
                'eea.googlecharts',
                'eea.sparql',
                'eea.versions',
                'eea.app.visualization',
                'Products.SimpleAttachment',
                'plone.formwidget.autocomplete',
                'plone.app.blocks',
                'plone.formwidget.contenttree',
                'plone.app.relationfield',
                'collective.js.colorpicker',
                'collective.js.fullcalendar',
                ]