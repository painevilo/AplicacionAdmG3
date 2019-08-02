from django.urls import path, re_path
from . import views 



urlpatterns = [    
    path('', views.home_genial, name='home'),
    path('cliRegistrar/', views.Cliente_Vista.as_view(), name='registro_cliente'),
    path('demRegistrar/', views.Demandante_Vista.as_view(), name='registro_demandate'),
    path('cliListar/', views.Cliente_List.as_view(), name='lista_cliente'),
    path('demListar/', views.Demandante_List.as_view(), name='lista_demandante'),
    re_path(r'^cliEliminar/(?P<id>[0-9]+)/$', views.Cliete_Delete.as_view(), name='eliminar_cliente'),
    re_path(r'^cliRegistrar/(?P<id>[0-9]+)/$',views.Cliente_Update.as_view(), name='update_cliente'),
    re_path(r'^demEliminar/(?P<id>[0-9]+)/$', views.Demandante_Delete.as_view(), name='eliminar_demandante'),
    re_path(r'^demRegistrar/(?P<id>[0-9]+)/$',views.Demandante_Update.as_view(), name='update_demandante'),
    

    
]