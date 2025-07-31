from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line assumes your API urls will be defined
    # in a urls.py file inside your faqs app directory.
    path('api/faqs/', include('faqs.urls_api')),
]