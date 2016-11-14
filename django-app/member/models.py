from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class MyUserManger(UserManager):
    pass


class MyUser(AbstractUser):
    img_profile = models.ImageField(
        upload_to='user',
        blank=True
    )
    following_users = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relationship',
        related_name='follower_users'
    )
    block_users = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='user_set_block'
    )

    def __str__(self):
        return self.get_full_name()

    def follow(self, user):
        instance, created = Relationship.objects.get_or_create(
            follower=self,
            followee=user,
        )
        return instance

    def unfollow(self, user):
        Relationship.objects.filter(follower=self, followee=user).delete()

    def unblock(self,user):
        self.block_users.remove()

    def friends(self):
        return self.following_users.filter(following_users=self)


class Relationship(models.Model):
    follower = models.ForeignKey(MyUser, related_name='relationship_set_follower')
    followee = models.ForeignKey(MyUser, related_name='relationship_set_following')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}가 {}을 follow합니다".format(self.followee, self.follower)