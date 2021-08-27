from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile/images')
    bio = models.TextField()


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    images = models.ManyToManyField(to='Image', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)

    def __str__(self):
        return 'Post {} - \'{}...\' by {}'.format(self.id, self.content[:5], self.user.username)


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images')
