from django.shortcuts import render
from django.http import HttpResponse

posts = [
		{
			"title":"Blog-1",
			"author": "Matt",
			"content":"First blog post",
			"date_posted":"Jun 01, 2020"
		},
		{
			"title":"Blog-2",
			"author": "Tony",
			"content":"Second blog post",
			"date_posted":"Mar 11, 2020"
		}

]

def home(request):
	dummy = {
	'posts':posts
	}
	return render(request,"blog/home.html",dummy)

def about(request):
	return render(request,"blog/about.html")