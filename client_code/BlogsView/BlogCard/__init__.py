from ._anvil_designer import BlogCardTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ...BlogPage import BlogPage

class BlogCard(BlogCardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def open_blog_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('BlogPage', currentBlog=self.item)
    pass

