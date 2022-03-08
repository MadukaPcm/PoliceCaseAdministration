from django.urls import path
from . import views

#path urls for expert app.
urlpatterns = [
    path('',views.DashboardpoliceView, name='dashboardpolice_url'),
    path('case/',views.CaseView.as_view(), name='case_url'),
    path('caseliststatus/',views.CaseListStatusView, name='caseliststatus_url'),
    path('casestatusdetail/<str:pk>',views.CaseStatusDetailView, name='casestatusdetail_url'),
    path('profile',views.ProfileView, name='profile_url'),

]