from django.http import Http404
from django.shortcuts import render

from .forms import AltmanForm, IrkutskForm, TafflerForm
from .utils import calculate_altman, calculate_irkutsk, calculate_taffler

MODELS = {
    'altman': ('Пятифакторная модель Альтмана', AltmanForm, calculate_altman),
    'irkutsk': ('Модель иркутской ГЭА', IrkutskForm, calculate_irkutsk),
    'taffler': ('Модель Таффлера', TafflerForm, calculate_taffler),
}


def calculator(request, model):
    if model not in MODELS:
        raise Http404('Выбранная модель не существует.')
    title, form_class, calculate = MODELS[model]
    form = form_class(request.GET or None)
    context = {'form': form, 'title': title}
    if form.is_valid():
        try:
            score, conclusion = calculate(form.cleaned_data)
        except ZeroDivisionError:
            context['error'] = (
                'Расчёт невозможен: один из знаменателей равен нулю. '
                'Проверьте введённые показатели.'
            )
        else:
            context.update({'score': round(score, 2), 'conclusion': conclusion})
    return render(request, 'calculator/calculator.html', context)
