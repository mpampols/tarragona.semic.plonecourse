# Zope imports
from Acquisition import aq_inner
from zope.interface import Interface
from five import grok
from zope.component import getMultiAdapter

from plone.app.layout.viewlets.interfaces import IHtmlHead
from tarragona.semic.plonecourse.interfaces import IHeader, IContent

grok.context(Interface)

# Location of the templates
grok.templatedir('templates')

""" Viewlet Managers 
"""
class ViewletsHeader(grok.ViewletManager):
    grok.implements(IHeader)
    grok.context(Interface)
    grok.name("viewletsheader")


class ViewletsContent(grok.ViewletManager):
    grok.implements(IContent)
    grok.context(Interface)
    grok.name("viewletscontent")


""" Viewlets Managers 
"""
class NameOfTheViewlet(grok.Viewlet):
    grok.context(Interface)

    # Viewlet manager
    grok.viewletmanager(IHeader)
    
    # Name of the template that's using
    grok.template("nameoftheviewlet")
    
    # Order (!)
    grok.order(2)

    # Name of your product
    grok.name("collective.nameofyourproduct")

    # Require permissions if necessary
    grok.require("cmf.AddPortalContent")

    # Control when we want to render the viewlet, for example:
    def enabled(self):
        """ Viewlet will be enabled if...
        """
        return True

    def available(self):
        """ Viewlet will be available when...
        """
        return True
