from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from guide.views import *
from users.views import *
from django.contrib.auth import views as auth_views

urlpatterns = (
    [
        path("manage/", admin.site.urls),
        path("ckeditor/", include("ckeditor_uploader.urls")),
        # GUIDE
        path("", HomeView, name="home"),
        path("sites", SiteList.as_view(), name="sites"),
        path("sites/search", SiteResults.as_view(), name="site_search-results"),
        path("sites/<int:pk>", SiteDetail.as_view(), name="site-detail"),
        path("sites/<int:pk>/add", SiteAdd.as_view(), name="site-add"),
        path("sites/<int:pk>/remove", SiteRemove.as_view(), name="site-remove"),
        # lodge
        path("lodges", LodgeList.as_view(), name="lodges"),
        path("lodges/search", LodgeResults.as_view(), name="lodge_search-results"),
        path("lodges/<int:pk>", LodgeDetail.as_view(), name="lodge-detail"),
        path("lodges/<int:pk>/add", LodgeAdd.as_view(), name="lodge-add"),
        path("lodges/<int:pk>/remove", LodgeRemove.as_view(), name="lodge-remove"),
        # events
        path("events", EventList.as_view(), name="events"),
        path("events/search", EventResults.as_view(), name="event_search-results"),
        path("events/<int:pk>", EventDetail.as_view(), name="event-detail"),
        path("events/<int:pk>/add", EventAdd.as_view(), name="event-add"),
        path("events/<int:pk>/remove", EventRemove.as_view(), name="event-remove"),
        # USERS auth
        path("signup/", SignUpView, name="signup"),
        path(
            "login/",
            auth_views.LoginView.as_view(template_name="users/login.html"),
            name="login",
        ),
        path(
            "logout/",
            auth_views.LogoutView.as_view(template_name="users/logout.html"),
            name="logout",
        ),
        # USERS profile
        path("<slug:slug>/", ProfileDetailView.as_view(), name="profile-detail"),
        path("<slug:slug>/update", ProfileUpdateView.as_view(), name="profile-update"),
        path("<slug:slug>/sites", ProfileSites.as_view(), name="profile-sites"),
        path("<slug:slug>/lodges", ProfileLodges.as_view(), name="profile-lodges"),
        path("<slug:slug>/events", ProfileEvents.as_view(), name="profile-events"),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
