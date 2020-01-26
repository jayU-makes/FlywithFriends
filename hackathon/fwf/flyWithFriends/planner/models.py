from django.db import models

class Plan( models.Model ):
    s_date = models.DateField('Start Date')
    e_date = models.DateField('End Date')
    id = models.IntegerField(primary_key=True)
    #places = models.CharField(max_length=5000)

    def __str__(self):
        return str(self.id)

class Places (models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    days = models.IntegerField(default=0)

    def __str__(self):
        return self.name




