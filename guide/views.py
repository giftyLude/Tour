from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from django.urls import reverse
from django.shortcuts import redirect


@login_required
def HomeView(request):
    top_site_list = Site.objects.all()[:5]
    more_site_list = Site.objects.order_by("?")[:6]
    first_event = Event.objects.order_by("?")[:1]
    scroll_events = Event.objects.order_by("?")[:5]
    second_event = Event.objects.order_by("?")[:1]
    top_lodge_list = Lodge.objects.all()[:7]
    context = {
        "top_sites": top_site_list,
        "more_sites": more_site_list,
        "top_lodges": top_lodge_list,
        "first_event": first_event,
        "h_events": scroll_events,
        "second_event": second_event,
    }
    return render(request, "guide/home.html", context)


# APP PAGES
class SiteList(LoginRequiredMixin, generic.ListView):
    model = Site
    template_name = "guide/sites.html"
    context_object_name = "sites"
    paginate_by = 12


class SiteResults(LoginRequiredMixin, generic.ListView):
    model = Site
    template_name = "guide/site_search.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(SiteResults, self).get_context_data(**kwargs)
        query = self.request.GET.get("q")
        context["results"] = Site.objects.filter(Q(name__contains=query))
        return context


class SiteDetail(LoginRequiredMixin, generic.View):
    def get(self, request, *args, **kwargs):
        site = Site.objects.get(pk=self.kwargs["pk"])
        other_sites = Site.objects.order_by("?").exclude(pk=self.kwargs["pk"])[:5]

        context = {"site": site, "other_sites": other_sites}

        return render(request, "guide/site_detail.html", context=context)


class LodgeList(LoginRequiredMixin, generic.ListView):
    model = Lodge
    template_name = "guide/lodges.html"
    context_object_name = "lodges"
    paginate_by = 12


class LodgeResults(LoginRequiredMixin, generic.ListView):
    model = Lodge
    template_name = "guide/lodge_search.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(LodgeResults, self).get_context_data(**kwargs)
        query = self.request.GET.get("q")
        context["results"] = Lodge.objects.filter(Q(name__contains=query))
        return context


class LodgeDetail(LoginRequiredMixin, generic.View):
    def get(self, request, *args, **kwargs):
        lodge = Lodge.objects.get(pk=self.kwargs["pk"])
        other_lodges = Lodge.objects.order_by("?").exclude(pk=self.kwargs["pk"])[:5]

        context = {"lodge": lodge, "other_lodges": other_lodges}

        return render(request, "guide/lodge_detail.html", context=context)


class EventList(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = "guide/events.html"
    context_object_name = "events"
    paginate_by = 12


class EventResults(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = "guide/event_search.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(EventResults, self).get_context_data(**kwargs)
        query = self.request.GET.get("q")
        context["results"] = Event.objects.filter(Q(title__contains=query))
        return context


class EventDetail(LoginRequiredMixin, generic.DetailView):
    model = Event
    template_name = "guide/event_detail.html"
    context_object_name = "event"


# SAVING SITES/LODGES/EVENTS
class SiteAdd(generic.View):
    def get(self, request, **kwargs):
        if "pk" in self.kwargs:
            user = request.user
            site = Site.objects.get(pk=self.kwargs["pk"])
            user.profile.sites.add(site)
            user.profile.save()
            site.users.add(user)
            site.save()
            site.refresh_from_db()
        return redirect(reverse("site-detail", kwargs={"pk": site.pk}))


class SiteRemove(generic.View):
    def get(self, request, **kwargs):
        if "pk" in self.kwargs:
            user = request.user
            site = Site.objects.get(pk=self.kwargs["pk"])
            user.profile.sites.remove(site)
            user.profile.save()
            site.users.remove(user)
            site.save()
            site.refresh_from_db()
        return redirect(reverse("site-detail", kwargs={"pk": site.pk}))


class LodgeAdd(generic.View):
    def get(self, request, **kwargs):
        if "pk" in self.kwargs:
            user = request.user
            lodge = Lodge.objects.get(pk=self.kwargs["pk"])
            user.profile.lodges.add(lodge)
            user.profile.save()
            lodge.users.add(user)
            lodge.save()
            lodge.refresh_from_db()
        return redirect(reverse("lodge-detail", kwargs={"pk": lodge.pk}))


class LodgeRemove(generic.View):
    def get(self, request, **kwargs):
        if "pk" in self.kwargs:
            user = request.user
            lodge = Lodge.objects.get(pk=self.kwargs["pk"])
            user.profile.lodges.remove(lodge)
            user.profile.save()
            lodge.users.remove(user)
            lodge.save()
            lodge.refresh_from_db()
        return redirect(reverse("lodge-detail", kwargs={"pk": lodge.pk}))


class EventAdd(generic.View):
    def get(self, request, **kwargs):
        if "pk" in self.kwargs:
            user = request.user
            event = Event.objects.get(pk=self.kwargs["pk"])
            user.profile.events.add(event)
            user.profile.save()
            event.users.add(user)
            event.save()
            event.refresh_from_db()
        return redirect(reverse("event-detail", kwargs={"pk": event.pk}))


class EventRemove(generic.View):
    def get(self, request, **kwargs):
        if "pk" in self.kwargs:
            user = request.user
            event = Event.objects.get(pk=self.kwargs["pk"])
            user.profile.events.remove(event)
            user.profile.save()
            event.users.remove(user)
            event.save()
            event.refresh_from_db()
        return redirect(reverse("event-detail", kwargs={"pk": event.pk}))
