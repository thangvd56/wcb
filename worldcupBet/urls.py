from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'worldcupBet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^danhsach', 'wcb.views.get_ds'),
    (r'^ketqua', 'wcb.views.get_kq'),
    (r'^results', 'wcb.views.get_result'),
    url(r'^logout/$', 'wcb.views.logout_page'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', 'wcb.views.register'),
    url(r'^register/success/$', 'wcb.views.register_success'),
    url(r'^home/$', 'wcb.views.home'),
)
