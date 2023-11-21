from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    UNI_CHOICES = [
        ('pharmacy', '약학대학'),
        ('global', '글로벌융합대학'),
        ('science', '과학기술대학'),
        ('art', '미술대학'),
        # 나중에 더 추가할 예정 (이 기능이 실제로 구현된다고 하면)
    ]

    MAJOR_CHOICES = [
        ('computer', '컴퓨터공학전공'),
        ('cyber_security', '사이버보안전공'),
        ('it_media', 'IT 미디어 공학전공'),
        # 나중에 더 추가할 예정 (이 기능이 실제로 구현된다고 하면)
    ]
    class_number = models.CharField(
        unique=True,
        max_length=50,
        null=False
    )
    password = models.CharField(
        max_length=50,
        null=False
    )
    phone_number = models.CharField(max_length=20, unique=True, null=False)
    user_name = models.CharField(
        max_length=50,
        null=False
    )
    uni = models.CharField(
        max_length=50,
        choices=UNI_CHOICES,
        null=False
    )
    major = models.CharField(
        max_length=50,
        choices=MAJOR_CHOICES,
        null=False
    )

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return f'[{self.get_major_display()}] {self.class_number} - {self.user_name}'



# # Add related_name to groups and user_permissions fields
# User._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
# User._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_permissions'
#
#
# class Code(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="code_user")
#     code = models.PositiveIntegerField(null=True)