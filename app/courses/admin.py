from django.contrib import admin

from .models import Course, Module, Subject


@admin.register(Subject)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ['id', 'title', 'slug']


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']

    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
