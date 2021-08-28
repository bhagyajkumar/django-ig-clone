from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post, Profile
from django.views.decorators.csrf import csrf_exempt


def home_page(request):
    posts = Post.objects.all().prefetch_related('images')
    like_data = {}
    for post in posts:
        like_data[post.id] = (post.likes.filter(id=post.id) is not None)

    return render(request, "main.html", {'posts': posts, 'like_data': like_data})


def ajax_like(request):
    if request.is_ajax():
        post_id = request.POST["post_id"]
        post = Post.objects.get(pk=post_id)
        likes = post.likes.filter(id=request.user.id)
        if len(likes) == 0:
            post.likes.add(request.user)
            return JsonResponse(
                {
                    'post_id': post_id,
                    'status': 1,
                    'total': post.likes.count()
                }
            )
        else:
            post.likes.remove(request.user)
            return JsonResponse(
                {
                    'post_id': post_id,
                    'status': 0,
                    'total': post.likes.count()
                }
            )


def profile(request):
    user = request.user
    profile = Profile.objects.filter(user=user).first()
    posts = Post.objects.filter(user=user).all().prefetch_related('images')
    context = {
        'user': user,
        'profile': profile,
        'posts': posts
    }
    return render(request, 'profile.html', context=context)
