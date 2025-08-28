from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from prometheus_client import start_http_server, Summary, Counter, Gauge, make_wsgi_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('apps.urls')),

]

from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class MetricsMiddleware(MiddlewareMixin):
    def __call__(self, request):
        return self.get_response(request)


def metrics_view(request):
    from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
    return HttpResponse(generate_latest(), content_type=CONTENT_TYPE_LATEST)


urlpatterns += [
    path("metrics/", metrics_view),
]
