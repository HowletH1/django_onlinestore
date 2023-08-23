from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from blog.models import Blog


class BlogCreate(CreateView):
    model = Blog
    fields = ('title', 'content', 'is_published')
    success_url = reverse_lazy('blog:list')


class BlogUpdate(UpdateView):
    model = Blog
    fields = ('title', 'content', 'is_published')
    success_url = reverse_lazy('blog:list')

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogList(ListView):
    model = Blog
    fields = ('title', 'content')


class BlogDetail(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')

