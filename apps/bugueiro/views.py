from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    # context['cursos'] = Curso.objects.all()
    return render(request, template_name='index.html', context=context)