from rest_framework.test import APIClient
from django.urls import reverse
from ..models import Recipe
from django.contrib.auth.models import User
import pytest



"""
    1. Verify that the request was successful (Status Code 200) ✅
    2. Verify the accuracy of the title of the first recipe ✅
    3. Verify the accuracy of the title of the second recipe ✅
    4. Verify the number of returned recipes ✅
    5. Verify that the 'results' list is empty ✅
    6. Verify the presence of the 'results' key in the response ✅
    7. Verify the presence of the 'next' key within 'links' ✅
    8. Verify the presence of the 'previous' key within 'links' ✅
    9. Verify that 'total_count' is zero when the list is empty ✅
"""



@pytest.fixture
def api_client():
    clint = APIClient()
    return clint


@pytest.fixture
def create_user():
    user = User.objects.create_user(username= 'samer', password= '123')
    return user




@pytest.fixture(scope="function")
def two_recipes(create_user):

    recipe1 = Recipe.objects.create(
        author=create_user,
        title='test1',
        description='description',
        ingredients='ingredients',
        instructions='instructions',
    )

    recipe2 = Recipe.objects.create(
        author=create_user,
        title='test2',
        description='description2',
        ingredients='ingredients2',
        instructions='instructions2',
    )

    return [recipe1, recipe2]



@pytest.mark.django_db
class TestRecipeApi:

    def test_recipe_list_api_returns_200(self,api_client,two_recipes):
        
        url = reverse('api:list-list')
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data['results'][0]['title'] == two_recipes[0].title
        assert response.data['results'][1]['title'] == two_recipes[1].title
        assert len(response.data['results']) == len(two_recipes)



    def test_recipe_list_empty_api_returns_200(self,api_client):
            
            url = reverse('api:list-list')
            response = api_client.get(url)
            assert response.status_code == 200
            assert response.data['results'] == []
            assert 'results' in response.data 
            assert 'next' in response.data['links']
            assert 'previous' in response.data['links']
            assert response.data['total_count'] == 0



            