from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    url(r'^requests/new/$', login_required(NewFeatureRequestView.as_view()),
        name="new-feature-request"),
    url(r'^requests/(?P<pk>\d+)/(?P<slug>[-_\w]+)/$',
        login_required(FeatureRequestView.as_view()),
        name="feature-request"),
    url(r'^requests/(?P<pk>\d+)/(?P<slug>[-_\w]+)/success/$',
        login_required(NewFeatureRequestSuccessView.as_view()),
        name="new-feature-request-added"),
]
