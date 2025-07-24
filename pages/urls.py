from django.urls import path

from pages.views import contact_view, home_page_view

app_name = 'pages'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('contact/', contact_view, name='contact'),
]
