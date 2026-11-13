from django.contrib import admin
from .models import Recipe,Category



class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_date',)
    search_fields = ('title', 'ingredients', 'instructions')
    list_filter = ('category',)

    def likes_count(self, obj):
        return obj.likes.count()

admin.site.register(Recipe,RecipeAdmin)  
admin.site.register(Category)



