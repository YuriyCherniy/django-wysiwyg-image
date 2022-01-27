# django-wysiwyg-image #

An easy way to paste images to wysiwyg editors in Django admin interface. All it needs from you is to download an image through standard Django interface, and you will get a url to provide to your wysiwyg editor. 

Quick start
-----------

**Installation:**

    pip install django-wysiwyg-image

**Usage:**

Let's imagine we have a blog with Post model in which we want to paste images by wysiwyg editor (in our tutorial django-tinymce editor). First up we're going to import ``BaseImageModel`` from ``wysiwyg_img.models`` and inherite from it our ``PostImage`` model. Then we have to tie by ``ForeignKey`` ``PostImage`` model to ``Post`` model.