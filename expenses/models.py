from django.db import models

class Expense(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=100)
    amount = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return f"{self.date} - {self.category} - ${self.amount}"
