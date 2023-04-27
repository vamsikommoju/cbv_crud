from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [ 
    path('update/<int:id>',views.update.as_view(),name='update'),
    path('delete/<int:id>',views.delete.as_view(),name='delete')
]