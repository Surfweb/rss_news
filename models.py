from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Post(models.Model):
	id = models.BigIntegerField(primary_key=True)
	title = models.CharField(max_length=60)
	text = models.TextField()
	
	def __str__(self):
		self_id = str(self.id)
		return self_id + "_" + self.title