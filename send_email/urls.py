
""" 
App (send_email) Urls 
-Title: Set Customized Urls
-Details: This will storages all urls from the app: send_email
-Version: 0.1.0
-Autor: Sergio Enmanuel González
"""

from pathlib import Path
from django.urls import path 
from . import views


#Let's creates the customized urls within app(send_email).
urlpatterns = [
    path('',views.index, name='index_page'),
    path('reqs',views.reqs, name='requirements'),
    path('install',views.installation, name='installation'),
    path('release_notes',views.release_notes, name='release_notes'),
    path('example',views.example, name='example'),
     path('email_template',views.show_email_template, name='email_template'),
    path('send_email',views.send_email),
    path('<str:email_from>',views.send_email),
 

]
