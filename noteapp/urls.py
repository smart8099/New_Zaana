from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeDoneView,PasswordChangeView
from .views import (registerpage,why_zaana,policy,about,createnote,
 delete_note,edit_note,download_note,view_notes, search_note,quotes,CustomLoginView,CustomLogoutView,CustomPasswordChangeView,)
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth import views as auth_views

handler404 = 'noteapp.views.bad_request'

urlpatterns=[

    path('', CustomLoginView.as_view(), name='login'),
    # path('',loginpage,name='login'),
    path('log', CustomLogoutView.as_view(), name='logout'),
    path('register/',registerpage,name='register'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password_change/done/', PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password_reset_confirm/<slug:uidb64>/<slug:token>',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),



    path('why_zaana',why_zaana,name='why'),
    path('policy',policy,name ='policy'),
    path('about',about,name='about'),
    # path('password_reset',password_reset,name='password_reset'),
    path('create_note/', createnote,name='create_note'),
    path('view_notes',view_notes,name='view_note'),
    # path('logout',signout,name='logout'),
    path('<id>/edit_note',edit_note,name='edit_note'),
    path('<id>/delete_note',delete_note,name='delete_note'),
    path('<id>/download_note',download_note,name='download_note'),
    path('search_note',search_note,name='searcher'),
    path('quote_of_the_day',quotes,name='quote'),
    

]