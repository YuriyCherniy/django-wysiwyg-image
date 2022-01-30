from setuptools import setup

setup(
    name='django-wysiwyg-image',
    version='0.1.4',
    packages=['wysiwyg_img', 'wysiwyg_img.migrations'],
    requires=['python (>=3.6)', 'django (>=3.2)'],
    description='An easy way to paste images to wysiwyg editors in Django admin interface.',
    long_description=open('./README.md', 'r').read(),
    long_description_content_type='text/markdown',
    author='Yuriy Cherniy',
    author_email='amidobox@gmail.com',
    url='https://github.com/YuriyCherniy/django-wysiwyg-image',
)
