from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, CreateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Scheduler


class SchedulerDeleteView(LoginRequiredMixin, DeleteView):
    model = Scheduler


class SchedulerCreateView(LoginRequiredMixin, CreateView):
    model = Scheduler

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SchedulerCreateView, self).form_valid(form)

    fields = ['message', 'one_time', 'every', 'datetime']



class SchedulerDetailView(LoginRequiredMixin, DetailView):
    model = Scheduler
    # These next two lines tell the view to index lookups by username
    #slug_field = 'username'
    #slug_url_kwarg = 'username'


class SchedulerRedirectView(LoginRequiredMixin, RedirectView):
    model = Scheduler
    #permanent = False

    #def get_redirect_url(self):
    #    return reverse('schedulers:detail',
    #                   kwargs={'pk': self.kwargs['pk']})

class SchedulerUpdateView(LoginRequiredMixin, UpdateView):
    model = Scheduler

    fields = ['message', 'one_time', 'every', 'datetime']

    # we already imported User in the view code above, remember?

    # send the user back to their own page after a successful update
    #def get_redirect_url(self):
    #    return reverse('schedulers:detail',
    #                   kwargs={'pk': self.kwargs['pk']})

    #def get_object(self):
    #    # Only get the User record for the user making the request
    #    return User.objects.get(username=self.request.user.username)


class SchedulerListView(LoginRequiredMixin, ListView):
    model = Scheduler

    def get_queryset(self):
        queryset = super(SchedulerListView, self).get_queryset()
        return queryset.filter(user = self.request.user)
    # These next two lines tell the view to index lookups by username
    #slug_field = 'username'
    #slug_url_kwarg = 'username'
