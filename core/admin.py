from django.contrib import admin
from .models import Post, Comentario


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("autor", "conteudo_curto", "criado_em")

    def conteudo_curto(self, obj):
        return obj.conteudo[:50]

    conteudo_curto.short_description = "Conteúdo"


# Regista o modelo Comentario no painel de administração
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("autor", "post_id", "conteudo_curto", "criado_em")

    def conteudo_curto(self, obj):
        return obj.conteudo[:50]

    conteudo_curto.short_description = "Conteúdo"
