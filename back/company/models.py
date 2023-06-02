from django.db import models

class Thing(models.Model):
    image = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField()

class ExclusiveDeal(models.Model):
    city = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    old_price = models.CharField(max_length=10)
    new_price = models.CharField(max_length=10)
    image = models.CharField(max_length=100)

class ExclusiveDealGroup(models.Model):
    # Relación uno a muchos con ExclusiveDeal
    exclusive_deals = models.ManyToManyField(ExclusiveDeal)

class GetUpdate(models.Model):
    text = models.TextField()
    date = models.CharField(max_length=20)
    image = models.CharField(max_length=100)

class GetUpdateGroup(models.Model):
    # Relación uno a muchos con GetUpdate
    get_updates = models.ManyToManyField(GetUpdate)

class MainBanner(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    options_list = models.JSONField()

class VacationPlan(models.Model):
    city = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    quantity_days = models.CharField(max_length=20)
    rating = models.CharField(max_length=10)
    image = models.CharField(max_length=100)

class VacationPlanGroup(models.Model):
    # Relación uno a muchos con VacationPlan
    vacation_plans = models.ManyToManyField(VacationPlan)