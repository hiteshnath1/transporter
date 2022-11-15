from http.client import HTTPResponse
import imp
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView,UpdateView

from transport.models import branches,transport
from .forms import transportSearchForm,transportForm,branchesForm
from .models import branches

# Create your views here.

class transportListView(ListView):    
    model = transport
    template_name = "transport/index.html"
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return transport.objects.filter(user=self.request.user)
        else:
            return transport.objects.all()


class transportDetailView(DetailView):
    model = transport
    template_name = "transport/detail.html"

class branchDetailView(DetailView):
    model = branches
    template_name = "transport/branch detail.html"


def add_transport(request):
    form = transportForm()
    if request.method == 'POST':
        form = transportForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            fm = form.save(commit=False)
            fm.user = request.user
            fm.save()
            form = transportForm()

    else:
        form = transportForm()


    context = {
        'form':form,
    }
    return render(request,'transport/add_transport.html',context)

def add_branch(request):
    form = branchesForm()
    choice = request.GET.get('id')
    transporter = transport.objects.get(id=choice)
    if request.method == "POST":
        form = branchesForm(request.POST)
        if form.is_valid():
            fm = form.save(commit=False)
            fm.transport = transporter
            fm.save()
            form = branchesForm()


    context={
        'form':form,
    }

    return render(request,'transport/add_branch.html',context)

class branchesUpdateView(UpdateView):
    model = branches
    fields = [
        "name",
        "address",
        'mobile_no',
        'landline_no',
        'email',
        "transporter_id"
    ]
    success_url = "/"
    template_name = "transport/edit_branch.html"

class branchesDeleteView(DeleteView):
    model = branches
    success_url ="/"
    template_name = "transport/delete_branch.html"


class transportDeleteView(DeleteView):
    model = transport
    success_url ="/"
    template_name = "transport/delete_transport.html"

class transportUpdateView(UpdateView):
    model = transport
    fields = [
        "name",
        "address",
        "logo",
        'mobile_no',
        'landline_no',
        'email',
        "transporter_id"
    ]
    success_url = "/"
    template_name = "transport/edit_transport.html"


def transporter_search(request):
    final_transporter = None
    source = None
    destination = None
    form = transportSearchForm()
    if request.method == "POST":
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        source_transporter = transport.objects.filter(branches__name__contains = source)
        destination_transporter = transport.objects.filter(branches__name__contains = destination)        
        final_transporter = set(source_transporter).intersection(set(destination_transporter))
        
    context={
        'form':form, 
        'source':source,
        'destination':destination,
        'destination_transporter':final_transporter, 
    }
    return render(request,'transport/search_transport.html',context)

def search(request):
    transporter = None
    if  request.method == 'GET':
        trans_name = request.GET['search']
        transporter = transport.objects.filter(name__contains = trans_name)
        print(transporter)

        context = {
            'transporter': transporter
        }   
        return render(request,'transport/search_result.html',context)

def chatbot(request):
    transporter = transport.objects.all()
    context= {
        'transporter':transporter
    }
    return render(request,'transport/chatbot copy.html',context)