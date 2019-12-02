from django.shortcuts import render, get_object_or_404, redirect
from .models import passport_holder
from .forms import passport_holder_form
# Create your views here.
def passport_holder_detail_view(request, id):
	obj = passport_holder.objects.get(passport_no=id)

	context = {
		"object": obj
	}


	return render(request, "passport_holder/detail.html", context)

def passport_holder_create_view(request):
	form = passport_holder_form(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(passport_holder_list_view)
	context = {
		'form': form
	}
	return render(request,"passport_holder/create.html", context)

def passport_holder_list_view(request):
	queryset = passport_holder.objects.all()
	context = {
		"object_list" : queryset
	}

	return render(request, "passport_holder/list.html", context)

def passport_holder_update_view(request, id):
	obj = get_object_or_404(passport_holder, passport_no=id)
	form = passport_holder_form(request.POST or None, instance = obj)

	if form.is_valid():
		form.save()
		return redirect(passport_holder_list_view)

	context = {
		"form": form
	}
	return render(request, "passport_holder/update.html", context)

def passport_holder_delete_view(request, id):
	obj = get_object_or_404(passport_holder, passport_no=id)
	if request.method == 'POST':
		obj.delete()
		return redirect(passport_holder_list_view)

	context = {
		"obj" : obj
	}
	return render(request, "passport_holder/delete.html", context)