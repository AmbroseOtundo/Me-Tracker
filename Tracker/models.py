from django.db import models
from django.contrib.auth.models import User

class Medicine(models.Model):
    medicine_name = models.CharField(max_length=30)
    DOSAGE_TYPE=(
        ('Drop', 'Drop'),
        ('Injection','Injection'),
        ('Vial','Vial'),
        ('Pill','Pill'),
        ('Tablet', 'Tablet'),
        ('Diff Form', 'Different Form'),

    )
    dosage = models.CharField(choices=DOSAGE_TYPE, max_length=30)
    FREQU_CHOICES =(
        ('Daily', 'Daily'),
        ('Weekly','weekly'),
        ('Monthly','monthly'),
    )
    frequency = models.CharField(choices=FREQU_CHOICES,max_length=30)
    OCCURENCE = (
        ('Once per frequency','once'),
        ('Twice per frequency', 'twice'),
        ('Thrice per frequency', 'thrice'),
        ('custom use', 'custom')
    )
    occurence = models.CharField(max_length=30, choices=OCCURENCE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username