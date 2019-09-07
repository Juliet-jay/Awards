# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Location, tags, Image, Review, User, Profile
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.
class tagsTestClass(TestCase):
    
    # Set up method the test for location and instantiating the location object

    def setUp(self):
        self.test_tags = tags(name='funny')
        self.test_tags.save()
        
     # Testing instance

    def test_instance(self):
        self.assertTrue(isinstance(self.test_tags, tags))
        
    # Testing Save method

    def test_save_method(self):
        tags = tags.objects.create(name='funny')
        tags = tags.objects.all()
        self.assertTrue(len(tags) > 0)
        
    # Tear down method
    def tearDown(self):
        tags.objects.all().delete()
