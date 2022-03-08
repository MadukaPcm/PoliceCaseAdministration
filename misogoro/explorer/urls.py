from django.urls import path
from . import views

#path urls for expert app.
urlpatterns = [
    path('',views.DashboardexplorerView, name='dashboardexplorer_url'),

]