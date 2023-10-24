from ._anvil_designer import HomePageTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from .HomeBlogsFeed import HomeBlogsFeed
from .BlogsView import BlogsView
from .AboutView import AboutView

class HomePage(HomePageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel.clear()
    self.content_panel.add_component(HomeBlogsFeed())

    # Any code you write here will run when the form opens.

  def reset_links(self, **event_args):
    self.homeLink.role = ''
    self.blogsLink.role = ''
    self.aboutLink.role = ''

  def homeLink_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.reset_links()
    self.homeLink.role = 'selected'
    
    self.content_panel.clear()
    self.content_panel.add_component(HomeBlogsFeed())
    pass

  def blogsLink_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.reset_links()
    self.blogsLink.role = 'selected'
    
    self.content_panel.clear()
    self.content_panel.add_component(BlogsView())
    pass

  def aboutLink_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.reset_links()
    self.aboutLink.role = 'selected'
    
    self.content_panel.clear()
    self.content_panel.add_component(AboutView())
    pass

  def addBlogLink_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('AddBlogPage')
    pass






