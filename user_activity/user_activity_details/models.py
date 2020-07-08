from django.db import models


class UserDetail(models.Model):
	id = models.CharField(primary_key=True, editable=False, max_length=11)
	name = models.CharField(max_length=100)
	time_zone = models.CharField(max_length=21)

	class Meta:
		db_table = 'user_details'


class UserActivity(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_activity'

  