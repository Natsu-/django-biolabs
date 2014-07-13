from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from biolabs.core import views


admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'labs', views.LaboratoryViewSet)


urlpatterns = patterns(
    '',

    # Examples:
    # url(r'^$', 'biolabs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)
