from django.urls import path

from . import views

app_name = 'acs'

urlpatterns = [
    # ex: /acs/
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('results/<int:offering_id>', views.offeringdetail, name='offeringdetail'),
]