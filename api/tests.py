from django.test import TestCase
from wagtail.tests.utils import WagtailTestUtils
from wagtail.images.tests.utils import Image, get_test_image_file


class ImageAPI(TestCase, WagtailTestUtils):

    def setUp(self):
        self.login()

    def test_api_v2_no_images(self):
        response = self.client.get('/api/v2/images/')
        self.assertEqual(response.status_code, 200)
        response_dict = eval(response.content.decode(response.charset))
        self.assertIsInstance(response_dict, dict)
        self.assertEqual(response_dict['meta']['total_count'], 0)
        self.assertEqual(response_dict['items'], [])

    def test_api_v2_single_image(self):
        response = self.client.get('/api/v2/images/')
        self.assertEqual(response.status_code, 200)
        response_dict = eval(response.content.decode(response.charset))
        self.assertIsInstance(response_dict, dict)
        self.assertEqual(response_dict['meta']['total_count'], 0)
        self.assertEqual(response_dict['items'], [])

        expected_title = "Test image"
        image = Image.objects.create(
            title=expected_title,
            file=get_test_image_file(),
        )

        response = self.client.get('/api/v2/images/')
        self.assertEqual(response.status_code, 200)
        response_dict = eval(response.content.decode(response.charset))
        self.assertIsInstance(response_dict, dict)
        self.assertEqual(response_dict['meta']['total_count'], 1)
        returned_title = response_dict['items'][0]['title']
        self.assertEqual(expected_title, returned_title)
