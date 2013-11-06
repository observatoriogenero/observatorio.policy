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
         'Plone>=4.3.1',
         'setuptools',
         'brasil.gov.barra',
         'brasil.gov.vcge',
         'collective.azindexpage==1.0.3',
         'collective.galleria==1.2.3',
         'collective.oembed==1.2.5',
         'collective.embedly==2.1',
         'collective.cover==1.0a5',
         'eea.daviz==7.7',
         'eea.depiction==5.2',
         'Products.EasyNewsletter[all]==2.6.11',
         'Solgema.fullcalendar==2.3',
         'collective.azindexpage==1.0.3',
         'eea.facetednavigation==6.1',
         'collective.linguafaq==0.5',
         'collective.newsticker',
         'raptus.autocompletewidget==0.1',
         'collective.portlet.relateditems==0.3.10',
         'collective.googleanalytics==1.4.3',
         'sc.contentrules.groupbydate==2.0',
         'collective.contentgovernance==1.1',
         'collective.twitter.action==1.0.1',
         'collective.quickupload==1.6.0',
         'collective.simplesocial==1.7',
         'collective.twitter.portlets==1.0b5',
         'collective.wasthisuseful',
         'collective.polls==1.4',
         'collective.linguafaq==0.5',
         'collective.newsticker',
         'collective.portlet.relateditems==0.3.10',
         'collective.googleanalytics==1.4.3',
         'sc.contentrules.groupbydate==2.0',
         'Products.PloneFormGen==1.7.12',
         'Products.PloneBoard==3.4',
         'observatorio.conteudo',
         'observatorio.tema',
         'quintagroup.seoptimizer>=4.0',
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
