from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ContactModel(BaseModel):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=13, null=True, blank=True
    )
    subject = models.CharField(
        max_length=255, null=True, blank=True
    )
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} | {self.email}"

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"


class StoreModel(BaseModel):
    image = models.ImageField(upload_to='stores/')
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=13)
    working_hours = models.CharField(max_length=255)
    location_link = models.URLField()
    picked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "store"
        verbose_name_plural = "stores"
