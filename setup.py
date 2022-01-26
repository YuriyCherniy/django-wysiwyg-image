from setuptools import setup

setup(
    name='django-wysiwyg-image',
    version='0.1',
    packages=['wysiwyg_img', 'wysiwyg_img.migrations'],
    requires=['python (>=3.6)', 'django (>=3.2)'],
)