from django.urls import include, path

from cats.views import APICat, APICatDetail, CatList, CatDetail

urlpatterns = [
   path('cats/', APICat.as_view()),
   path('cats/<int:pk>/', APICatDetail.as_view()),
   path('cats-generic/', CatList.as_view()),
   path('cats-generic/<int:pk>/', CatDetail.as_view()),
]


