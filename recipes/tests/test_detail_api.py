from rest_framework.test import APIClient
from django.urls import reverse
from ..models import Recipe
from django.contrib.auth.models import User
import pytest



@pytest.fixture
def api_clint():
    clint = APIClient()
    return clint



@pytest.fixture
def create_user():
    user = User.objects.create_user(username= 'samer', password= '123')
    return user


@pytest.fixture(scope="function")
def recipes(create_user):

    recipe1 = Recipe.objects.create(
        author= create_user,
        title='test1',
        description='description',
        ingredients='ingredients',
        instructions='instructions',
    )
    return recipe1


@pytest.mark.django_db

class TestDetailApi():

    def test_recipe_detail_api_status_code_200(self,api_clint,recipes):
        
        url = reverse('api:detail-detail',args=[recipes.id])
        response = api_clint.get(url)
        assert response.status_code == 200
        assert response.data['title'] == recipes.title
        assert response.data['description'] == recipes.description
        assert response.data['author'] == recipes.author.username
        

    def test_recipe_detail_status_code_404(self,api_clint,recipes):
        url = reverse('api:detail-detail',args=[recipes.id + 1])
        response = api_clint.get(url)
        assert response.status_code == 404 

        