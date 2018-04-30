from django.db import models


class UserInfo(models.Model):
	post_name = models.CharField(max_length=40)
	post_password = models.CharField(max_length=20)