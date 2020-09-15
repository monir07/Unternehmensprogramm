from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from iden.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('home/<user_name>/', starter_view, name='home'),
    path('compose-iden/<user_shop>/', Compose_iden, name='compose-iden'),
    path('mail-list/<user_shop>/', iden_MailBox, name='mail-list'),
    path('sent-mail/<user_shop>/', SentMail, name='sent-mail'),

    path('plater-shop/', plater_shop, name='plater-shop'),
    path('project_list/', project_list, name='project_list'),
    path('project_detail/', project_detail, name='project_detail'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),



    #
    # # Mail Box Start here...
    # path('mail_box/<user_shop>/', iden_MailBox, name='mail-box'),
    path('iden_pdf/<int:new_iden_id>/', iden_pdf_view, name='show-iden'),
    path('preview/<int:new_preview_id>/', preview_view, name='preview'),
    #

    # login Url.............
    path('accounts/login/', login_vew, name='login'),
    path('logout/', logout_view, name='logout'),

    # Password Reset URL here..........
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_change/$', auth_views.PasswordChangeView.as_view(), name='password_change'),
    url(r'^password/$', change_password, name='change_password'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    # CkTExt Editor
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)