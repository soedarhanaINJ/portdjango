from django.http import HttpResponse
from django.views import generic
from django.template import loader
from .models import posting

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import ContactForm


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
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            massage = form.cleaned_data['massage']

            html = render_to_string('contact/contactform.html', {
                'name': name,
                'email': email,
                'phone': phone,
                'massage': massage
            })

            send_mail('Contact Form Subjet', 'User send massage', email, ['dangdeurlahir@gmail.com'], html_message=html)

            return redirect('home')
        
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
