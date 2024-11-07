from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField()
    # так не корректно если мы желаем чтоб у профиля пользователя было много фото поскольку отношение
    # ForeignKey указывает на "один ко многим"
    # photos = models.ForeignKey("UserPhotos", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class UserPhotos(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo for {self.user.user.username}"


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(UserProfile, related_name='groups')

    def __str__(self):
        return self.name


class UserPosts(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user_profile.user.username}"
