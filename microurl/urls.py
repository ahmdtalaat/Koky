from django.urls import path
from microurl import views as mv

app_name = "microurl"


urlpatterns = [
    path('', mv.home, name='home')
]
