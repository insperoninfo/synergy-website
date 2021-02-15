from django.shortcuts import render


def index(request):
	return render(request, 'website/index.html')


def about_us(request):
	return render(request, 'website/about_us.html')


def services(request):
	return render(request, 'website/services.html')


def locations(request):
	return render(request, 'website/locations.html')


def contact_us(request):
	return render(request, 'website/contact_us.html')
