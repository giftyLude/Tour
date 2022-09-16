from django.shortcuts import render
from django.views import generic

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from .models import Profile
from guide.models import *
from .forms import SignUpForm


def SignUpView(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.email = form.cleaned_data.get("email")
        user.profile.slug = form.cleaned_data.get("username")
        user.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect(
            reverse("profile-update", kwargs={"slug": username})
        )
    else:
        form = SignUpForm()
    return render(request, "users/signup.html", {"form": form})


class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    model = Profile
    template_name = "users/profile_detail.html"


class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    fields = ["name", "email", "gender"]
    template_name = "users/profile_update.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("profile-detail", kwargs={"slug": self.request.user.username})


class ProfileSites(LoginRequiredMixin, generic.ListView):
    model = Site
    template_name = "users/sites.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(ProfileSites, self).get_context_data(**kwargs)
        user = self.request.user
        context["sites"] = user.profile.sites.all()
        return context


class ProfileLodges(LoginRequiredMixin, generic.ListView):
    model = Lodge
    template_name = "users/lodges.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(ProfileLodges, self).get_context_data(**kwargs)
        user = self.request.user
        context["lodges"] = user.profile.lodges.all()
        return context


class ProfileEvents(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = "users/events.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(ProfileEvents, self).get_context_data(**kwargs)
        user = self.request.user
        context["events"] = user.profile.events.all()
        return context
