from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Feature(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Test(models.Model):
    feature = models.ForeignKey(Feature)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class Browser(models.Model):
    CHROME = 'C'
    FIREFOX = 'FF'
    IE = 'IE'
    SAFARI = 'S'
    BROWSER_CHOICES = (
        (CHROME, 'Google Chrome'),
        (FIREFOX, 'Mozilla Firefox'),
        (IE, 'Internet Explorer'),
        (SAFARI, 'Safari')
    )

    OSX = 'OSX'
    WIN7 = 'Win7'
    WIN8 = 'Win8'
    WIN10 = 'Win10'
    OS_CHOICES = (
        (OSX, 'OSX'),
        (WIN7, 'Windows 7'),
        (WIN8, 'Windows 8'),
        (WIN10, 'Windows 10'),
    )

    project = models.ForeignKey(Project, null=True)
    name = models.CharField(max_length=200,
                            choices=BROWSER_CHOICES,
                            default=CHROME)
    version = models.CharField(max_length=200, blank=True)
    operating_system = models.CharField(max_length=200, choices=OS_CHOICES)

    def __str__(self):
        return self.name
