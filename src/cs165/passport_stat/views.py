from django.shortcuts import render
from .models import passport_stat
from .forms import passport_stat_form
# Create your views here.

def passport_stat_create_view(request):
	form = passport_stat_form(request.POST or None)
	if form.is_valid():
		form.save()
		form = passport_holder_form()
	context = {
		'form' : form
	}
	return render(request, "passport_stat/create.html", context)

def passport_stat_list_view(request):
	queryset = passport_stat.objects.all()
	context = {
		"object_list" : queryset
	}

	return render(request, "passport_stat/list.html", context)
