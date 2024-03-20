from django.contrib import admin

from dogs.models import DogsTable

#admin.site.register(DogsTable)
#admin.site.register(DogsProperty)

@admin.register(DogsTable)
class DogsTableAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('breed',)}
