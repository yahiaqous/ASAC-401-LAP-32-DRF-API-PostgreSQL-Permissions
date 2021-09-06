from django.test import TestCase
from django.contrib.auth.models import User

from .models import Snack


class SnackTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(username="testuser1", password="abc123")
        testuser1.save()

        # Create a blog post
        test_snack = Snack.objects.create(
            author=testuser1, title="Blog title", body="Body content..."
        )
        test_snack.save()

    def test_snack_content(self):
        snack = Snack.objects.get(id=1)
        expected_author = f"{snack.author}"
        expected_title = f"{snack.title}"
        expected_body = f"{snack.body}"
        self.assertEqual(expected_author, "testuser1")
        self.assertEqual(expected_title, "Blog title")
        self.assertEqual(expected_body, "Body content...")