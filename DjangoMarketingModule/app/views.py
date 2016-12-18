"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest,HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from .forms import NameForm
from .models import PersonInfo
from django.views.generic.list import ListView
from django.views import generic


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


def addEmail(request):    
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)        
        if form.is_valid():            
            new_form = form.save()            
            return HttpResponseRedirect('/list.html')    
    else:
        form = NameForm()

    return render(request, 'app/add.html', {
        'form': form, 
        'title': 'Add Email',        
        'year':datetime.now().year,
        }
    )

class EmailListView(generic.ListView):
    model = PersonInfo
    template_name = 'app/list.html'
    paginate_by = 7
    queryset = PersonInfo.objects.all() 

    def get_context_data(self, **kwargs):
        context = super(EmailListView, self).get_context_data(**kwargs)
        context.update({
            'title': 'List',
            'year':datetime.now().year,            
        })
        return context