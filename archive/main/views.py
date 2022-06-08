from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .filters import *
from .models import *

# Create your views here.
def Home(request):
    return redirect('docs')

def Docs(request):
    docs = Document.objects.all()
    docs_filter = DocsFilter(request.GET, queryset=docs)
    docs = docs_filter.qs

    data = {'docs': docs,
            'docs_filter': docs_filter}
    return render(request, 'docs.html', data)

class DocsDetailView(DetailView):
    model = Document
    template_name = 'docs_detail.html'

def DeleteDocs(request, id):
    docs = Document.objects.get(id=id)

    if docs.author == request.user:
        docs.delete()
    elif request.user.is_superuser:
        docs.delete()
    else:
        raise Http404

    return redirect('docs')

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def server_error_view(request):
    return render(request, '500.html', status=500)
