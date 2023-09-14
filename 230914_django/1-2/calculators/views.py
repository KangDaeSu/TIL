from django.shortcuts import render

# Create your views here.
def calculation(request):
    return render(request, 'calculators/calculation.html')

def result(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    res = int(num1) * int(num2)
    res1 = int(num1) - int(num2)
    if num2 != '0':
        res2 = int(num1) / int(num2)
    else:
        res2 = False
    context = {
        'num1':num1,
        'num2':num2,
        'result':res,
        'result1':res1,
        'result2':res2,
    }
    return render(request, 'calculators/result.html', context)