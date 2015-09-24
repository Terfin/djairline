from django.forms import ModelForm, formset_factory
from .models import Ticket


class TicketForm(ModelForm):

    class Meta:
        model = Ticket
        fields = ['ticket_number', 'flight', 'passenger']
