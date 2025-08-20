from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import ImageField, DateTimeField, TextChoices, Model, ForeignKey, CASCADE, OneToOneField
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

    first_name = CharField(max_length=35)
    last_name = CharField(max_length=35)
    avatar = ImageField(upload_to='avatars/%Y/%m/%d/', null=True, blank=True)
    email = EmailField(max_length=255, unique=True)
    username = CharField(max_length=100, unique=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    bio = RichTextField(null=True, blank=True)
    location = CharField(max_length=50, choices=AddressType.choices, null=True, blank=True)
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


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name='profile')
    reputation = IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} (Reputation: {self.reputation})"


class Badge(Model):
    name = CharField(max_length=255, unique=True)
    description = RichTextField(null=True, blank=True)
    icon = ImageField(upload_to='badges/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.name


class UserBadge(Model):
    class Meta:
        unique_together = ("user", "badge")

    user = OneToOneField(User, on_delete=CASCADE, related_name='badges')
    badge = ForeignKey(Badge, on_delete=CASCADE)
    awarded_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} (Awarded: {self.awarded_at})"
