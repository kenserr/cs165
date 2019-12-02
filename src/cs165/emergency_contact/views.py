from django.shortcuts import render, redirect, get_object_or_404
from .models import emergency_contact
from .forms import emergency_contact_form
# Create your views here.
def emergency_contact_detail_view(request, name):
	obj = emergency_contact.objects.get(emergency_contact=name)

	context = {
		"object": obj
	}


	return render(request, "emergency_contact/detail.html", context)
# Create your views here.

def emergency_contact_create_view(request):
	form = emergency_contact_form(request.POST or None)
	if form.is_valid():
		form.save()
		form = emergency_contact_form()

	context = {
		'form' : form
	}
	return render(request, "emergency_contact/create.html", context)
def emergency_contact_list_view(request):
	queryset = emergency_contact.objects.all()
	context = {
		"object_list" : queryset
	}

	return render(request, "emergency_contact/list.html", context)

def emergency_contact_update_view(request, name):
	obj = get_object_or_404(emergency_contact, emergency_contact=name)
	form = emergency_contact_form(request.POST or None, instance = obj)

	if form.is_valid():
		form.save()
		return redirect(emergency_contact_list_view)

	context = {
		"form": form
	}
	return render(request, "emergency_contact/update.html", context)