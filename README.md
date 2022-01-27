# django-wysiwyg-image #

An easy way to paste images to wysiwyg editors in Django admin interface. All it needs from you is to download an image through standard Django interface, and you will get a url to provide to your wysiwyg editor. 

Quick start
-----------

**Installation:**

    pip install django-wysiwyg-image

**Usage:**

Let's imagine we have a blog with Post model in which we want to paste images by wysiwyg editor (in our tutorial django-tinymce editor). First up we're going to import ``BaseImageModel`` from ``wysiwyg_img.models`` and inherite from it our ``PostImage`` model. Then we have to tie by ``ForeignKey`` ``PostImage`` model to ``Post`` model. Now our ``models.py`` file should look like this:

```
from django.db import models

from tinymce import models as tinymce_models

from wysiwyg_img.models import BaseImageModel


class Post(models.Model):
    title = models.CharField(max_length=100)
    tiny_mce = tinymce_models.HTMLField()


class PostImage(BaseImageModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
```
Run ``./manage makemigrations`` and ``./manage.py migrate``
We also need do some configurations in ``admin.py`` file of current application:

```
from django.contrib import admin

from post.models import Post, PostImage
from wysiwyg_img.admin import ImageInline


class ImageInline(ImageInline):
    model = PostImage

class PostAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

admin.site.register(Post, PostAdmin)

```