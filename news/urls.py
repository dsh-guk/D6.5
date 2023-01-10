from django.urls import path
from .views import (
    NewsList, NewDetail, NewCreate, NewUpdate, NewDelete
)


urlpatterns = [
   path('', NewsList.as_view(), name='new_list'),
   path('<int:id>', NewDetail.as_view(), name='new_detail'),
   path('create/', NewCreate.as_view(), name='new_create'),
   path('<int:pk>/edit/', NewUpdate.as_view(), name='new_edit'),
   path('<int:pk>/delete/', NewDelete.as_view(), name='new_delete')
]