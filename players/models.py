from django.db import models


class HighSchool(models.Model):
    """
        Create HighSchool Table Into Database
    """
    name = models.CharField(max_length=50, null=True)


class Team(models.Model):
    """
        Create Team Table Into Database
    """
    name = models.CharField(max_length=50)
    logo = models.URLField()


class Position(models.Model):
    """
        Create Position Table Into Database
    """
    pos = models.CharField(max_length=12)


class Country(models.Model):
    """
        Create Country Table Into Database
    """
    name = models.CharField(max_length=12)

    def save(self, *args, **kwargs):
        self.name = 'US'
        super(Country, self).save(*args, **kwargs)


class State(models.Model):
    """
        Create State Table Into Database
    """
    name = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class City(models.Model):
    """
       Create City Table Into Database
    """
    name = models.CharField(max_length=20)
    state = models.ForeignKey(State, on_delete=models.CASCADE)


class Year(models.Model):
    """
        Create Year Table Into Database
    """
    year = models.IntegerField()


class Offers(models.Model):
    """
        Create Offers Table Into Database with relationship teams
    """
    teams = models.ManyToManyField(Team)


class Prospect(models.Model):
    """
        Create Player Table Into Database
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    height = models.CharField(max_length=15)
    weight = models.CharField(max_length=15)
    image = models.URLField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    school = models.ForeignKey(HighSchool, on_delete=models.CASCADE, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE, null=True, blank=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class HardCommited(models.Model):
    """
        Create Commited Table Into Database
    """
    commited = models.CharField(max_length=20, null=True)
    requited_by = models.CharField(max_length=40, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(Prospect, on_delete=models.CASCADE)


class TwitterInfo(models.Model):
    """
        Create Twitter_info Table Into Database
    """
    username = models.CharField(max_length=300, null=True)
    tweets_count = models.CharField(max_length=300, null=True)
    followers_count = models.CharField(max_length=300, null=True)
    following_count = models.CharField(max_length=300, null=True)
    last_tweet = models.CharField(max_length=3000, null=True)
    retweets_count = models.CharField(max_length=300, null=True)
    profile_name = models.CharField(max_length=300, null=True)
    location = models.CharField(max_length=300, null=True)
    player_id = models.ForeignKey(Prospect, on_delete=models.CASCADE)
