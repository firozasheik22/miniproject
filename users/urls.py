
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# Create your views here.

urlpatterns=[
    path('added/<int:id>',views.added,name="added"),
    path('history',views.history,name="history"),
    path('change_donor_password',views.change_donor_password,name="change_donor_password"),
    path('update_donor',views.update_donor,name="update_donor"),
    path('donor_profile',views.donor_profile,name="donor_profile"),

    path('change_volunteer_password',views.change_volunteer_password,name="change_volunteer_password"),
    path('change_volunteer_id',views.change_volunteer_id,name="change_volunteer_id"),

    path('update_volunteer',views.update_volunteer,name="update_volunteer"),
    path('volunteer_profile',views.volunteer_profile,name="volunteer_profile"),

    path('home_check',views.home_check,name="home_check"),
    path('login',views.login,name="login"),
    path('check_id',views.check_id,name="check_id"),
    path('check_id_status',views.check_id_status,name="check_id_status"),
    path('donate',views.donate,name="donate"),
    path('receive',views.receive,name="receive"),
    path('single/<int:id>', views.single, name='single'),
    path('view_all/<str:type>',views.view_all,name='view_all'),
    path('donor_login',views.donor_login,name="donor_login"),
    path('volunteer_login',views.volunteer_login,name="volunteer_login"),
    path('donor_register',views.donor_register,name="donor_register"),
    path('volunteer_register',views.volunteer_register,name="volunteer_register"),
    path('donor_register_check',views.donor_register_check,name="donor_register_check"),
    path('volunteer_register_check',views.volunteer_register_check,name="volunteer_register_check"),
    path('donor_login_check',views.donor_login_check,name="donor_login_check"),
    path('volunteer_login_check',views.volunteer_login_check,name="volunteer_login_check"),
    path('donor_main',views.donor_main,name="donor_main"),
    path('volunteer_main',views.volunteer_main,name="volunteer_main"),
    path('logout',views.logout,name="logout"),
    path('donate_item',views.donate_item,name="donate_item"),
    path('post_item',views.post_item,name="post_item"),
    path('post',views.post,name="post"),
    path('all_posts',views.all_posts,name="all_posts"),
    path('all_donations',views.all_donations,name="all_donations"),
    path('all_receptions',views.all_receptions,name="all_receptions"),
    path('view_posts',views.view_posts,name="view_posts"),
    path('view_all_posts/<str:type>',views.view_all_posts,name="view_all_posts"),
    path('single_post/<int:id>',views.single_post,name="single_post"),
    path('added_post/<int:id>',views.added_post,name="added_post"),
    #path('forgot_password',views.forgot_password,name="forgot_password"),

    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='change-password.html',
            success_url = '../change-password-success'
        ),
        name='change_password'
    ),
    path('change-password-success',views.change_password_success,name="change-password-success"),



    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html',
             subject_template_name='password_reset_subject.txt',
             email_template_name='password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),
]

