import pytest
from ..models import Recipe,Category
from django.contrib.auth.models import User




""" Model Tests - Recipe

1. Review of Successful Recipe Creation
2. Check if the Recipe is saved in the database using get()
3. Check the validity of the title value
4. Check the accuracy of the description value
5. Checking the correctness of the Recipe connection with the User (author)
6. Check the correctness of the Recipe connection with the Category
7. Checking the possibility of creating a Recipe without a Category
8. Check if category is None in Recipe without category
9. Check if category is None after retrieving Recipe from database

"""


@pytest.fixture
def create_user():
    user = User.objects.create_user(username='test',password='test123456')
    return user



@pytest.mark.django_db
class TestModel():

    def test_create_model_Information(self,create_user):
        category_obj = Category.objects.create(name='test-category-model')

        recipe = Recipe.objects.create(
            author = create_user,
            title = 'test-model',
            description = 'description-model',
            ingredients = 'ingredients-model',
            instructions = 'instructions-model',
            category = category_obj,
        )
        
        saved_recipe = Recipe.objects.get(id=recipe.id)
    
        assert saved_recipe == recipe
        assert recipe.category == category_obj
        assert recipe.title == 'test-model'
        assert recipe.description == 'description-model'
        assert recipe.author == create_user
        

    def test_recipe_without_category(self,create_user):
        recipe = Recipe.objects.create(
            author = create_user,
            title = 'test-model',
            description = 'description-model',
            ingredients = 'ingredients-model',
            instructions = 'instructions-model',
            category = None,
        )
        saved_recipe = Recipe.objects.get(id=recipe.id)
        assert recipe.category is None
        assert saved_recipe.category is None
