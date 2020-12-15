from django.test import TestCase
from articles.models import Article


class TestModels(TestCase):
    def test_article_has_an_author_and_title(self):
        article = Article.objects.create(title="The man in the high castle", author="Jone Brower")
        self.assertEqual(str(article), "The man in the high castle", "Jone Brower")

