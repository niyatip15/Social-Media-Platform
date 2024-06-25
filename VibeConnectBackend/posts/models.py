import uuid
from django.db import models
from django.conf import settings
from django.utils.timesince import timesince

class PostAttachments(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    image = models.ImageField(upload_to='upload_posts')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='post_attachment',on_delete=models.CASCADE)



class Post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    content = models.TextField(blank=True,null=True)
    attachments = models.ManyToManyField(PostAttachments,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='posts',on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)

    def created_at_formatted_date(self):
        return timesince(self.created_at)