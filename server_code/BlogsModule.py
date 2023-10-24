import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def getLatestBlogs():
  blogSearch = app_tables.blogs.search()
  blogs = []
  i = 0
  for b in blogSearch:
    i = i + 1
    blogs.append({
      'author': {
        'editorsChoice':b['author']['editorsChoice'],
        'joined':b['author']['joined'],
        'name':b['author']['name'],
        'role': b['author']['role'],
        'username': b['author']['username']
      },
      'content': b['content'],
      'image': b['image'],
      'pub_date': b['pub_date'],
      'title': b['title']
    })
    print(i)
    return blogs;
