import uuid
from django.db import models


class BaseModel(models.Model):
    """
    An abstract base model that provides a UUID primary key
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
