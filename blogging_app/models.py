from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.name

# CATEGORY_CHOICES = (
#     ("Fashion", "Fashion"),
#     ("Nature", "Nature"),  
#     ("News", "News"),
#     ("Food blogs", "Food blogs"),
#     ("Travel blogs", "Travel blogs"),
#     ("Health and fitness blogs", "Health and fitness blogs"),
# )

class PostCategory(models.Model):
    name =models.CharField(max_length=100)


    class Meta:
        verbose_name="Post Category"
        verbose_name_plural="Post Categories"

    def __ref__(self)->str:
        return self.name

    def __str__(self)->str:

        return self.name    


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(
    PostCategory,related_name="posts",related_query_name="post")
    
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField(max_length=500)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Comment by {self.user.name} on {self.post.title}"

class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="likes", related_query_name="like"
    )

    post = models.ForeignKey(
        Post, related_name="likes", related_query_name="like", on_delete=models.CASCADE
    )

    liked = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)  

    class Meta:
        unique_together = ('user', 'post')  

    def __str__(self):
        return f"{self.user.name} {'liked' if self.liked else 'disliked'} {self.post.title}"
