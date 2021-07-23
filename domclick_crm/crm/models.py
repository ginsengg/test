from django.db import models
import django.utils.timezone


class Client(models.Model):

    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    telegram_nickname = models.CharField(max_length=50, null=True)

    def __str__(self):
        return 'Client {} {}'.format(self.first_name, self.second_name)


class Employee(models.Model):

    positions = (
        ('M', 'Manager'),
        ('D', 'Director'),
        ('T', 'Tech support')
    )

    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    position = models.CharField(max_length=1, choices=positions)

    def __str__(self):
        return 'Employee {} {}(№{})'.format(self.first_name, self.second_name, self.id)


class Application(models.Model):

    statuses = (
        ('O', 'Opened'),
        ('W', 'In work'),
        ('C', 'Closed')
    )
    types = (
        ('R', 'Repair'),
        ('S', 'Service'),
        ('C', 'Consult')
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=statuses, default='O')
    type = models.CharField(max_length=1, choices=types)
    creation_time = models.TimeField(default=django.utils.timezone.now)

    def __str__(self):
        return 'Application №{} from {}'.format(self.id, self.client)
