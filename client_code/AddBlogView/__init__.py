from ._anvil_designer import AddBlogViewTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class AddBlogView(AddBlogViewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Submit the data to server for adding the blog
    confirmed = confirm("This action is irreversible!", title="Are you sure you want to publish this blog?")
    if not confirmed:
      return
    email = anvil.users.get_user()['email']
    title = self.titleField.text
    content = self.contentBox.text
    image = self.blogImageUploader.file
    success = anvil.server.call('addBlog', title, content, email, image)
    Notification("Added the new blog successfully!" if success else "Failed to add new blog!").show()
    pass

  def titleField_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    self.contentBox.focus()
    pass


