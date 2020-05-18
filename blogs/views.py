from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from .models import blog

def BlogDetailView(request, pk):
    # model = blog
    # template_name = 'blog/blog-detail.html'
    # context_object_name = 'blog'
    # def get(self, request, **kwargs):
    if 'search' in request.GET:

        # return redirect(reverse('find'), kwargs={'search':request.GET.search})
        print("p")
        q = ''
        context = {}
        if 'search' in request.GET:
            print("p")

            q = request.GET['search']
            blog_set = blog.objects.all().filter(title__icontains=q).distinct()

            context = {
                'blog_set' : blog_set
            }

            return render(request, 'blog/list.html', context)
    blog_pk = get_object_or_404(blog, pk=pk)
    # return Blog
    print(blog_pk)
    context = {
        'blog' : blog_pk
    }
    print(context['blog'])

    return render(request, 'blog/blog-detail.html', context)


def find(request):
    if 'search' in request.GET:
        print("p")
        q = ''
        context = {}
        if 'search' in request.GET:
            print("p")

            q = request.GET['search']
            blog_set = blog.objects.all().filter(content__icontains=q)
            print(blog_set)
            print(blog_set)
            context = {
                'blog_set' : blog_set
            }

            return render(self.request, 'blog/list.html', context)