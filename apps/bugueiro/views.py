from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    context = {}
    # context['cursos'] = Curso.objects.all()
    return render(request, template_name='index.html', context=context)


@login_required
def dashboard(request):
    context = {}
    return render(request, template_name='dashboard.html', context=context)