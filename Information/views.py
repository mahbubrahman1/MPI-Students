from django.shortcuts import render, HttpResponseRedirect
from Information import forms
from Information.models import Student


# add new item and show data
def display_and_add(request):
    form = forms.StudentForm()
    
    if request.method == "POST":
        form = forms.StudentForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            form = forms.StudentForm()
        
    else:
        form = forms.StudentForm()

    student = Student.objects.all()

    info = {
        'form': form,
        'students': student
    }
    return render(request, 'info/display_and_add_data.html', context=info)


# update or edit data
def update(request, id):
    if request.method == "POST":
        id_num = Student.objects.get(pk=id)
        form = forms.StudentForm(request.POST, instance=id_num)

        if form.is_valid():
            form.save(commit=True)
    
    else:
        id_num = Student.objects.get(pk=id)
        form = forms.StudentForm(instance=id_num)

    return render(request, 'info/update_data.html', {'form': form})


# delete data
def delete(request, id):
    if request.method == "POST":
        id_num = Student.objects.get(pk=id)
        id_num.delete()

        return HttpResponseRedirect('/')