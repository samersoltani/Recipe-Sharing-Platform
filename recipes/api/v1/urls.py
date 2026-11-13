from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register('',views.RecipeListApiView,basename='list')
router.register('detail',views.RecipeDetailApiView,basename='detail')
urlpatterns = router.urls + [
    path('like/<int:pk>/', views.Like.as_view(), name='Like')
]

# urlpatterns = [
#     # path('',views.RecipeListApiView.as_view(),name='list-api'),
#     # path('detail/<int:pk>/',views.RecipeDetailApiView.as_view(),name='detail-api'),
#     # # path('',views.recipes_list_api, name='recipes_list_api'),
#     # # path('detail/<int:pk>/',views.recipe_detail_api, name='recipe_detail_api'),
# ]



