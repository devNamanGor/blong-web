from ._anvil_designer import BlogPageTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..BlogsByPublisher import BlogsByPublisher

class BlogPage(BlogPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.item = properties['currentBlog']

    # Any code you write here will run before the form opens.

  def homeLink_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('HomePage')
    pass

  def blogAuthor_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('BlogsByPublisher', username=self.item['author']['username'])
    pass


