from django.db import models


class Aircraft(models.Model):

    manufacturer = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    manufacturer_sn = models.CharField(max_length=50)
    manufacturing_date = models.DateField()

    def __repr__(self):
        return '{} {}'.format(self.manufacturer, self.model)

    def __str__(self):
        return '{} {}'.format(self.manufacturer, self.model)


class Flight(models.Model):

    flight_number = models.CharField(max_length=10) ## e.g. - LY001
    origin = models.CharField(max_length=10) ## e.g. TLV
    destination = models.CharField(max_length=10) ## e.g. JFK
    aircraft = models.ForeignKey(Aircraft, related_name='flights')
    STD = models.DateTimeField() ## Scheduled Time of Departure
    ETD = models.DateTimeField(null=True, blank=True) ## Estimated Time of Departure
    STA = models.DateTimeField() ## Scheduled Time of Arrival
    ETA = models.DateTimeField(null=True, blank=True) ## Estimated Time of Arrival

    def __str__(self):
        return '{} -> {}'.format(self.origin, self.destination)


class Ticket(models.Model):

    ticket_number = models.CharField(max_length=20)
    flight = models.ForeignKey(Flight, related_name='tickets')
    purchase_date = models.DateTimeField()
    use_date = models.DateTimeField(null=True)
    passenger = models.ForeignKey('Passenger')


class Person(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    passport_number = models.CharField(max_length=20, null=True) # Obviously not everyone has a passport
    id_number = models.CharField(max_length=20) # You better have one of these, more than one is a luxury, or you're a spy


    class Meta:
        abstract = True

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Pilot(Person):

    employment_start_date = models.DateTimeField()
    flights = models.ManyToManyField(Flight, related_name='pilots')


class Passenger(Person):

    has_carry_on_luggage = models.BooleanField(default=True) # We usually bring a small bag of some kind


