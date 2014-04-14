from django.db import models

class Season(models.Model):
    start = models.IntegerField(verbose_name="Season start")

    def __unicode__(self):
      return str(self.start)+'/'+str(self.start+1)

class Position(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
      return self.name

class Player(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='players/',blank=True,null=True)
    birthdate = models.DateField(blank=True,null=True)
    position = models.CharField(max_length=30,null=True)
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
    
    @property
    def points(self):
      return str(self.get_pointsInt())
    
#    points.short_description = 'Points made'
   
    @property
    def cards(self):
      return self.get_cards()

    def get_cards(self):
      c = Card.objects.filter(player=self)
      return c.count()
     
    @property
    def tries(self):
      return self.get_tries() 

    def get_tries(self):
      points = Point.objects.filter(player=self)
      tries = points.filter(pointType = PointType.objects.filter(name="Try"))
      return tries.count()
    def get_dropgoals(self):
      points = Point.objects.filter(player=self)
      dg = points.filter(pointType = PointType.objects.filter(name="Drop Goal"))
      return dg.count()
    def get_penalties(self):
      points = Point.objects.filter(player=self)
      pen = points.filter(pointType = PointType.objects.filter(name="Penalty"))
      return pen.count()
    def get_conversions(self):
      points = Point.objects.filter(player=self)
      conv = points.filter(pointType = PointType.objects.filter(name="Conversion"))
      return conv.count()

    def __unicode__(self):
      return self.get_name()

class Location(models.Model):
    name = models.CharField(max_length=120)
    url = models.CharField(max_length=500, null = True)
    def __unicode__(self):
      return self.name

class League(models.Model):
    name = models.CharField(max_length=50)  
    def __unicode__(self):
      return self.name

class Team(models.Model):
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=200, null = True)
    pitch = models.ForeignKey(Location)
    league = models.ForeignKey(League)
    def __unicode__(self):
      return self.name

class Game(models.Model):
    season = models.ForeignKey(Season,verbose_name="Season")
    hostteam = models.ForeignKey(Team,verbose_name="Host",related_name="hostteam_set")
    guestteam = models.ForeignKey(Team,verbose_name="Guest",related_name="guestteam_set")
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
      return self.hostteam.name+' vs '+self.guestteam.name


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

class CardType(models.Model):
    name = models.CharField(max_length=50)
    # TODO: create HEX field with colour
    def __unicode__(self):
      return self.name

class Card(models.Model):
    cardType = models.ForeignKey(CardType)
    player = models.ForeignKey(Player)
    game = models.ForeignKey(Game)

    def __unicode__(self):
      return self.cardType.name+" ("+self.player.get_name()+")"
