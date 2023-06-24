from django.test import TestCase
from .models import Author, Post, Comment


class BlogModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="John Doe")
        self.post = Post.objects.create(
            title="Test Post", content="This is a test post", author=self.author
        )
        self.comment = Comment.objects.create(
            post=self.post, content="This is a test comment", author=self.author
        )

    def test_author_creation(self):
        self.assertEqual(self.author.name, "John Doe")

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "This is a test post")
        self.assertEqual(self.post.author, self.author)

    def test_comment_creation(self):
        self.assertEqual(self.comment.content, "This is a test comment")
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.author, self.author)
