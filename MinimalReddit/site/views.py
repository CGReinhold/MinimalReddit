import praw
from django.shortcuts import render
from django.shortcuts import render_to_response
 
def home(request):
	posts = []
	r = praw.Reddit(user_agent="Get posts")
	for submission in r.get_front_page():
		content = {
			'url' : submission.url,
			'title' : submission.title,
			'permalink' : submission.permalink,
			'num_comments' : submission.num_comments
		}
		posts.append(content)
	
	return render_to_response('index.html', {'posts' : posts})

def sub(request):
	return render_to_response('index.html', {'posts' : getPosts(request.path_info.split('/')[2])})

def getPosts(subreddit):
	posts = []
	r = praw.Reddit(user_agent="Get posts")
	subreddit = r.get_subreddit(subreddit)
	for submission in subreddit.get_hot(limit=10):
		content = {
			'subreddit' : subreddit,
			'url' : submission.url,
			'title' : submission.title,
			'permalink' : submission.permalink,
			'num_comments' : submission.num_comments
		}
		posts.append(content)
	return posts

#Get images test
def subImagesSearch():
	imgs = {".jpg", ".gif", ".png"}
	r = praw.Reddit(user_agent="Select MoviePosterPorn images by movies")
	subreddits = r.get_subreddit("MoviePosterPorn")
	for submission in subreddits.search("Fight Club"):
		if(submission.url[-4:] in imgs):
			print(submission.url)