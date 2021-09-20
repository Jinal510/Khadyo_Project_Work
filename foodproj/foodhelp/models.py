
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.
class User(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=25)
    
    otp=models.IntegerField(default=459)
    role=models.CharField(max_length=10)
    is_active=models.BooleanField(default=True)
    is_verfied=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)

    def __str__(self):
        return self.email

class foodhelper(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=25)
    lastname=models.CharField(max_length=25)
    contact=models.CharField(max_length=10)
    profile_pic=models.FileField(upload_to="img", default="media/default.png")
    city=models.CharField(max_length=30,blank=True,null=True)
    area=models.CharField(max_length=30,blank=True,null=True)

    def __str__(self):
        return self.name

class UserRole(models.Model):
    role=models.CharField(max_length=50)

    def __str__(self):
        return self.role

class AddFood(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    fid=models.ForeignKey(foodhelper,on_delete=models.CASCADE)
    person_type=models.ForeignKey(UserRole,on_delete=models.CASCADE)
    reason=models.CharField(max_length=50)
    foodquantity=models.CharField(max_length=20)
    foodquality=models.CharField(max_length=20)
    cooktime=models.CharField(max_length=20)
    expirytime=models.CharField(max_length=20)
    food_categories=models.CharField(max_length=20,blank=True)
    food_picture=models.FileField(upload_to="media/img/")
    
    pickup_address=models.CharField(max_length=50)
    contact_person_name=models.CharField(max_length=20)
    contact_person_number=models.CharField(max_length=20)
    zipcode=models.CharField(max_length=20)

    def __str__(self):
        return self.contact_person_name

class NGO(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=25)
    contact=models.CharField(max_length=10)
    profile_pic=models.FileField(upload_to="img", default="media/default.png",blank=True)
    address=models.TextField(max_length=300,blank=True)
    area=models.CharField(max_length=30,blank=True,null=True) 
    def __str__(self):
        return self.name

class Feedback(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=25,blank=True)
    profile_pic=models.FileField(upload_to="img", default="media/default.png",blank=True)
    feedback=models.TextField(max_length=350,null=True)
    def __str__(self):
        return self.name

class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.order_id