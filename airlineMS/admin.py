from django.contrib import admin
from .models import *

# Register your models here.
admin.autodiscover()


class FlightAdmin(admin.ModelAdmin):
    pass


class TicketAdmin(admin.ModelAdmin):
    pass


class PersonAdmin(admin.ModelAdmin):
    pass


class AircraftAdmin(admin.ModelAdmin):
    pass

admin.site.register(Flight, FlightAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Passenger, PersonAdmin)
admin.site.register(Pilot, PersonAdmin)
admin.site.register(Aircraft, AircraftAdmin)