from django.db import models

# Create your models here.
class Message(models.Model):
	title = models.CharField(max_length=25)
	message_maker = models.CharField(verbose_name="your name", max_length=25)
	message = models.TextField()

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	comment_maker = models.CharField(verbose_name="your name", max_length=25)
	comment = models.TextField()
	message = models.ForeignKey(Message)

	def __unicode__(self):
		return self.comment

