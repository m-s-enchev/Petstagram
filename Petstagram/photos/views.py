from django.shortcuts import render, redirect

from Petstagram.common.forms import CommentForm
from Petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from Petstagram.photos.models import Photo


# Create your views here.


def photo_add(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('homepage')
    context = {
        'form': form
    }

    return render(request, template_name='photos/photo-add-page.html', context=context)


def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    comment_form = CommentForm()
    photo_is_liked_by_user = likes.filter(user=request.user)
    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'comment_form': comment_form,
        'photo_is_liked_by_user': photo_is_liked_by_user
    }
    return render(request, template_name='photos/photo-details-page.html', context=context)


def photo_edit(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == 'GET':
        form = PhotoEditForm(instance=photo, initial=photo.__dict__)
    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo-details', pk)
    context = {'form': form}
    return render(request, template_name='photos/photo-edit-page.html', context=context)


def photo_delete(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('homepage')

