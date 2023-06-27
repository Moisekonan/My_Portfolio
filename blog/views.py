from django.shortcuts import get_object_or_404, render

from .models import Blog

def detail_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail_blog.html', locals())