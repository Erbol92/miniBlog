from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm


# Create your views here.

def post_view(request):
    post_list = Post.objects.all()
    post_form = PostForm(request.POST or None)
    comment_form = CommentForm()
    if post_form.is_valid():
        post_form.save()
        return redirect('post_view')
    context = {
        'post_list': post_list,
        'post_form': post_form,
        'comment_form': comment_form,
        'title': 'посты',
    }
    return render(request, template_name='main/posts.html', context=context)

def add_comment(request, post_id: int):
    comment_form = CommentForm(request.POST)
    post = Post.objects.get(id=post_id)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect('post_view')
