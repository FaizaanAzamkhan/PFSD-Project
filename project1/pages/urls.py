from django.urls import path,include
from .views import home,aboutus,register,login,intro,emptyroom,services,RR,facilities


urlpatterns = [
    path('',home,name='hm'),
    path('aboutus',aboutus,name='ab'),
    path('register/',register,name='reg'),
    path('login',login,name='lg'),
    path('intro',intro,name='in'),
    path('emptyroom',emptyroom,name='er'),
    path('services',services,name='ser'),
    path('RR',RR,name='rr'),
    path('facilities',facilities,name='fac'),

]