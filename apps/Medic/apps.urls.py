from oauthlib.uri_validate import path

from . import view

urlpatterns = [
    path('', view.home, name='home'),
    path('about/', view.about, name='about'),
    path('blog/', view.blog, name='blog'),
    path('contact/', view.contact, name='contact'),
]