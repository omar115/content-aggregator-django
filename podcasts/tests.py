from turtle import title
from urllib import response
from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse
from .models import Episode

class PodCastsTests(TestCase):
    def setUp(self):
        self.episode = Episode.objects.create(
            title = "My Awesome Podcast Episode",
            description = "Look mom, I made it!",
            pub_date = timezone.now(),
            link = "https://myawesomeshow.com",
            image = "https://image.myawesomeshow.com",
            podcast_name = "My Python Podcast",
            guid = "de18k-sdhil32-islkn12-fetr",
        )
    
    def test_episode_content(self):
        self.assertEqual(self.episode.description, "Look mom, I made it!")
        self.assertEqual(self.episode.link, "https://myawesomeshow.com")
        self.assertEqual(
            self.episode.guid, "de18k-sdhil32-islkn12-fetr"
        )
    
    def test_episode_guid(self):
        self.assertEqual(
            str(self.episode), "My Python Podcast: My Awesome Podcast Episode"
        )

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_home_page_uses_correct_template(self):
        res = self.client.get(reverse('homepage'))
        self.assertTemplateUsed(res, 'homepage.html')
    
    # def test_homepage_list_contents(self):
    #     res = self.client.get(reverse('hompage'))
    #     self.assertContains(res, "My Awesome Podcast Episode")