from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import generic

# Create your views here.
def index(request):
    return render( request, 'nba_forum/index.html')

#Classes that use generics to build the list and detail view
class TeamsListView(generic.ListView):
    model = Team
class TeamsDetailView(generic.DetailView):
    model = Team

    #def get_context_data to send additional variables to template
    def get_context_data(self, **kwargs):

        # Call the base implementation first to get the context for the current portfolio
        context = super(TeamsDetailView, self).get_context_data(**kwargs)

        #Grabs the posts that use the current team to use for the context
        context['post'] = Post.objects.filter(team=context['team'])
        return context


#Classes that use generics to build the list and detail view
class PostsListView(generic.ListView):
    model = Post
class PostsDetailView(generic.DetailView):
    model = Post


def createPost(request, team_id):

    form = PostForm()
    teams = Post.objects.get(pk=team_id)
    
    if request.method == 'POST':
        
        form = PostForm(request.POST)

        if form.is_valid():
            #Save the form without committing to the database
            post = form.save(commit=False)
            #Set the objects relationship
            post.teams = teams
            post.save()

            #Redirect back to the team detail page
            return redirect('team-detail', team_id)

    context = {'form': form}
    return render(request, 'nba_forum/post_form.html', context)

#Method to update a post in a team page
def updatePost(request, team_id, id):
    #Sets the team based on the id from the url
    teams = Team.objects.get(pk=team_id)
    #Sets the post based on the id from the url
    post = Post.objects.get(id = id)
    #Generates a post form using the current instance
    form = PostForm(instance = post)
    
    if request.method == 'POST':
        
        #Generates a post form using the current instance of the post and trys to post the updated information
        form = PostForm(request.POST, instance = post)

        if form.is_valid():
            # Save the form without committing to the database
            post = form.save(commit=False)
            # Set the objects relationship
            post.teams = teams
            post.save()

            # Redirect back to the team detail page
            return redirect('team-detail', team_id)

    context = {'form': form}
    return render(request, 'nba_forum/post_form.html', context)

#Method to delete a post from a team page
def deletePost(request, team_id, id):

    #Sets the post based on the id from the url
    post = Post.objects.get(id = id)

    #check the method is as expected
    if request.method == 'POST':
        #Delete the project using delete function
        post.delete()
        #Redirect back to the team list page
        return redirect('team-detail', team_id)

    context = {'item': post}
    return render(request, 'nba_forum/delete.html', context)
