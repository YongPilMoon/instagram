from django.http import HttpResponse
from django.contrib.auth import authenticate as auth_authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import View

from member.forms import LoginForm


def login_fbv(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        user = auth_authenticate(
            username=username,
            password=password
        )
        if user is not None:
            auth_login(request, user)
            return redirect('photo:photo_list')
        else:
            return HttpResponse('로그인 실패 하였습니다.')
    else:
        form = LoginForm()
        return render(request, 'member/login.html', {'form': form})


class Login(FormView):
    template_name = 'member/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('photo:photo_list')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = auth_authenticate(
            username=username,
            password=password
        )
        if user is not None:
            auth_login(self.request, user)
        else:
            return HttpResponse('로그인 실패 하였습니다.')
        return super().form_valid(form)


class Logout(View):
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return redirect('photo:photo_list')
    
