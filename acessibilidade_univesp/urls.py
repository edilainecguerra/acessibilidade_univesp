from django.contrib import admin
from django.urls import path
from checklist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('polos/', views.selecionar_polo, name='selecionar_polo'),
    path('questionario/<int:avaliacao_id>/<int:indicador_numero>/', views.questionario, name='questionario'),
    path('resultado/<int:avaliacao_id>/', views.resultado, name='resultado'),
]