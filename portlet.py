from zope import schema
from zope.formlib import form
from zope.interface import implements
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName


class ITarragonaPortlet(IPortletDataProvider):
    """ Tarragona portlet with a simple title
    """
    label = schema.TextLine(
        title=_(u"Porlet title"),
        description=_(u"Title of the portlet."),
        required=True
    )


class Assignment(base.Assignment):
    """ Assignment
    """
    implements(ITarragonaPortlet)

    @property
    def title(self):
        """ Get portlet title
        """
        return self.label


class AddForm(base.AddForm):
    """ Add Tarragona portlet
    """
    form_fields = form_fields.Fields(ITarragonaPortlet)
    label = _(u"Add Tarragona portlet")
    description = _(u"This portlet does something cool")

    def create(self, data):
        """ Create Tarragona portlet
            That's what to do just after the portlet creation
        """
        return Assignment()


class EditForm(base.EditForm):
    """ Portlet edit
    """
    form_fields = form.Fields(ITarragonaPortlet)
    label = _(u"Edit Tarragona portlet")
    description = _(u"This portlet does something cool")


class Renderer(base.Renderer):
    """ Tarragona portlet renderer
    """
    render = ViewPageTemplateFile('templates/portlet.pt')

    @property
    def available(self):
        """ When this portlet should be available (can be any kind of condition)
            for example, when user has some permission.
        """
        return True