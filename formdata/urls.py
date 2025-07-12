from django.urls import path
from .views import FormDataCreate, FormDataRetrieve

urlpatterns = [
    path('formdata/', FormDataCreate.as_view(), name='formdata-create'),
    path('formdata/<int:pk>/', FormDataRetrieve.as_view(), name='formdata-retrieve'),
]
