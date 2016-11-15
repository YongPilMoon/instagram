from django.conf.urls import url
from ..views import login_fbv, Login, Signup,Logout


urlpatterns = [
    url(r'login/$', login_fbv, name='login_fbv'),
    url(r'login/class/$', Login.as_view(), name='login_cbv'),
    url(r'signup/$', Signup.as_view(), name='signup'),
    url(r'logout/class/$', Logout.as_view(), name='logout_cbv'),
]
