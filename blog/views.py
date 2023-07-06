from django.http import HttpResponse
from django.views import generic
from django.template import loader
from .models import posting


class PostList(generic.ListView):
    queryset = posting.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = posting
    template_name = 'post_detail.html'

def about(request):
    template = loader.get_template('about.html')

    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')

    return HttpResponse(template.render())