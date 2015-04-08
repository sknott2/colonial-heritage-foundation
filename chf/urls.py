from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # Password Reset URLs:
   url(r'^account/password_reset/$', 
       'django.contrib.auth.views.password_reset', 
       {'post_reset_redirect' : '/account/password_reset/mailed/'},
       name="password_reset"),
       (r'^account/password_reset/mailed/$',
           'django.contrib.auth.views.password_reset_done'),
       (r'^account/password_reset/(?P<uidb64>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
           'django.contrib.auth.views.password_reset_confirm', 
           {'post_reset_redirect' : '/account/password_reset/complete/'}),
       (r'^account/password_reset/complete/$', 
           'django.contrib.auth.views.password_reset_complete'),
    url(r'^admin/', include(admin.site.urls)),
    # the django_mako_plus controller handles every request - this line is the glue that connects Mako to Django
    url(r'^.*$', 'django_mako_plus.controller.router.route_request' ),
)
