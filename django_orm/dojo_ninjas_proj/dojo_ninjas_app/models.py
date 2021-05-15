from django.db import models

# Create your models here.
class dojos(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    desc=models.TextField(null=True)
    
    def __repr__(self):
        return f'[Name: {self.name}, City: {self.city}, State: {self.state}, Ninjas: {self.ninjas}]'
    
class ninjas(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo=models.ForeignKey(dojos,related_name='ninjas',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
        return f"Name: {self.first_name} {self.last_name} ID: {self.id}"
    