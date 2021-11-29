from django.views.generic import TemplateView, ListView, DetailView

from pages.models import Post

class HomePageView(TemplateView):
    template_name="index.html"

class AboutPageView(TemplateView):
    template_name="about.html"

class PostListView(ListView):
    model=Post
    template_name="post_list.html"


class PostDetailView(DetailView):
    model= Post
    template_name ="post_detail.html"