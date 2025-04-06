from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm


# Create your views here.

def post_view(request):
    post_list = Post.objects.all()
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('post_view')

    context = {
        'post_list': post_list,
        'form': form,
        'title': 'посты',
    }
    return render(request, template_name='main/posts.html', context=context)
