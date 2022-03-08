from django.shortcuts import redirect, render
from account.decolators import un_explorer

# Create your views here.
@un_explorer
def DashboardexplorerView(request):
    
    context = {}
    return render(request, 'explorer/dashboardexplorer.html', context)