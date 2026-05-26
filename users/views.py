from django.shortcuts import render, redirect
from django.contrib.auth import login

from learning_logs.forms import CustomRegisterForm

def register(request):
    """Регистрирует нового пользователя."""
    if request.method != 'POST':
        # Выводит пустую форму регистрации.
        form = CustomRegisterForm()
    else:
        # Обработка заполненной формы.
        form = CustomRegisterForm(data=request.POST)

        if form.is_valid():
            # Выполнение входа и перенаправление на домашнюю страницу.
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_logs:index')

    # Вывести пустую или недействительную форму
    context = {'form': form}
    return render(request, 'registration/register.html', context)