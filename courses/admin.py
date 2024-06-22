from django.contrib import admin
from courses.models import Course,Categories

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","slug","category_list")
    list_display_links = ("title","slug")
    readonly_fields = ("slug",)
    list_filter = ("isActive","categories")
    list_editable = ("isActive",)
    search_fields = ("title","description")

    def category_list(self,obj):
        html =""
        for category in obj.categories.all():
            html += category.name +", "
        return html
    

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display=("name","slug","course_count")
    readonly_fields = ("slug",)

    def course_count(self,obj):
        return obj.course_set.count()



