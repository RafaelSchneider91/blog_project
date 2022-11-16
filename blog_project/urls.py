from django.contrib import admin
from django.urls import path
from blog.views import index, post_detail  # <------ NEW IMPORT

# import for display image
from django.conf import settings  # <------ NEW
from django.conf.urls.static import static  # <------ NEW

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('post-detail/<int:id>/', post_detail, name='postDetail')  # <------ NEW

]

if settings.DEBUG:  # <------ NEW
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
