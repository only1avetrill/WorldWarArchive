from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('docs/', views.Docs, name='docs'),
    path('docs/<int:pk>/', views.DocsDetailView.as_view(), name='docs-detail'),
    path('docs/sort/<slug:sort_slug>', views.SortDocs, name='sort-docs'),
    path('delete-docs/<int:id>/ ', views.DeleteDocs, name='delete-docs'),
]

handler404 = "main.views.page_not_found_view"
handler500 = "main.views.server_error_view"

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)