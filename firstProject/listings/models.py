from django.db import models


class Language(models.TextChoices):
    JavaScript = 'JavaScript'
    CPlus = 'C++'
    CSharp = 'C#'
    Python = 'Python'
    PHP = 'PHP'
    none = 'None'


class Project(models.Model):
    name = models.fields.CharField(max_length=30)
    description = models.fields.CharField(max_length=100)

    # Change name object in Django administration
    def __str__(self):
        return f'{self.name}'


class User(models.Model):

    firstName = models.fields.CharField(max_length=30)
    lastName = models.fields.CharField(max_length=30)
    mail = models.fields.EmailField(max_length=100)
    address = models.fields.CharField(null=True, max_length=150)
    age = models.fields.IntegerField()
    registrationDate = models.fields.DateTimeField(auto_now=True)
    isMajor = models.fields.BooleanField()
    language = models.fields.CharField(
        choices=Language.choices, null=True, default='----', max_length=15)
    project = models.ForeignKey(
        Project, default='----', null=True, on_delete=models.SET_NULL)

    # Change name object in Django administration
    def __str__(self):
        return f"{self.firstName + ' ' + self.lastName}"
