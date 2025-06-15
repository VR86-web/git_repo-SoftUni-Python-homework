from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, RedirectView, ListView, FormView, CreateView, UpdateView, DeleteView, \
    DetailView

from forumApp.posts.forms import PostCreateForm, PostDeleteForm, SearchForm, PostEditForm, CommentFormSet
from forumApp.posts.models import Post


#def index(request):

    #context = {
    #    "my_form": "",
    #}

    # return render(request, 'common/index.html', context)


class IndexView(TemplateView):
    template_name = 'common/index.html' # - static way
    extra_context = {
       'static_time': datetime.now(),
     } # - static way

    def get_context_data(self, **kwargs): # dynamic way
        context = super().get_context_data(**kwargs)

        context['dynamic_time'] = datetime.now()

        return context

    def get_template_names(self):
        if self.request.user.is_authenticated: # - dynamic way
            return ['common/index_logged_in.html']
        else:
            return ['common/index.html']


# def dashboard(request):
#    form = SearchForm(request.GET)
#    posts = Post.objects.all()

#    if request.method == "GET":
#        if form.is_valid():
#           query = form.cleaned_data['query']
#            posts = posts.filter(title__icontains=query)

#   context = {
#        "posts": posts,
#        "form": form,
#    }

#    return render(request, 'posts/dashboard.html', context)


class DashboardView(ListView, FormView):
    template_name = 'posts/dashboard.html'
    context_object_name = 'posts'
    form_class = SearchForm
    paginate_by = 2
    success_url = reverse_lazy('dash')
    model = Post

    def get_queryset(self):
        queryset = self.model.objects.all()

        if 'posts.can_approve_posts' not in self.request.user.get_group_permissions() or not self.request.user.has_perm('posts.can_approve_posts'):
            queryset = queryset.filter(approved=True)

        if 'query' in self.request.GET:
            query = self.request.GET.get('query')
            queryset = queryset.filter(title__icontains=query)

        return queryset


# def add_post(request):
#    form = PostCreateForm(request.POST or None, request.FILES or None)

#    if request.method == "POST":
#        if form.is_valid():
#            form.save()
#            return redirect('dash')

#    context = {
#        "form": form,
#    }

#    return render(request, 'posts/add-post.html', context)

def approve_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.approved = True
    post.save()

    return redirect(request.META.get('HTTP_REFERER'))


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/add-post.html'
    success_url = reverse_lazy('dash')


# def edit_post(request, pk: int):
#    post = Post.objects.get(pk=pk)
'''    if request.method == 'Post':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('dash')

    else:
        form = PostEditForm(instance=post)

    context = {
        "form": form,
        "post": post,
    }

    return render(request, 'posts/edit-post.html', context)'''


class EditPostView(UpdateView):
    model = Post
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('dash')

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Post, fields=('title', 'content', 'author', 'language'))
        else:
            return modelform_factory(Post, fields=('content',))


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/details-post.html'

    def get_context_data(self, **kwargs):
        print(PostDetailView.__mro__)
        context = super().get_context_data(**kwargs)
        context['formset'] = CommentFormSet()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        formset = CommentFormSet(request.POST)

        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return redirect('details-post', pk=post.id)

        context = self.get_context_data()
        context['formset'] = formset

        return self.render_to_response(context)


'''def delete_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(instance=post)

    if request.method == "POST":
        post.delete()
        return redirect('dash')

    context = {
        "form": form,
        "post": post,
    }

    return render(request, 'posts/delete-post.html', context)'''


class DeletePostView(DeleteView):
    model = Post
    template_name = 'posts/delete-post.html'
    context_object_name = 'post'
    success_url = reverse_lazy('dash')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        post = Post.objects.get(pk=pk)
        return post.__dict__


class MyRedirectHomeView(RedirectView):
    url = reverse_lazy('index') # - static way

    # def get_redirect_url(self, *args, **kwargs): # dynamic way
    #    pass
