from django.urls import path
from . import views

app_name = 'cards'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('add_profile/', views.add_profile, name='add_profile'),
    path('edit/<int:uid>/', views.edit_card, name='edit_card'),
    path('download_vcf/', views.download_vcf, name='download_vcf'),
    
    # Public NFC URLs - program these into NFC cards
    path('p/<int:uid>/', views.public_profile, name='public_profile'),
    path('p/<int:uid>/vcf/', views.public_download_vcf, name='public_download_vcf'),
]
