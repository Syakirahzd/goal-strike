from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'title' : 'GoalStrike',
        'npm': '2406353950',
        'name': 'Syakirah Zahra Dhawini',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)