from django.shortcuts import render
from django.http import HttpResponse
from forms import forms
from backend import calorie_calc
# Create your views here.
def index(request):
    if request.method == "POST":
        form = forms.CalorieForm(request.POST)

        if form.is_valid():
            value = calorie_calc.calc(
                form.cleaned_data['gender'],
                form.cleaned_data['weight'],
                form.cleaned_data['height'],
                form.cleaned_data['age']
            )
            return HttpResponse(int(value))
    else:
        form = forms.CalorieForm()

    return render(request, 'calorie_calc/index.html', {'form': form})


def day_selected(request, day):
    if 1 <= day <= 6:
        return HttpResponse("%s" % day)
    else:
        return HttpResponse("Invalid number of days")
