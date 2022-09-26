from django.urls import path
from .views import *

urlpatterns = [
    path('create-patients/', CreatePatient.as_view()),
    path('view-specialists/',ViewSPecialists.as_view()),
    path('injurys/',IsInjury.as_view()),
    path('filterdoctors/',FilterForDoctors.as_view()),
    path('pharmacy/<int:pk>/',PatientMedicines.as_view()),
    path('allthose/',AllThose.as_view()),
    path('those/',FilterThose.as_view()),
    path('info/',Info.as_view()),
    path('categorys/',Categoryview.as_view()),
    path('allpatients/',Patients.as_view())
]