from django.shortcuts import render
from django.http import HttpResponse
from . models import Post 


posts = [
	{
		'author':"Mark",
		'title':"Blog 1",
		'content':"First blog",
		'date_posted':"Aug 25 2020"
	},
	{
		'author':"Jude",
		'title':"Blog 2",
		'content':"Second blog",
		'date_posted':"Sep 25 2020"
	}
]

def home(request):
	data = {
		'posts':Post.objects.all()
	}
	return render(request,'blog/home.html',data)


def about(request):
	data = {
		'title':"About Blog"
	}
	return render(request,'blog/about.html',data)

