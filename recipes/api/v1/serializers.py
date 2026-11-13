from rest_framework import serializers
from recipes.models import Recipe,Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta :
        model = Category
        fields = ['id','name'] 



class RecipeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source ="author.username")
    snippet = serializers.SerializerMethodField()
    absolute_url = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    class Meta :
        model = Recipe
        fields = ['author','title','description','snippet','image','ingredients','instructions','category','absolute_url','likes_count','updated_date']
        read_only_fields = ['author']



    def get_likes_count(self, obj):
        return obj.likes.count()



    def validate_title(self, value):
        if value.strip():
            return value
        raise serializers.ValidationError('The value cannot be empty') 





    def validate_description(self,value):
        if len(value) < 20 :
            raise serializers.ValidationError('The description length is less than 20')
        return value





    def validate_ingredients(self , value):
        if value.strip():
            return value 
        raise serializers.ValidationError('The ingredients cannot be empty') 






    def validate(self, attrs):
        title_name =attrs.get('title')
        des_name = attrs.get('description')
        if title_name == des_name :
            raise serializers.ValidationError('The title and description must not be the same')
        return attrs





    def get_absolute_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/recipes-api/detail/{obj.pk}/')
    




        
    def get_snippet(self,obj):
        snippet = obj.description
        return snippet[0:10]



                

    def to_representation(self,instance):
        rep = super().to_representation(instance)  
        rep ['category'] = CategorySerializer(instance.category).data
        return rep   

    