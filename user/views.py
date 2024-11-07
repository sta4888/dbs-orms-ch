from django.contrib.auth.models import User
from django.shortcuts import render

from user.models import UserProfile, UserPhotos, UserPosts


def index(request):
    # SELECT * FROM myapp_userphotos WHERE user_id = (
    #     SELECT userprofile.id FROM myapp_userprofile
    #     JOIN auth_user ON myapp_userprofile.user_id = auth_user.id
    #     WHERE auth_user.username = 'some_username'
    # );
    user_photos = UserPhotos.objects.filter(user__user__username="test1")
    user_posts = UserPosts.objects.filter(user_profile__user__username="test1")

    # Retrieve all objects
    all_objects = UserProfile.objects.all()

    # Retrieve a single object
    single_object = UserProfile.objects.get(pk=2)

    # Filter objects
    # filtered_objects = UserProfile.objects.filter(user__user__username='test1')
    #
    # # Chaining filters
    # chained_filters = UserProfile.objects.filter(user__user__username='test1', another_field=14)

    # Exclude objects
    excluded_objects = UserProfile.objects.exclude(user__username='test1')

    # Ordering
    ordered_objects = UserProfile.objects.order_by('pk')

    # Count objects
    count_objects = UserProfile.objects.count()
    photos_objects = UserPhotos.objects.filter(user__user__username='new_user')

    # Check if an object exists
    exists = UserProfile.objects.filter(user__username='test1').exists()

    # Пример, когда есть доступ к User через ForeignKey/OneToOneField
    # Получение профиля пользователя вместе с данными пользователя в одном запросе
    user_profiles = UserProfile.objects.select_related('user').all()

    for profile in user_profiles:
        print(profile.user.username)  # Django не делает дополнительный запрос к User

    # Пример, когда UserProfile связан с множеством UserPhotos через ForeignKey
    user_profiles = UserProfile.objects.prefetch_related('photos').all()

    for profile in user_profiles:
        photos = profile.photos.all()  # Django не делает отдельный запрос для каждой итерации
        for photo in photos:
            print(photo.image.url)

    # Подгрузить данные пользователя с профилем (один к одному) и все фотографии (один ко многим) в один запрос
    user_profiles = UserProfile.objects.select_related('user').prefetch_related('photos').all()

    for profile in user_profiles:
        print(profile.user.username)
        for photo in profile.photos.all():
            print(photo.image.url)

    context = {
        'user_photos': user_photos,
        'user_posts': user_posts,
        'all_objects': all_objects,
        'single_object': single_object,
        'photos_objects': photos_objects,
        # 'filtered_objects': filtered_objects,
        # 'chained_filters': chained_filters,
        'excluded_objects': excluded_objects,
        'ordered_objects': ordered_objects,
        'count_objects': count_objects,
        'exists': exists,
    }

    return render(request, 'index.html', context=context)
