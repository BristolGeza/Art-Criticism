from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path('admin/', admin.site.urls),
    #path('art/', include("art.urls"), name='post_list_view'),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
    path("", include("art.urls"), name="art-urls"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)