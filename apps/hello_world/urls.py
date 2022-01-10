from django.contrib import admin
from django.urls import path, include
from . import views



#Defined internal apps.
import apps.hello_world.views

urlpatterns = [
    path('webpres_admin/', admin.site.urls),
    path("", apps.hello_world.views.home, name='home'),
    path('new/', apps.hello_world.views.new, name='new'),
    path("services/", apps.hello_world.views.services, name="services"),
    path("sponsored_page/", apps.hello_world.views.sponsored_page, name="sponsored_page"),
    path("privacy/", apps.hello_world.views.privacy, name="privacy"),
    path("terms/", apps.hello_world.views.terms, name="terms"),
    path("contact/", apps.hello_world.views.contact, name="contact"),
]



