from django.db import models

class TravelBooking(models.Model):
    destination = models.CharField(max_length=200, null=False, blank=False)
    departure_city = models.CharField(max_length=200, null=False, blank=False)
    departure_date = models.DateField(null=False, blank=False)
    return_date = models.DateField(null=False, blank=False)
    adults = models.PositiveIntegerField(default=1, null=False, blank=False)
    children = models.PositiveIntegerField(default=0, null=False, blank=False)
    travel_class = models.CharField(max_length=50, null=False, blank=False)
    include_accommodation = models.BooleanField(default=False)
    include_activities = models.BooleanField(default=False)
    special_requirements = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.destination} - {self.departure_city} ({self.departure_date} to {self.return_date})"
