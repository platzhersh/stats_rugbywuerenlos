from django.db import models

class Season(models.Model):
    start = models.IntegerField(verbose_name="Season start")

    def __unicode__(self):
      return str(self.start)+'/'+str(self.start+1)


class Player(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='players/',blank=True,null=True)
    birthdate = models.DateField(blank=True,null=True)
    entry = models.DateField(blank=True,null=True)
    active = models.BooleanField(default=True)

    def get_id(self):
      return self.firstName+self.lastName
    
    def get_name(self):
      return self.firstName+' '+self.lastName
    get_name.admin_order_field = 'firstName'

    def get_pointsInt(self):
      p = Point.objects.filter(player=self)
      sum = 0
      for point in p:
        sum += point.pointType.value
      return sum

    def get_points(self):
      return str(self.get_pointsInt())
    
    get_points.short_description = 'Points made'

    def __unicode__(self):
      return self.get_name()

class Game(models.Model):
    season = models.ForeignKey(Season,verbose_name="Season")
    opponent = models.CharField(max_length=50,verbose_name="Opponent")
    location = models.CharField(max_length=50,verbose_name="Location")
    homegame = models.BooleanField(default=False,verbose_name="Homegame?")
    pointsO = models.IntegerField(verbose_name="Points received",blank=True,null=True)
    date = models.DateTimeField(verbose_name="KickOff")
    mom = models.ForeignKey(Player,verbose_name="Man of the Match",blank=True,null=True,related_name='mom')
    tom = models.ForeignKey(Player,verbose_name="Tackler of the Match",blank=True,null=True,related_name='tom')

    def get_points(self):
      p = Point.objects.filter(game=self)
      sum = 0
      for point in p:
        sum += point.pointType.value
      return str(sum)
    
    get_points.short_description = 'Points made'

    def __unicode__(self):
      return self.opponent+' '+str(self.date)


class PointType(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()

    def __unicode__(self):
      return self.name

class Point(models.Model):
    pointType = models.ForeignKey(PointType)
    game = models.ForeignKey(Game)
    player = models.ForeignKey(Player)

    def __unicode__(self):
      return self.pointType.name+' by '+self.player.get_name()
