from django.shortcuts import render, redirect
from exchange_converter.forms import CurencyForm, result


def index(request):
    if request.method== 'POST':
        form=CurencyForm(request.POST)
        if form.is_valid():
            first_cur=result[form.cleaned_data['first_cur']]
            second_cur = result[form.cleaned_data['second_cur']]
            amount=form.cleaned_data['cur_amount']
            exch=round(second_cur/first_cur*amount,2)
            return render(request, 'exchange_converter/base.html', {'form': form, 'exch': exch})
    else:
        form=CurencyForm()
        return render(request,'exchange_converter/base.html',{'form':form})
