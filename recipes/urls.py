from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import RecipesListView,RecipeDetailView,RecipeCreateView,RecipeUpdateView,RecipeDeleteView,LoginRequiredMixin,LikeRecipeView

app_name = 'recipes'

urlpatterns = [
    path('',RecipesListView.as_view(), name='recipes_list'),
    path('detail<int:pk>/',RecipeDetailView.as_view(), name='recipe_detail'),
    path('create/',RecipeCreateView.as_view(), name='recipe_create'),
    path('update<int:pk>/',RecipeUpdateView.as_view(), name='recipe_update'),
    path('delete<int:pk>/',RecipeDeleteView.as_view(), name='recipe_delete'),
    path('like<int:pk>/',LikeRecipeView.as_view(), name='like_recipe'),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)