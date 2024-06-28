from django.contrib import admin
from .models import User, PostCategory, Post, Like, Comment


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "post_count")


    class Meta:
        ordering = "name"


    def post_count(self, obj):
        return obj.posts.count()




@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "post_count")
    search_fields = ("name__startswith",)


    class Meta:
        ordering = "name"


    def post_count(self, obj):
        return obj.posts.count()




@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "categories", "created_at", "content")
    search_fields = ("title__startswith",)


    def categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("user").prefetch_related("likes", "categories")


    class Meta:
        ordering = "created_at"




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "posted_by",
        "post",
        "content",
        "created_at",
    )
    search_fields = ("user__email",)


    def posted_by(self, obj):
        return obj.user.name + " - " + obj.user.email


    def post(self, obj):
        return obj.post.title


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("user", "post")


    class Meta:
        ordering = "created_at"
