from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page

    path('polling-units/', views.polling_units_list, name='polling_units_list'),

    path('polling-unit/<int:pu_id>/', views.polling_unit_results, name='polling_unit_results'),

    path('lga-results/', views.lga_results, name='lga_results'),

    path('new-polling-unit/', views.new_polling_unit, name='new_polling_unit'), 

    path('ward-results/', views.ward_results, name='ward_results'),
    path('state-results/', views.state_results, name='state_results'), 
]
