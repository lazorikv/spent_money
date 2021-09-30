from .serializers import StatisticSerializer
from .models import Statistic
from django.views import generic
from api.forms import MoneyForm
from django.shortcuts import render


class ResultsView(generic.ListView):
    model = Statistic
    template_name = 'index.html'
    context_object_name = 'latest_list'
    serializer_class = StatisticSerializer

    def get_queryset(self):
        return Statistic.objects.all()


def index(request):

    if request.method == "POST":
        submitbutton = request.POST.get("submit")
        spent = 0
        get_money = 0

        form = MoneyForm(request.POST or None)
        if form.is_valid():
            spent = form.cleaned_data.get("spent")
            get_money = form.cleaned_data.get("get_money")
            Statistic.objects.create(spent=spent, get_money=get_money)

        context = {'form': form, 'spent': spent,
                   'get_money': get_money, 'submitbutton': submitbutton}

        return render(request, 'post.html', context)
    else:
        form = MoneyForm()
        return render(request, 'post.html', {'form': form})



