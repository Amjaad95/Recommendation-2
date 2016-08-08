from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Recommendation, Profile , Category , Comment
from django.contrib.auth.models import User
from .forms import RecommendationForm
from django.db.models import Count
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authentiated():
        pass

@login_required
def timeline(request):
    latest_recommendation = Recommendation.object.all().order_by('submission_date')[:20]
    context = {'latest_recommendation': latest_recommendation}
    return render(request, context)

@login_required
def recommendations_page(request):
    profile = get_object_or_404(Profile, username=User)
    category = get_object_or_404(Category, username=User)
    context ={'profile': profile,
              'category': category}
    return render(request, 'recommendation/base.html', context)

@login_required
def explore(request):
    most_popular = Recommendation.objects.annotate(comment_count=Count('comment')).filter(comment_count__gt=5).order_by('?')
    context = {'most_popular': most_popular}
    return render(request, context)

@login_required
def search(request):
    Recommendation.objects.filter(description__icontains=term)


@login_required
def list_followers(request):
    pass

@login_required
def list_following(request, User):
    pass

@login_required
def add_recommendation(request):

        if request.method == 'POST':

            form = RecommendationForm(request.POST, request.FILES)
            instance = Recommendation(user= request.user,
                                      date= request.submission_date)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/success/url/') #??

        elif request.method == 'GET':
            form = RecommendationForm()

            context = {'form': form}
            return render(request, context)
@login_required
def recommendation(request, recommendation_id):
    recommendation_page= get_object_or_404(Recommendation, recommendation_id)
    context= {'recommendation' : recommendation_page}
    return render(request, context)

