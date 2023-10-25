import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

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
  blogSearch = app_tables.blogs.client_readable().search(tables.order_by("pub_date", ascending=False))
  print(blogSearch)
  blogs = []
  i = 0
  for b in blogSearch:
    i = i+1
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

@anvil.server.callable
def isUserPublisher(email):
  results = app_tables.publishers.search(email=email)
  i = 0
  for result in results:
    i = i + 1
  return i == 1

def getPublisherForEmail(email):
  results = app_tables.publishers.search(email=email)
  for result in results:
    return result

@anvil.server.callable(require_user=True)
def addBlog(title, content, email, image):
  publisher = getPublisherForEmail(email)
  result = app_tables.blogs.add_row(author=publisher, content=content, title=title, image=image, pub_date=datetime.now().date())
  return result != None

@anvil.server.callable
def getBlogsForPublisher(username):
  author = app_tables.publishers.get(username=username)
  blogSearch = app_tables.blogs.client_readable().search(tables.order_by("pub_date", ascending=False), author=author)
  blogs = []
  for b in blogSearch:
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
  for b in blogSearch:
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
    return blogs;

@anvil.server.callable
def getAllBlogs():
  blogSearch = app_tables.blogs.client_readable().search(tables.order_by("pub_date", ascending=False))
  blogs = []
  for b in blogSearch:
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
  for b in blogSearch:
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
    return blogs;
