from django.contrib import admin
from . models import Post, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') # campos de solo lectura
    list_display = ('title','author', 'published','post_categories') # mostrar en listado, para relaciones manytomany crear nuestro propio campo, ver(post_categories)
    ordering = ('author', 'published')#ordenar
    search_fields = ('title', 'content', 'author__username', 'categories__name')#campos de busqueda, acordarse de que cuando tienen relacion buscar con __
    date_hierarchy = ('published')#Hace jerarquia de fechas
    list_filter = ('author__username',)#LISTA DE FILTRADO POR AUTOR, SE UTILIZA SIEMPRE CON RELACIONES

    def post_categories(self, obj):
        return ", ".join(c.name for c in obj.categories.all().order_by('name'))
    
    post_categories.short_description = "Categorias"




admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

