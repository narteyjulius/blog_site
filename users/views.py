from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User 
from blog.models import Post
from django.urls import reverse
from .forms import  UserUpdateForm, ProfileUpdateForm


# @login_required
# def profile(request, id):
#     user = User.objects.get(id=id)
#     posts_user = Post.objects.filter(author=request.user)
#     total_post = posts_user.count()

#     # posts_user = posts.filter(user=userme)
#     return render (request, 'users/profile.html', { #'user': user,
#                                                     'total_post': total_post,
#                                                     'posts':posts_user})




@login_required
def profile(request):
    # user = User.objects.get(id=id)
    posts_user = Post.objects.filter(author=request.user)
    total_post = posts_user.count()
    # posts_user = posts.filter(user=userme)
    return render (request, 'users/profile.html', { #'user': user,
                                                    'total_post': total_post,
                                                    'posts':posts_user})



def update_profile(request, id):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance=request.user.profile)

        if u_form.is_valid and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f' Your account has been updated ')
            return redirect ("users:my_profile" )

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
       
    }

    return render(request, "users/edit_profile.html", context )