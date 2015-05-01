from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'core.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^accounts/logout/$', 'core.views.logout', name='logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
