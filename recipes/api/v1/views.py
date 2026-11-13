from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from .serializers import RecipeSerializer
from ...models import Recipe
from rest_framework import generics
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .pagination import CustomPagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework import status




class RecipeListApiView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields = ['category','author','title']
    filterset_fields = ['category','author']
    ordering_fields = ['created_date']
    pagination_class = CustomPagination
    
    def perform_create(self,serializer):
        serializer.save(author=self.request.user)     
        


class RecipeDetailApiView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    

class Like(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        recipe = get_object_or_404(Recipe,pk=pk)
        recipe.likes.add(request.user)
        return Response('Your like was successful')


# @api_view(['GET','POST'])
# @permission_classes([IsAuthenticatedOrReadOnly])
'''def recipes_list_api(request):
    if request.method == 'GET':
        recipe_list = Recipe.objects.all()
        serializer = RecipeSerializer(recipe_list, many=True) 
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serialize = RecipeSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save(author=request.user)
            return Response(data=serialize.data,status=status.HTTP_201_CREATED)
        return Response(data=serialize.errors,status=status.HTTP_400_BAD_REQUEST)

'''

# @api_view(['GET','PUT','DELETE'])
# @permission_classes([IsAuthenticatedOrReadOnly])
'''def recipe_detail_api(request,pk):
    if request.method == 'GET':
        recipe = get_object_or_404(Recipe, pk=pk)
        serializer = RecipeSerializer(recipe)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        recipe = get_object_or_404(Recipe, pk=pk)
        serialize = RecipeSerializer(recipe,data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(data=serialize.data,status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        recipe = get_object_or_404(Recipe, pk=pk)
        recipe.delete()
        return Response({'detail':'Recipe deleted successfully'},status=status.HTTP_200_OK)'''