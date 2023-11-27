from django.db import models

type_choices = [('auto','Auto'), ('patch', 'Patch'), ('auto/patch', 'Auto/Patch'), ('base', 'Base')]

class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class League(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
         return self.name
    
class Nation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
         return self.name

class Team(models.Model):
    name = models.CharField(max_length=255)
    nation = models.ForeignKey(Nation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Set(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    leagues = models.ManyToManyField(League)
    relase_date = models.DateField()

    def __str__(self):
        return self.name

class Subset(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=type_choices)
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    basic = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Parallel(models.Model):
    name = models.CharField(max_length=255)
    numbered = models.IntegerField(null=True,blank=True)
    subset = models.ForeignKey(Subset, on_delete=models.CASCADE)

    def __str__(self):
        return (f"#/{self.numbered} - {self.name}") if self.numbered else self.name

class Card(models.Model):
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    subset = models.ForeignKey(Subset, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return f"{self.set} - {self.player} - {self.team}"

