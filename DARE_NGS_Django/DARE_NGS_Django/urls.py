from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin


urlpatterns = patterns(
    "",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^user/", TemplateView.as_view(template_name="user.html"), name="user"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r'^Jobs/$', 'job_management.views.Jobs', name='Jobs'),
    url(r'^dataAnalysis/$','job_management.views.Ibiomes', name='dataAnalysis'),
    url(r'^forms/$','job_management.views.forms', name='forms'),
    url(r'^edit/$','job_management.views.Jobs', name='edit'),
    url(r'^Jobs/update','job_management.views.update', name='update'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
