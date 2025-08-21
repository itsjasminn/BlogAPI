from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import ImageField, DateTimeField, TextChoices, BooleanField
from django.db.models import Model, ForeignKey, CASCADE, ManyToManyField
from django.db.models.fields import CharField, EmailField, IntegerField


class User(AbstractUser):
    class AddressType(TextChoices):
        TASHKENT = "Tashkent", "Toshkent, O'zbekiston"
        SAMARKAND = "Samarkand", "Samarqand, O'zbekiston"
        SURKHANDARYA = "Surkhandarya", "Surxondaryo, O'zbekiston"
        KASHKADARYA = "Kashkadarya", "Qashqadaryo, O'zbekiston"
        NAVOI = "Navoi", "Navoiy, O'zbekiston"
        BUKHARA = "Bukhara", "Buxoro, O'zbekiston"
        NAMANGAN = "Namangan", "Namangan, O'zbekiston"
        KHOREZM = "Khorezm", "Xorazm, O'zbekiston"
        FERGANA = "Fergana", "Farg'ona, O'zbekiston"
        JIZZAKH = "Jizzakh", "Jizzax, O'zbekiston"
        ANDIJAN = "Andijan", "Andijon, O'zbekiston"
        SYRDARYA = "Syrdarya", "Sirdaryo, O'zbekiston"
        KARAKALPAKSTAN = "Karakalpakstan", "Qoraqalpog'iston Respublikasi"

    reputation = IntegerField(default=0)
    avatar = ImageField(upload_to='avatars/%Y/%m/%d/', null=True, blank=True)
    email = EmailField(max_length=255, unique=True)
    bio = RichTextField(null=True, blank=True)
    location = CharField(max_length=50, choices=AddressType.choices, null=True, blank=True)
    two_factor = BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.first_name + " " + self.last_name

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)


class Follow(Model):
    class Meta:
        unique_together = ("follower", "following")

    follower = ForeignKey('authentication.User', related_name='follower', on_delete=CASCADE)
    following = ForeignKey('authentication.User', related_name='following', on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower.username} -> {self.following.username}"


class Comment(Model):
    blog = ForeignKey('authentication.Blog', on_delete=CASCADE, related_name="comments")
    author = ForeignKey(User, on_delete=CASCADE)
    content = RichTextField()
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username}"


class Question(Model):
    author = ForeignKey(User, on_delete=CASCADE, related_name="questions")
    title = CharField(max_length=255)
    content = RichTextField()
    created_at = DateTimeField(auto_now_add=True)
    topics = CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class Answer(Model):
    question = ForeignKey(Question, on_delete=CASCADE, related_name="answers")
    author = ForeignKey(User, on_delete=CASCADE)
    content = RichTextField()
    created_at = DateTimeField(auto_now_add=True)
    upvotes = ManyToManyField(User, related_name="upvoted_answers", blank=True)
    downvotes = ManyToManyField(User, related_name="downvoted_answers", blank=True)

    def __str__(self):
        return f"Answer by {self.author.username}"


class Blog(Model):
    author = ForeignKey('authentication.User', related_name='blogs', on_delete=CASCADE)
    title = CharField(max_length=255)
    content = RichTextField()
    tags = CharField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)
    likes = ManyToManyField('authentication.User', related_name='blogs_users', blank=True)


class Notifications(Model):
    class NotificationType(TextChoices):
        NEW_FOLLOWER = 'new follower', 'New Follower'
        ANSWER_UPVOTE = 'answer upvote', 'Answer Upvote'
        BLOG_COMMENT = 'blog comment', 'Blog Comment'
        WARNING = 'warning', 'MODERATOR Comment'

    recipient = ForeignKey(User, on_delete=CASCADE, related_name="notifications")
    type = CharField(max_length=20, choices=NotificationType, default=NotificationType.NEW_FOLLOWER)
    message = RichTextField()
    created_at = DateTimeField(auto_now_add=True)
    is_read = BooleanField(default=False)


class Badge(Model):
    name = CharField(max_length=255, unique=True)
    description = RichTextField(null=True, blank=True)
    icon = ImageField(upload_to='badges/%Y/%m/%d/', null=True, blank=True)
    users = ManyToManyField('authentication.User', related_name='badges_users', blank=True)

    def __str__(self):
        return self.name
