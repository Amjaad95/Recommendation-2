from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    following = models.ManyToManyField(User,
                                       related_name='followed_by',
                                        )
    bio = models.CharField(max_length=120)
    image = models.FileField(upload_to='Profile_image')


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to='Recommendation/categories/', null=True)

    def __unicode__(self):
        return self.name


class Recommendation(models.Model):
    user = models.ForeignKey(User)
    description = models.TextField()
    image = models.FileField(upload_to='recommendtion_image')
    submission_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,
                                 null=True,
                                        )

    def get_last_Recommednation(self):
        try:
            return self.Recommednation.filter(is_deleted=False).order_by('date').last()
        except Recommendation.DoesNotExist:
            return

    def __unicode__(self):
       return self.description


class Comment(models.Model):
    Recommendation = models.ForeignKey(Recommendation)
    user = models.ForeignKey(User)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "Comment by %s on Recommendation %s" % (self.user,
                                                       self.Recommendation.id)
