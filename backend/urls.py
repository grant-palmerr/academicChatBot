from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from professors.views import ask_bot

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ask_bot/', ask_bot, name='ask_bot'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),  # Serve React app
]