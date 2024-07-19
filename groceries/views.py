from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Grocery
from django.http import HttpResponseRedirect
from django.http import HttpResponse


class IndexView(generic.ListView):
    template_name = 'groceries/index.html'
    context_object_name = 'grocery_list'

    def get_queryset(self):
        """Return all the latest groceries."""
        return Grocery.objects.order_by('-created_at')

def add(request):
    title = request.POST['title']
    Grocery.objects.create(title=title)

    return redirect('groceries:index')

def delete(request, grocery_id):
    grocery = get_object_or_404(Grocery, pk=grocery_id)
    grocery.delete()

    return redirect('groceries:index')

def test_message(request):
     groceryList = Grocery.objects.all()
     data = list(groceryList.values('title'))
     return HttpResponse(data)

def update(request, grocery_id):
    grocery = get_object_or_404(Grocery, pk=grocery_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    
    grocery.isCompleted = isCompleted

    grocery.save()
    return redirect('groceries:index')