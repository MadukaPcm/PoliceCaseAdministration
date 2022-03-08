from django.shortcuts import redirect, render
from account.decolators import un_police,un_explorer
from co.models import CaseStatus
from co.forms import CaseViewForm
from co.models import Case

from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.urls import reverse


# Create your views here.
@un_police
def DashboardpoliceView(request):
    
    context = {}
    return render(request,'police/dashboardpolice.html', context)

class CaseView(CreateView):
 
    model = Case
    fields = ['case_no','reporter','case_site','phoneNo','description']
    template_name = 'police/createcase.html'

    def get_success_url(self):
        return reverse('caseliststatus_url')

def CaseListStatusView(request):
    ddd = CaseStatus.objects.all()
    
    context = {'dattt':ddd}
    return render(request,'police/caseliststatus.html', context)


def CaseStatusDetailView(request,pk):
    tt = CaseStatus.objects.get(id=pk)
    form = CaseViewForm(instance=tt)
    
    context = {'formm':form}
    return render(request,'police/casestatusdetail.html', context)

def ProfileView(request):
    
    context = {}
    return render(request,'police/profile.html', context)