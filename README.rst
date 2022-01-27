=====
django-wysiwyg-image
=====

An easy way to paste images to wysiwyg editors in Django admin interface. All it needs from you is to download an image through standard Django interface, and you will get a url to provide to your wysiwyg editor. 

Quick start
-----------

* Installation::

    pip install django-wysiwyg-image

2. Include the polls URLconf in your project urls.py like this::

    path('polls/', include('polls.urls')),

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.