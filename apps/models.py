from ckeditor.fields import RichTextField
from django.db.models import ImageField, DateTimeField
from django.db.models import Model, ForeignKey, CASCADE, ManyToManyField
from django.db.models.fields import CharField, BooleanField


class Blog(Model):
    author = ForeignKey('authentication.User', related_name='blogs', on_delete=CASCADE)
    title = CharField(max_length=255)
    content = RichTextField()
    tags = CharField(max_length=255)
    likes = ManyToManyField('authentication.User', related_name='blog_likes')
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BlogImages(Model):
    blog = ForeignKey('apps.Blog', related_name='images', on_delete=CASCADE)
    image = ImageField()


class Comment(Model):
    blog = ForeignKey('apps.Blog', on_delete=CASCADE, related_name="comments")
    author = ForeignKey('authentication.User', on_delete=CASCADE)
    content = RichTextField()
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username}"


class Question(Model):
    author = ForeignKey('authentication.User', on_delete=CASCADE, related_name="questions")
    title = CharField(max_length=255)
    content = RichTextField()
    created_at = DateTimeField(auto_now_add=True)
    is_edited = BooleanField(default=False)

    def __str__(self):
        return self.title


class Answer(Model):
    question = ForeignKey(Question, on_delete=CASCADE, related_name="answers")
    author = ForeignKey('authentication.User', on_delete=CASCADE)
    content = RichTextField()
    created_at = DateTimeField(auto_now_add=True)
    upvotes = ManyToManyField('authentication.User', related_name="upvoted_answers", blank=True)
    downvotes = ManyToManyField('authentication.User', related_name="downvoted_answers", blank=True)

    def __str__(self):
        return f"Answer by {self.author.username}"
