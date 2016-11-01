from django.db import models
#from django.contrib.auth.models import User

class new_entry(models.Model):
	
    SPACES = (
        ('1', 'modal1'),
        ('2', 'modal2'),
        ('3', 'modal3'),
        ('4', 'modal4'),
    )

    name = models.CharField(max_length=128)
    entry = models.TextField(max_length=128)
    space = models.CharField(max_length=1, choices=SPACES)

    def __unicode__(self):
		return self.name
