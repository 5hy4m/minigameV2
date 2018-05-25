from django.shortcuts import render
from mini_app.models import feedback_model
from mini_app.forms import feedback_form
# Create your views here.
def home(request):
    return render(request,'newui/index.html')

def feedback(request):
    form = feedback_form()
    if request.method =='POST':
        form = feedback_form(request.POST)
        if form.is_valid():
            form.save(commit =True)
            return render(request,'feedback/thankyou.html')
        else:
            print('ERROR FORM INVALID')
    return render(request,'feedback/feedback.html',{'form':form})

# def archery_form(request):
#     form = archery_board_form()
#
#     if request.method == "POST":
#         form = archery_board_form(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return archery_game(request)
#         else:
#             print('ERROR FORM INVALID')
#             return retry(request)
#
# return render(request,'archery/archery_login.html',{'form':form})

def tictactoe(request):
    return render(request,'mini_app/tictactoe/tictactoe.html')

def fingercut(request):
    return render(request,'fingercut/fingercut.html')

def snakeattack(request):
    return render(request,'snakeattack/snakeattack.html')

def light_game(request):
    return render(request,'light_game/light_game.html')

def orbitshooter(request):
    return render(request,'orbitshooter/orbitshooter.html')


def archery_game(request):
    return render(request,'archery/archery.html')


def retry(request):
    return render(request,'archery/archery_login.html')
