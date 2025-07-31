from django.db import models
from ckeditor.fields import RichTextField
from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = RichTextField()

    def __str__(self):
        return self.question
