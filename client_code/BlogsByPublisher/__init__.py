from ._anvil_designer import BlogsByPublisherTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class BlogsByPublisher(BlogsByPublisherTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    username = properties['username']
    self.usernameHeadline.text = "Blogs by " + username
    self.listView.items = anvil.server.call('getBlogsForPublisher', username)

    # Any code you write here will run before the form opens.
