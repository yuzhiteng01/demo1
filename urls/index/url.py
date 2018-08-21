from django.conf.urls import include, url

from app.index import view

urlpatterns = [
    url(r'login/$', view.LoginView.as_view(), name="login"),
    # url(r'save/$', view.testdb),
    # url(r'edit/$', view.testedit),
    # url(r'form_serch/$', view.search_form),
    # url(r'search$', view.search),
]


