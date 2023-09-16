from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView, DetailView, DeleteView

from Petstagram.accounts.models import PetstagramUser
from Petstagram.accounts.forms import PetstagramUserCreateForm, LoginForm, PetstagramUserEditForm
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.


class UserRegisterView(generic.CreateView):
    model = PetstagramUser
    form_class = PetstagramUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    template_name = 'accounts/login-page.html'
    form_class = LoginForm
    next_page = reverse_lazy('homepage')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class UserEditView(UpdateView):
    model = PetstagramUser
    form_class = PetstagramUserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs = {'pk': self.object.pk})


class UserDetailsView(DetailView):
    model = PetstagramUser
    template_name = 'accounts/profile-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_likes_count = sum(p.like_set.count() for p in self.object.photo_set.all())
        total_photos_count = self.object.photo_set.count()
        total_pets_count = self.object.pet_set.count()
        all_of_users_pets = self.object.photo_set.all()

        context.update({
            'total_likes_count': total_likes_count,
            'total_photos_count': total_photos_count,
            'total_pets_count': total_pets_count,
            'all_of_users_pets': all_of_users_pets,
        })
        return context


class UserDeleteView(DeleteView):
    model = PetstagramUser
    template_name = 'accounts/profile-delete-page.html'
    next_page = reverse_lazy('homepage')
    success_url = reverse_lazy('homepage')








