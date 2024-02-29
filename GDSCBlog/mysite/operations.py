import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GDSCBlog.settings")
django.setup()

from BlogApp.models import Post
from .CommentApp.models import Comment

def _create():
    First_post = Post.objects.create(title='First Post', content='The first Content', category='First category')
    Second_post = Post.objects.create(title='Second Post', content='The Second Content', category='Second category')
    Third_post = Post.objects.create(title='Third Post', content='The Third Content', category='Third category')

def _filter():
    category_Second_posts = Post.objects.filter(category='Second category')
    for post in category_Second_posts:
        print(f"Title {post.title}, Content {post.content}, Category {post.category}")

def _update():
    updated_post = Post.objects.get(title="First Post")
    updated_post.content = "New Content"
    updated_post.save()

def _delete():
    deleted_post = Post.objects.get(title="Third Post")
    deleted_post.delete()

_create()
_filter()
_update()
_delete()
