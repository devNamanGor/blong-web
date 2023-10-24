from ._anvil_designer import AddBlogPageTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from .AddBlogView import AddBlogView

class AddBlogPage(AddBlogPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user = anvil.users.get_user()
    if (user == None):
      self.content_panel.clear()
      label = Label()
      label.text = "Please login to add blogs!"
      loginBtn = Button()
      loginBtn.add_event_handler('click', self.onLoginClicked)
      loginBtn.text = 'Login/Sign Up'
      self.content_panel.add_component(label)
      self.content_panel.add_component(loginBtn)
      return
    email = user['email']
    isUserPublisher = anvil.server.call('isUserPublisher', email)
    logoutButton = Button()
    logoutButton.role = 'primary'
    logoutButton.icon = 'fa:sign-out'
    logoutButton.add_event_handler('click', self.onLogoutClicked)
    self.navbar_links.add_component(logoutButton)
    if isUserPublisher:
      self.content_panel.clear()
      self.content_panel.add_component(AddBlogView())
    else:
      self.content_panel.clear()
      label = Label()
      label.text = "You are not a publisher on our website, hence you cannot add new blogs.!"
      self.content_panel.add_component(label)
      
  def onLoginClicked(self, **event_args):
    open_form('LoginForm')
    # Any code you write here will run when the form opens.

  def onLogoutClicked(self, **event_args):
    anvil.users.logout()

  def homeButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('HomePage')
    pass

