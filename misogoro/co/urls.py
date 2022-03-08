from django.urls import path
from . import views

#path urls for expert app.
urlpatterns = [
    path('',views.DashboardcoView, name='dashboardco_url'),
    path('caseassigned/',views.CaseAssignedView, name='caseassigned_url'),
    path('casestatus/',views.CaseStatusView, name='casestatus_url'),
    path('addcasestatus/',views.AddCaseStatusView.as_view(), name='addcasestatus_url'),
    path('casestatusview/<str:pk>',views.CaseStatusDetailView, name='casestatusview_url'),
    path('myprofile/',views.MyProfileView, name='myprofile_url'),
    
    #report management.....
    path('policereport/',views.PoliceReportView, name='policereport_url'),
    path('explorerreport/',views.ExplorerReportView, name='explorerreport_url'),
    path('casereport/',views.CaseReportView, name='casereport_url'),
    path('criminalcase/',views.CriminalCaseView, name='criminalcase_url'),
    

]