import uuid
from django.db import models

class GoodsEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=255)
    condition = models.IntegerField()

    @property
    def is_good_condition(self):
        return self.condition > 8