from django.db import models

class charityInfo(models.Model):
    reg_charity_id=models.IntegerField(max_length=40, primary_key=True)
    addr1=models.CharField(max_length=40, null=True)
    addr2=models.CharField(max_length=40, null=True)
    addr3=models.CharField(max_length=40, null=True)
    addr4=models.CharField(max_length=40, null=True)
    pri_phone_number=models.IntegerField(max_length=10, null=True)
    sec_phone_numer=models.IntegerField(max_length=10, null=True)
    email=models.EmailField(max_length=40)
    charity_description=models.CharField(max_length=1000, null=True)
	
class charityLogin(models.Model):
    reg_charity_id=models.IntegerField(max_length=40, primary_key=True)
    user_name=models.CharField(max_length=40)
    charity_password=models.CharField(max_length=40)
	
class charityAdmin(models.Model):
    reg_charity_id=models.IntegerField(max_length=40, primary_key=True)
    charity_name=models.CharField(max_length=40)
	
class charityUploads(models.Model):
    reg_charity_id=models.IntegerField(max_length=40, primary_key=True)
    content_type=models.CharField(max_length=5)
    content_path_name=models.CharField(max_length=200)
    content_description=models.CharField(max_length=1000)

class adopterInfo(models.Model):
    adopter_id=models.IntegerField(max_length=40, primary_key=True)
    adopter_name=models.CharField(max_length=40)

class adoptions(models.Model):
    adopter_id=models.IntegerField(max_length=40, primary_key=True)
    adopted_id=models.IntegerField(max_length=40)
    date=models.DateField(null=True)

class adoptedInfo(models.Model):
    adopted_id=models.IntegerField(max_length=40, primary_key=True)
    adopted_name=models.CharField(max_length=40)

class eventInfo(models.Model):
    event_id=models.IntegerField(max_length=40, primary_key=True)
    event_name=models.CharField(max_length=40)

class events(models.Model):
    reg_charity_id=models.IntegerField(max_length=40, primary_key=True)
    event_id=models.IntegerField(max_length=40, primary_key=True)
    event_start_date=models.DateField(null=True)
    event_end_date=models.DateField(null=True)
    event_description=models.CharField(max_length=250, null=True)
	
class sponsorship(models.Model):
    reg_charity_id=models.IntegerField(max_length=40, primary_key=True)
    sponsor_name=models.CharField(max_length=40, null=True)
    sponsee_id=models.IntegerField(max_length=40)
    date=models.DateField(null=True)
    amount=models.DecimalField(max_digits=40, decimal_places=2)

class sponsee(models.Model):
    sponsee_id=models.IntegerField(max_length=40, primary_key=True)
    sponsee_name=models.CharField(max_length=40)
	
class donations(models.Model):
    reg_charity_id=models.IntegerField(max_length=40, primary_key=True)
    donor_name=models.CharField(max_length=40, null=True)
    date=models.DateField(null=True)
    amount=models.DecimalField(max_digits=40, decimal_places=2)

class userAdmin(models.Model):
    user_id=models.IntegerField(max_length=40, primary_key=True)
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)

class userInfo(models.Model):
    user_id=models.IntegerField(max_length=40, primary_key=True)
    addr1=models.CharField(max_length=40, null=True)
    addr2=models.CharField(max_length=40, null=True)
    addr3=models.CharField(max_length=40, null=True)
    addr4=models.CharField(max_length=40, null=True)
    phone_number=models.IntegerField(max_length=10, null=True)
    email=models.EmailField(max_length=40)

class tempUserLogin(models.Model):
    user_id=models.IntegerField(max_length=40, primary_key=True)
    user_name=models.CharField(max_length=40)
    user_password=models.CharField(max_length=40)

class userUploads(models.Model):
    reg_charity_id=models.IntegerField(max_length=40, primary_key=True)
    user_id=models.IntegerField(max_length=40, primary_key=True)
    content_type=models.CharField(max_length=5)
    content_path_name=models.CharField(max_length=100)
    content_description=models.CharField(max_length=1000)
