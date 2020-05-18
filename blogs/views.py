from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from .models import blog
from .forms import CommentForm

def BlogDetailView(request, pk):
    if 'search' in request.GET:
        q = ''
        if 'search' in request.GET:
            print("p")

            q = request.GET['search']
            blog_set = blog.objects.all().filter(title__icontains=q).distinct()

            context = {
                'blog_set' : blog_set
            }

            return render(request, 'blog/list.html', context)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.Blog = get_object_or_404(blog, pk=pk)
            context = {
                'form' : form
            }
            form.save()
            print(form)
            return redirect(reverse('detail', kwargs={
                'pk' : pk
            }))
        else:
            form = CommentForm()
    blog_pk = get_object_or_404(blog, pk=pk)
    context = {
        'blog' : blog_pk,
        'form' : form
    }

    print(blog_pk.Comment)
    return render(request, 'blog/blog-detail.html', context)


