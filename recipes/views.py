from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import RecipeForm
from .models import Recipe
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.views import View



class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'
    context_object_name = 'recipe_list'
    paginate_by = 3


    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q :
            queryset = queryset.filter(Q(title__icontains=q) | Q(description__icontains=q))
        return queryset

 


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'




class RecipeCreateView(LoginRequiredMixin,CreateView):
    model = Recipe
    template_name = 'recipes/recipe_create.html'
    form_class = RecipeForm
    success_url = reverse_lazy('recipes:recipes_list')


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class RecipeUpdateView(UserPassesTestMixin,UpdateView):
    model = Recipe
    template_name = 'recipes/recipe_update.html'
    context_object_name = 'recipe'
    form_class = RecipeForm
    success_url = reverse_lazy('recipes:recipes_list')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author
    
    def form_valid(self, form):
        if not form.cleaned_data.get('image') and self.get_object().image:
            form.instance.image = self.get_object().image
        return super().form_valid(form)



class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_delete.html'
    context_object_name = 'recipe'
    success_url = reverse_lazy('recipes:recipes_list')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author



class LikeRecipeView(LoginRequiredMixin,View):

   def post(self,request, *args, **kwargs) :
        recipe = get_object_or_404(Recipe, pk=kwargs['pk'])

        if recipe.likes.filter(pk=request.user.pk).exists():
           recipe.likes.remove(request.user)

        else : 
           recipe.likes.add(request.user)

        return redirect('recipes:recipe_detail', pk=recipe.pk)