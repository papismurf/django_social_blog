from django.views.generic import ListView


from .models import Posts


class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Posts
    context_object_name = 'posts'
