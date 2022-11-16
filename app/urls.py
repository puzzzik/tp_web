from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from askme import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view=views.index, name='index'),
    path('hot/', view=views.hot, name='hot'),
    path('ask/', view=views.ask, name='ask'),
    path('question/<int:id>/', view=views.question, name='question'),
    path('settings/', view=views.settings, name='settings'),
    path('login/', view=views.login, name='login'),
    path('registration/', view=views.signup, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
