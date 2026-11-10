from django import forms


class FinancialForm(forms.Form):
    """Показатели, которые используются во всех трёх моделях.

    В initial указаны примерные значения: они подставляются в пустую
    форму, и пользователь может заменить их своими данными.
    """

    current_assets = forms.IntegerField(
        label='Оборотные активы (1200)', initial=500
    )
    current_liabilities = forms.IntegerField(
        label='Краткосрочные обязательства (1500)', initial=300
    )
    total_assets = forms.IntegerField(
        label='Баланс — итого активов (1600)', initial=1000
    )
    revenue = forms.IntegerField(label='Выручка (2110)', initial=1500)


class AltmanForm(FinancialForm):
    equity = forms.IntegerField(
        label='Капитал и резервы (1300)', initial=400
    )
    retained_earnings = forms.IntegerField(
        label='Нераспределённая прибыль (непокрытый убыток) (1370)',
        initial=100,
    )
    long_term_liabilities = forms.IntegerField(
        label='Долгосрочные обязательства (1400)', initial=200
    )
    profit_before_tax = forms.IntegerField(
        label='Прибыль (убыток) до налогообложения (2300)', initial=120
    )
    interest_payable = forms.IntegerField(
        label='Проценты к уплате (2330)', initial=10
    )
    net_profit = forms.IntegerField(
        label='Чистая прибыль (убыток) (2400)',
        help_text='Этот показатель не используется в расчёте Альтмана.',
        initial=90,
    )
    field_order = [
        'current_assets', 'equity', 'retained_earnings',
        'long_term_liabilities', 'current_liabilities', 'total_assets',
        'revenue', 'profit_before_tax', 'interest_payable', 'net_profit',
    ]


class IrkutskForm(FinancialForm):
    equity = forms.IntegerField(
        label='Капитал и резервы (1300)', initial=400
    )
    cost_of_sales = forms.IntegerField(
        label='Себестоимость продаж (2120)', initial=1000
    )
    net_profit = forms.IntegerField(
        label='Чистая прибыль (убыток) (2400)', initial=90
    )
    field_order = [
        'current_assets', 'equity', 'current_liabilities', 'total_assets',
        'revenue', 'cost_of_sales', 'net_profit',
    ]


class TafflerForm(FinancialForm):
    long_term_liabilities = forms.IntegerField(
        label='Долгосрочные обязательства (1400)', initial=200
    )
    sales_profit = forms.IntegerField(
        label='Прибыль (убыток) от продаж (2200)', initial=150
    )
    field_order = [
        'current_assets', 'long_term_liabilities', 'current_liabilities',
        'total_assets', 'revenue', 'sales_profit',
    ]
