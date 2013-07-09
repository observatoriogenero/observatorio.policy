# -*- coding: utf-8 -*-
"""Installer for the observatorio.policy package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = \
    read('README.rst') + \
    read('docs', 'CHANGELOG.rst') + \
    read('docs', 'LICENSE.rst')

setup(
    name='observatorio.policy',
    version='0.1',
    description="",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='',
    author='Gustavo Lepri.',
    author_email='gustavolepri@gmail.com',
    url='http://pypi.python.org/pypi/observatorio.policy',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['observatorio'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
         'five.grok',
         'five.pt',
         'Pillow',
         'Plone',
         'setuptools',
         'brasil.gov.barra',
         'brasil.gov.vcge',
         'collective.portlet.banners',
         'collective.galleria',
         'collective.oembed',
         'collective.embedly',
         'collective.cover',
         'eea.daviz',
         'Products.EasyNewsletter[all]',
         'collective.watcherlist',
         'Solgema.fullcalendar',
         'collective.azindexpage',
         'eea.facetednavigation',
         'collective.linguafaq',
         'collective.newsticker',
         'collective.portlet.feedmixer',
         'raptus.autocompletewidget',
         'collective.portlet.relateditems',
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
         'Products.PloneBoard',
         'observatorio.conteudo',
         'observatorio.tema',
         'quintagroup.seoptimizer>=4.0',
         'jyu.rsslisting',
    ],
    extras_require={
        'test': [
            'mock',
            'plone.app.testing',
            'unittest2',
        ],
        'develop': [
            'flake8',
            'jarn.mkrelease',
            'niteoweb.loginas',
            'plone.app.debugtoolbar',
            'plone.reload',
            'Products.Clouseau',
            'Products.DocFinderTab',
            'Products.PDBDebugMode',
            'Products.PrintingMailHost',
            'Sphinx',
            'zest.releaser',
            'zptlint',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
