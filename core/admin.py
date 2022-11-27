from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import Autor, Categoria, Editora, Livro, Usuario


class UsuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "cpf", "telefone", "data_nascimento")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

admin.site.register(Usuario, UsuarioAdmin)

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livro)