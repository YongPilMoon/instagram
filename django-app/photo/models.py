from django.conf import settings
from django.db import models
from django.urls import reverse
from versatileimagefield.fields import VersatileImageField

__all__ =[
    'Photo',
    'PhotoLike',
    'PhotoTag',
    'PhotoComment',
]


class Photo(models.Model):
    image = VersatileImageField(upload_to='upload')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    tags = models.ManyToManyField('PhotoTag', blank=True)
    created_date = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='PhotoLike',
        related_name='user_set_like_users'
    )

    def get_absolute_url(self):
        return reverse('photo:photo_list')

    def __str__(self):
        return '%s (author:%s)' % (
            self.content,
            self.author.get_full_name()
        )

    def to_dict(self):
        ret = {
            'id': self.id,
            'image': self.image.url,
            'author': self.author.id,
            'content': self.content,
            'commentList': [comment.to_dict() for comment in PhotoComment]
        }
        return ret


class PhotoTag(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now=True)


class PhotoComment(models.Model):
    photo = models.ForeignKey(Photo)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()

    def to_dict(self):
        ret = {
            'id': self.id,
            'photo': self.photo.id,
            'author': self.author.id,
            'content': self.content,
        }
        return ret


class PhotoLike(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now=True)

