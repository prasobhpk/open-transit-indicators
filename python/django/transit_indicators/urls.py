from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from datasources.views import GTFSFeedViewSet, GTFSFeedProblemViewSet

router = DefaultRouter()
router.register(r'gtfs-feeds', GTFSFeedViewSet)
router.register(r'gtfs-feed-problems', GTFSFeedProblemViewSet)

urlpatterns = patterns('',  # NOQA
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(router.urls)),
)
