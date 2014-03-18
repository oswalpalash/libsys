from django.template.loader import get_template
from django.template import Template, Context
from django.http import Http404, HttpResponse
import datetime
from django.shortcuts import render,render_to_response, get_object_or_404
from books.models import Book
from contact.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.template import loader, Context
from django.http import HttpResponse
from blog.models import BlogPost
from django.db.models import Q

def hello(request):
	return HttpResponse("Hello world")
	
def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})	
def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	t = get_template('hours_ahead.html')
	return render(request, 'hours_ahead.html', {'hour_offset': offset,'next_time':dt})	
	
def search_form(request):
    return render(request, 'search_form.html')
	
def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		elif len(q) > 20:
			errors.append('Please enter at most 20 characters.')
		else:
			books = Book.objects.filter(title__icontains=q)
			return render(request, 'search_results.html',
				{'books': books, 'query': q})
	return render(request, 'search_form.html',
		{'errors': errors})
		
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'noreply@example.com'),
				['siteowner@example.com'],
			)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
			initial={'subject':'Enter Your Subject'}
			)
	return render(request, 'contact_form.html', {'form': form})

def foobar_view(request, url):
    m_list = MyModel.objects.filter(is_new=True)
    if url == 'foo':
        template_name = 'template1.html'
    elif url == 'bar':
        template_name = 'template2.html'
    return render(request, template_name, {'m_list': m_list})
	
def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({ 'posts': posts })
    return HttpResponse(t.render(c))

