from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#function base view
def home(request):
	dummy = {
	'posts':Post.objects.all()
	}
	return render(request,"blog/home.html",dummy)
#class based view
class PostListView(ListView):
	model = Post
	template_name="blog/home.html"
	context_object_name ='posts'
	ordering = ['date_posted']


def about(request):
	return render(request,"blog/about.html")

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title','content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title','content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	# to keep chekc if the post is the author who is changing
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			False
