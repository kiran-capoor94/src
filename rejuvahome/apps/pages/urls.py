"""medical_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from .views import home_page, contact_page, about_page, PrivacyPolicyView, TnCView, HairTreatmentsView, FaceTreatmentsView, BodyTreatmentsView, SkinTreatmentsView, CosmeticTreatmentsView, BreastTreatmentsView, LaserTreatmentsView


urlpatterns = [
    path('', home_page, name='home'),
    path('about-us/', about_page, name='about'),
    # path('services/', Home.as_view(), name='services'),
    path('contact/', contact_page, name='contact'),
    path('users/',include('users.urls')),
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy-policy'),
    path('terms-conditions/', TnCView.as_view(), name='tnc'),
    path('hair-treatment/', HairTreatmentsView.as_view(), name='hair-treatment'),
    path('body-treatment/', BodyTreatmentsView.as_view(), name='body-treatment'),
    path('face-treatment/', FaceTreatmentsView.as_view(), name='face-treatment'),
    path('skin-treatment/', SkinTreatmentsView.as_view(), name='skin-treatment'),
    path('breast-treatment/', BreastTreatmentsView.as_view(), name='breast-treatment'),
    path('cosmetic-treatment/', CosmeticTreatmentsView.as_view(), name='cosmetic-treatment'),
    path('laser-treatment/', LaserTreatmentsView.as_view(), name='laser'),

]
