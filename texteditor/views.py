from django.shortcuts import render
from texteditor.models import Editor
from texteditor.forms import EditorForm
# Create your views here.

def data_view(request):
    post_detail = Editor.objects.all()
    context_dict = {'post': post_detail}
    return render(request,'texteditor/data_view.html',context_dict,)


def editor(request):
    if request.method == 'POST':
        form = EditorForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return data_view (request)
        else:
            print (form.errors)
    else:
        form = EditorForm()

    return render(request, 'texteditor/editor.html', {'form':form})