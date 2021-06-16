from django.db import models


class questions(models.Model):
    question_text = models.CharField(max_length=200)
   # pub_date = models.DateTimeField('date published')
    def __str__(self):
        return "{}".format(self.question_text)

