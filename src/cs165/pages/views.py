from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from passport_holder.models import passport_holder
from passport_stat.models import passport_stat
from emergency_contact.models import emergency_contact
def home_view(request,*args, **kwargs):
	#return HttpResponse("<h1>Hello, world!</h1>")
	return render(request, "home.html", {})

#def new_application_view(request, *args, **kwargs):
#	return HttpResponse("<h1>here is where u make a new passport application</h1>")
#	my_context = {
#		"my_text": "This is to make new appl",
#		"my_number": 123,
#		"my_list": [123,32,21,2]
#
#	}
#	return render(request, "new_application.html", my_context)

def read_view(request, *args, **kwargs):
	damaged = passport_holder.objects.filter(passport_status__extra_documents__exact="Affidavit of Explanation")
	econtact = []
	econtactno = []
	app = []
	stats = []
	for i in damaged:
		app.append(i.applicant_name)
		stats.append(i.passport_status.passport_status)
		econtact.append(i.emergency_contact.emergency_contact)
		econtactno.append(i.emergency_contact.emergency_contact_number)
	querylist = [econtact, econtactno]
	context = {
		"object_list" : querylist,
		"app" : app,
		"n" : range(len(querylist[0])),
		"stats": stats
	}

	return render(request, "read.html", context)
