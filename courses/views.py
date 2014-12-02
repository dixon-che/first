from django.shortcuts import render

# Create your views here.
def courses_list(request):
	r = render(request, 'index.html')
	print type(r)
	return r


def course_item(request, course_id):
	print request.user
	print request
	return render(request, 'index.html', {'id': course_id})


def course_view(request, course_slug):
	print course_slug
	return render(request, 'index.html', {'string': course_slug})

	