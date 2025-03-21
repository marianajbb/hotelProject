from bson import ObjectId
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    department = models.CharField(max_length=255)
    salary = models.FloatField()
    hire_date = models.DateField()
    projects = models.JSONField(default=list)  # Use JSONField for the 'projects' array
    id = models.CharField(max_length=255, primary_key=True)

    @property
    def id(self):
        return self._id  # Access the _id field as `id` in the template

    # Optional: Add a save method if you need to override the behavior when saving an instance
    def save(self, *args, **kwargs):
        if not self.id:  # Corrected line
            # Your logic to generate a new ID (if needed)
            pass
        super().save(*args, **kwargs)
