from django.db import models


class Promise(models.Model):
    name = models.CharField(max_length=255, blank=False)
    dline = models.CharField(max_length=20, blank=False)
    desc = models.CharField(max_length=255, blank=False)
    create_time = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='promise', on_delete=models.CASCADE)
    #owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     super(Promise, self).save(*args, **kwargs)

