from ._anvil_designer import HomeBlogsFeedTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class HomeBlogsFeed(HomeBlogsFeedTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    blogs = anvil.server.call('getLatestBlogs')
    self.latest_blogs_panel.items = blogs
    # Any code you write here will run before the form opens.
