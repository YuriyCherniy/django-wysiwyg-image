from django.test import TestCase, SimpleTestCase

from wysiwyg_img.models import BaseImageModel


class BaseImageModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        BaseImageModel.objects.create(
            image='test_image.jpg'
        )
    
    def test_str_method(self):
        img = BaseImageModel.objects.first()
        result = img.__str__()
        self.assertEqual(result, 'image id: 1')        

    def test_get_image_url_method(self):
        img = BaseImageModel.objects.first()
        url = img.get_image_url()
        self.assertEqual(url, '<h3>/test_image.jpg</h3>')

    def test_construct_image_tag_method(self):
        img = BaseImageModel.objects.first()
        tag = img.construct_image_tag()
        self.assertEqual(tag, '<img src="/test_image.jpg" width="50" height="auto"/>')


class SettingsTestCase(SimpleTestCase):
    def test_wysiwyg_img_upload_to_value(self):
        value = BaseImageModel.upload_to
        self.assertEqual(value, 'test_folder')

    def test_wysiwyg_img_image_width_value(self):
        value = BaseImageModel.image_width
        self.assertEqual(value, 50)