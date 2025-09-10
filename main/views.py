from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'title' : 'GoalStrike',
        'name': 'Syakirah Zahra Dhawini',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)