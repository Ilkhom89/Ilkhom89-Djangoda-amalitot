from django.urls import path
from .views import contact_form, messages_list

urlpatterns = [
    path('', contact_form, name='contact'),
    path('xabarlar/', messages_list, name='messages'),
]
