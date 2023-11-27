from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import generic
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .decorator import allowed_users



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

@login_required(login_url='login')
@allowed_users(allowed_roles=['posters'])
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
@login_required(login_url='login')
@allowed_users(allowed_roles=['posters'])
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
@login_required(login_url='login')
@allowed_users(allowed_roles=['posters'])
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

#Method used to register a user to the web app
def registerPage(request):
   if request.method == 'POST':
       form = CreateUserForm(request.POST)

       if form.is_valid():
           form.save()
           return redirect('index')
    
   else:
       form = CreateUserForm()
    
   context = {'form': form}
   return render(request, 'registration/register.html', context)

#Method used to login the user and authenticate that the user exists
def userLogin(request):
    if request.method == 'POST':
        form = Authenticate(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('index')
    else:
        form = Authenticate()
    
    context = {'form': form}
    return render(request, 'registration/login.html', context)

#Method used to logout the user
def userLogout(request):
    logout(request)
    return redirect('index')

