from django.db import models

# Create your models here.

class BaseModel(models.Model):
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True
