from django.conf.urls import url
from PYTHONIDLE import views

urlpatterns = [
	url('',views.index),
	url(r'^home/$',views.greetings),
    url(r'^home/run$',views.runcode),
]
