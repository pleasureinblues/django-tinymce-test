from django.shortcuts import render
from texteditor.models import Editor
from texteditor.forms import EditorForm
# Create your views here.

def data_view(request):
    post_detail = Editor.objects.all()
    context_dict = {'post': post_detail}
    return render(request,'texteditor/data_view.html',context_dict,)


def editor1(request):
    print ("checking method")
    if request.method == 'POST':
        print ("method is post")
        form = EditorForm(request.POST)
        print ("before valiation")
        if form.is_valid():
            form.save()
            print ("after valiation")
            return data_view(request)
        else:
            print (form.errors)
    else:
        form = EditorForm()
    return render(request, 'texteditor/editor.html', {'form':form })

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