from django.shortcuts import render, redirect
from .models import Travels
from .forms import TravelsForm


# Create your views here.
def index(request):
    travels = Travels.objects.all()
    context = {
        'travels':travels,
    }
    return render(request, 'travels/index.html', context)

def create(request):
    # 요청 메서드가 POST라면 (create)
    if request.method == 'POST':
        form = TravelsForm(request.POST)
        # 유효성 검사 진행
        # 유효성 검사가 통과된 경우
        if form.is_valid():
            travel = form.save()
            return redirect('travels:detail', travel.pk)
    # 요청 메서드가 POST가 아니라면 (new)
    else:
        form = TravelsForm()
    context = {
        'form': form,
    }
    return render(request, 'travels/create.html', context)

def detail(request, pk):
    travel = Travels.objects.get(pk=pk)
    context ={
        'travel':travel,
    }
    return render(request, 'travels/detail.html', context)

def delete(request, pk):
    travel = Travels.objects.get(pk=pk)
    travel.delete()
    return redirect('travels:index')

def update(request, pk):
    travel = Travels.objects.get(pk=pk)
    # 요청의 메서드가 POST라면(update)
    if request.method == 'POST':
        form = TravelsForm(request.POST, instance=travel)
        if form.is_valid():
            form.save()
            return redirect('travels:detail', travel.pk)
    # 요청의 메서드가 POST가 아니라면(edit)
    else:
        form = TravelsForm(instance=travel)
    context = {
        'travel': travel,
        'form': form,
    }
    return render(request, 'travels/update.html', context)