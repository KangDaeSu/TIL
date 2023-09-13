from django.shortcuts import render

# Create your views here.
def converter(request, num1, num2):
    result = num1 * num2
    result1 = num1 - num2
    if num2 != 0:
        result2 = num1 / num2
    else:
        result2 = False
    context = {
        'num1': num1,
        'num2': num2,
        'result': result,
        'result1': result1,
        'result2': result2

    }
    return render(request, 'calculators/calculator.html', context)