from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Player(models.Model):
    rank = models.IntegerField()
    name = models.CharField(max_length=50)
    team = models.CharField(max_length=5)
    position = models.CharField(max_length=5)
    projection = models.IntegerField()
    points = models.IntegerField()
    drafted = models.BooleanField()

    def __str__(self):
        return self.name

class Pick(models.Model):
    round = models.IntegerField()
    number = models.IntegerField()
    player = models.ForeignKey(Player, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'Pick ' + str(self.round) + '.' + str(self.number)

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str(self):
        return self.name
        
class League(models.Model):
    picks = models.ManyToManyField(Pick)
    players = models.ManyToManyField(Player)
    users = models.ManyToManyField(Team)
    leagueId = models.IntegerField()
    teams = models.IntegerField()
    rounds = models.IntegerField()

    def __str__(self):
        return 'League ' + str(self.leagueId)

