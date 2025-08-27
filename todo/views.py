from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import TodoForm
from .models import Todo


def index(request):
    item_list = Todo.objects.order_by("-date")

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New Q&A added successfully!")
            return redirect('todo')
    else:
        form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }

    return render(request, 'todo/index.html', page)


def remove(request, item_id):
    item = get_object_or_404(Todo, id=item_id)
    item.delete()
    messages.info(request, "Item removed!")
    return redirect('todo')
