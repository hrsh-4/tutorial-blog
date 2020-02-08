from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from simplemathcaptcha.fields import MathCaptchaField
POST_CHOICE = (
    ('PUB','Public'),
    ('PVT','Private'),
)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    post_title = models.CharField(max_length = 200,unique = True)
    post_description = RichTextUploadingField()
    is_published = models.BooleanField(default = False)
    published_date = models.DateTimeField(auto_now_add = True)
    post_type = models.CharField(choices = POST_CHOICE, max_length = 3)
    # follows = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name = 'follows')

    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.post_title
    #
    # def get_delete_post_url(self):
    #     return reverse('blog:post-delete', kwargs={
    #                 'pk':self.pk
    #     })


    def publish_post(self):
        self.is_published = True
        return self.is_published

class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.name
