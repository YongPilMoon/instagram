from django.test import LiveServerTestCase
from .models import MyUser


class FollowTest(LiveServerTestCase):
    def create_user(self, username, last_name, first_name):
        return MyUser.objects.create_user(
            username=username,
            last_name=last_name,
            first_name=first_name,
        )

    def test_create_user(self):
        print('test_create_user')
        u1 = self.create_user('u1', '방', '민아')
        u2 = self.create_user('u2', '이', '한영')
        u3 = self.create_user('u3', '박', '성환')

    def test_follow_user(self):
        print('test_create_user')
        u1 = self.create_user('u1', '방', '민아')
        u2 = self.create_user('u2', '이', '한영')
        u3 = self.create_user('u3', '박', '성환')

        u1.follow(u2)
        u1.unfollow(u2)

        u2.follow(u1)
        u3.follow(u2)
        u3.follow(u1)

        # print(u1.following_users.all())
        # print(u2.following_users.all())
        # print(u3.following_users.all())
        # print(u1.follower_users.all())

    def test_friends_user(self):
        print("test_friends_user")
        u1 = self.create_user('u1', '방', '민아')
        u2 = self.create_user('u2', '이', '한영')
        u1.follow(u2)
        print(u1.relationship_set_follower.all())
        print(u1.following_users.all())
        print(u1.follower_users.all())
        print(u1.relationship_set_following.all())
