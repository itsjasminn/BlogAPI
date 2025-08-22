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

    class RoleType(TextChoices):
        ADMIN = "admin", "Admin"
        MODERATOR = "moderator", "Moderator"
        USER = 'user', 'User'

    # Extra fields
    reputation = IntegerField(default=0)
    avatar = ImageField(upload_to='avatars/%Y/%m/%d/', null=True, blank=True)
    email = EmailField(max_length=255, unique=True)
    bio = RichTextField(null=True, blank=True)
    location = CharField(max_length=50, choices=AddressType.choices, null=True, blank=True)
    two_factor = BooleanField(default=False)
    role = CharField(max_length=25, choices=RoleType.choices, default=RoleType.USER)
    topic_followed = ManyToManyField('authentication.Topic', related_name='topic_followed')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


# ------------------------
# 2. FOLLOW (Social graph)
# ------------------------
class Follow(Model):
    class Meta:
        unique_together = ("follower", "following")

    follower = ForeignKey(User, related_name='following_set', on_delete=CASCADE)
    following = ForeignKey(User, related_name='followers_set', on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower.username} -> {self.following.username}"


# ------------------------
# 3. TOPICS
# ------------------------
class Topic(Model):
    name = CharField(max_length=100, unique=True)
    description = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.name


# ------------------------
# 4. BLOGS
# ------------------------
class Blog(Model):
    author = ForeignKey(User, related_name='blogs', on_delete=CASCADE)
    title = CharField(max_length=255)
    content = RichTextField()
    tags = CharField(max_length=255)
    likes = ManyToManyField('authentication.User', related_name='blog_likes')
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(Model):
    blog = ForeignKey(Blog, on_delete=CASCADE, related_name="comments")
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


class Notifications(Model):
    class NotificationType(TextChoices):
        NEW_FOLLOWER = 'new_follower', 'New Follower'
        ANSWER_UPVOTE = 'answer_upvote', 'Answer Upvote'
        BLOG_COMMENT = 'blog_comment', 'Blog Comment'
        WARNING = 'warning', 'Moderator Warning'

    recipient = ForeignKey(User, on_delete=CASCADE, related_name="notifications")
    type = CharField(max_length=20, choices=NotificationType.choices, default=NotificationType.NEW_FOLLOWER)
    message = RichTextField()
    created_at = DateTimeField(auto_now_add=True)
    is_read = BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.recipient.username}"


class Badge(Model):
    name = CharField(max_length=255, unique=True)
    description = RichTextField(null=True, blank=True)
    icon = ImageField(upload_to='badges/%Y/%m/%d/', null=True, blank=True)
    users = ManyToManyField(User, related_name='badges', blank=True)

    def __str__(self):
        return self.name
