from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import TweetModel
from .forms import TweetForm, UserRegistrationForm

# Create your views here.
def index(request):

    return render(request, 'index.html')


def fetch_all_tweets(request):

    all_tweets_fetched = TweetModel.objects.all().order_by('-created_at')

    return render(request, 'all_tweet_list.html', {
        'all_tweets': all_tweets_fetched
    })


@login_required 
def create_new_tweet(request):

    form = TweetForm()

    if request.method == 'POST':

      form = TweetForm(request.POST, request.FILES)

      if form.is_valid():

          tweet_created = form.save(commit=False)

          tweet_created.user = request.user 

          tweet_created.save()

          return redirect('all_tweets') 

    else:

        form = TweetForm()


    return render(request, 'tweet_form.html', {
        'create_tweet_form': form
    })


@login_required
def edit_particular_tweet(request, tweet_id):

    getting_the_tweet_by_id_that_is_to_be_edited = get_object_or_404(TweetModel, pk=tweet_id, user=request.user)

    form = TweetForm(instance=getting_the_tweet_by_id_that_is_to_be_edited)

    if request.method == 'POST':

        form = TweetForm(request.POST, request.FILES, instance=getting_the_tweet_by_id_that_is_to_be_edited)

        if form.is_valid():

            tweet_created = form.save(commit=False)

            tweet_created.user = request.user 

            tweet_created.save()


            return redirect('all_tweets')
        
        else:

            form = TweetForm(instance=getting_the_tweet_by_id_that_is_to_be_edited)


    return render(request, 'tweet_form.html', {
        'create_tweet_form': form
    })


@login_required
def delete_particular_tweet(request, tweet_id):

    getting_the_tweet_by_id_that_is_to_be_deleted = get_object_or_404(TweetModel, pk=tweet_id, user=request.user)
    
    
    if request.method == 'POST':
        
        getting_the_tweet_by_id_that_is_to_be_deleted.delete()
        
        return redirect('all_tweets')
    
    
    return render(request, 'tweet_delete.html', {
        'tweet_data_to_be_deleted': getting_the_tweet_by_id_that_is_to_be_deleted
    })


def registerNewUser(request):

    form = UserRegistrationForm()

    if request.method == 'POST':
        
        form = UserRegistrationForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(form.cleaned_data['password1'])

            user.save()

            login(request, user)

            return redirect('all_tweets')

    else:
        
        form = UserRegistrationForm()


    return render(request, 'registration/register.html', {
        'form': form
    })