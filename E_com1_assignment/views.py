from django.shortcuts import render
from .models import Category

def list_categories(request):
    categories = Category.objects.all()
    # Assuming you want to display the categories on a web page
    return render(request, 'categories.html', {'categories': categories})

# This will not be executed directly in production code, but for debugging:
def print_list_category():
    categories = Category.objects.all()
    for category in categories:
        print(category)

# You can call this function here to see the output in the console when the server starts
print_list_category()