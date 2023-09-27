from django.db import models

# Create your models here.


class ChatHistory(models.Model):

    session_id = models.CharField(max_length=250)
    prompt = models.TextField(null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'session : {}'.format(self.session_id)

    class Meta:
        verbose_name_plural = 'Chat History'
