from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.utils.functional import lazy
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, FormMixin
from .models import Flight, Ticket
from .forms import TicketForm

# Create your views here.

class ListFormView(FormMixin, ListView):

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)

        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)


class HomeView(ListView):

    model = Flight
    queryset = Flight.objects.all()
    template_name = 'index.html'


class PilotAssignmentView(ListView):

    model = Flight
    queryset = Flight.objects.all()
    template_name = 'pilots.html'


class TicketView(ListFormView):
    form_class = TicketForm
    success_url = lazy(reverse, str)('tickets')
    template_name = 'tickets.html'
    queryset = Ticket.objects.all()

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.body)
        form.save()
        return HttpResponse()