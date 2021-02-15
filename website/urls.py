from django.urls import path
from website.views import (
		index,
		about_us,
		services,
		locations,
		contact_us,
	)

urlpatterns = [
    path('', index, name='index'),
    path('about-us', about_us, name='about_us'),
    path('our-services', services, name='services'),
    path('our-locations', locations, name='locations'),
    path('contact-us', contact_us, name='contact_us'),
]