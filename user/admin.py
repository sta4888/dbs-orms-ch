from django.contrib import admin

from user.models import UserPosts, Group, UserPhotos, UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(UserPhotos)
class UserPhotosAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(UserPosts)
class UserPostsAdmin(admin.ModelAdmin):
    pass
