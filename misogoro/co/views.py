from django.shortcuts import render
from account.decolators import un_co
from co.models import *

from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.urls import reverse

from co.forms import CaseViewForm

# Create your views here.
@un_co
def DashboardcoView(request):
    
    context = {}
    return render(request, 'co/dashboardco.html', context)

def CaseAssignedView(request):
    assignedcase = CaseAssignment.objects.all()
    
    context = {'data':assignedcase}
    return render(request, 'co/caseassignment.html',context)
    
def CaseStatusView(request):
    statuslist = CaseStatus.objects.all()
    
    context = {'statuslist':statuslist}
    return render(request, 'co/casestatus.html', context)

class AddCaseStatusView(CreateView):
 
    model = CaseStatus
    fields = '__all__'
    template_name = 'co/addcasestutus.html'

    def get_success_url(self):
        return reverse('casestatus_url')

def CaseStatusDetailView(request, pk):
    dada = CaseStatus.objects.get(id=pk)
    datas = CaseViewForm(instance=dada)

    context = {'dat':datas}
    return render(request, 'co/casestatusdetail.html', context)

def MyProfileView(request):
    
    context = {}
    return render(request, 'co/myprofile.html', context)

def PoliceReportView(request):
    
    context = {}
    return render(request, 'co/policereport.html', context)

def ExplorerReportView(request):
    
    context = {}
    return render(request, 'co/explorerreport.html', context)

def CaseReportView(request):
    
    context = {}
    return render(request, 'co/casereport.html', context)

def CriminalCaseView(request):
    
    context = {}
    return render(request, 'co/criminalcase_report.html', context)
