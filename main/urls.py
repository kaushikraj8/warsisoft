from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name="main"

urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("contact/",views.contact,name="contact"),
    path("services/",views.services,name="services"),
    path("about/",views.about,name="about"),
   # path("homepage",views.homepage,name='homepage'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
