from django.db import models


class person(models.Model):
    name = models.CharField(max_length=100)
    referal_code = models.IntegerField(unique=True)
    referred_by = models.CharField(max_length =100 ,null=True ,blank = True)
    profit = models.FloatField(default =0.0)
    Total_withdrawn = models.FloatField(default =0.0)

    def __str__(self):
        return self.name

class transaction(models.Model):
    person = models.ForeignKey(person, on_delete=models.CASCADE)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class referral_code(models.Model):
    usedby= models.ForeignKey(person, on_delete=models.CASCADE)
    code = models.IntegerField(unique=True)  
    date_used = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)  
