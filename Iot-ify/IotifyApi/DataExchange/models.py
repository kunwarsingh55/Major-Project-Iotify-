from django.db import models



class parking(models.Model):
    spot_1 = models.CharField(max_length=200,default="")
    spot_2 = models.CharField(max_length=200,default="")
    spot_3 = models.CharField(max_length=200,default="")
   # pub_date = models.DateTimeField('date published')
    def __str__(self):
        return "{}{}{}".format(self.spot_1,self.spot_2,self.spot_3)

class parkingBooking(models.Model):
    spot_1 = models.CharField(max_length=200,default="")
    spot_2 = models.CharField(max_length=200,default="")
    spot_3 = models.CharField(max_length=200,default="")
   # pub_date = models.DateTimeField('date published')
    def __str__(self):
        return "{}{}{}".format(self.spot_1,self.spot_2,self.spot_3)