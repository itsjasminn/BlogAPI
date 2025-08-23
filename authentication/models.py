from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import ImageField, DateTimeField, TextChoices, BooleanField
from django.db.models import Model, ForeignKey, CASCADE, ManyToManyField
from django.db.models.fields import CharField, EmailField, IntegerField


class User(AbstractUser):
    class RoleType(TextChoices):
        ADMIN = "admin", "Admin"
        MODERATOR = "moderator", "Moderator"
        USER = 'user', 'User'

    reputation = IntegerField(default=0)
    avatar = ImageField(upload_to='avatars/%Y/%m/%d/', null=True, blank=True)
    email = EmailField(max_length=255, unique=True)
    bio = RichTextField(null=True, blank=True)
    location = CharField(max_length=50, null=True, blank=True)
    role = CharField(max_length=25, choices=RoleType.choices, default=RoleType.USER)
    city = ForeignKey('authentication.City', related_name='users', on_delete=CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class City(Model):
    name = CharField(max_length=60)


class Follow(Model):
    class Meta:
        unique_together = ("follower", "following")

    follower = ForeignKey('authentication.User', related_name='following_set', on_delete=CASCADE)
    following = ForeignKey('authentication.User', related_name='followers_set', on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower.username} -> {self.following.username}"


class Badge(Model):
    name = CharField(max_length=255, unique=True)
    description = RichTextField(null=True, blank=True)
    icon = ImageField(upload_to='badges/%Y/%m/%d/', null=True, blank=True)
    users = ManyToManyField(User, related_name='badges', blank=True)

    def __str__(self):
        return self.name


class Notifications(Model):
    class NotificationType(TextChoices):
        NEW_FOLLOWER = 'new_follower', 'New Follower'
        ANSWER_UPVOTE = 'answer_upvote', 'Answer Upvote'
        BLOG_COMMENT = 'blog_comment', 'Blog Comment'
        WARNING = 'warning', 'Moderator Warning'

    recipient = ForeignKey('authentication.User', on_delete=CASCADE, related_name="notifications")
    type = CharField(max_length=20, choices=NotificationType.choices, default=NotificationType.NEW_FOLLOWER)
    message = RichTextField()
    created_at = DateTimeField(auto_now_add=True)
    is_read = BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.recipient.username}"
