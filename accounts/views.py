from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('recipes:recipes_list')



class MyLoginView(auth_views.LoginView):
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'


    def get_success_url(self):
        return reverse_lazy('recipes:recipes_list')
    
    def form_invalid(self, form):
        messages.error(self.request,'The information entered is not valid. Please try again.')
        return self.render_to_response(self.get_context_data(form=form))



class MyLogoutView(auth_views.LogoutView):
    template_name = 'accounts/logout.html'
   


class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name_email = 'templates/registration/password_reset_email.html'
    template_name = 'templates/registration/password_reset_from.html'
    success_url = reverse_lazy('recipes:recipes_list')



class MyProfileView(LoginRequiredMixin,View):

    def get(self, request):
        profile,created = Profile.objects.get_or_create(
            user=request.user
        )
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)
        
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'accounts/profile.html', context)
    
    def post(self, request):
        profile, created = Profile.objects.get_or_create(
            user=request.user
        )

        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(
                request,
                'Your profile has been updated successfully'
            )

            return redirect('accounts:profile')

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        messages.error(request, 'Error updating your profile')

        return render(request, 'accounts/profile.html', context)