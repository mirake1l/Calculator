from django import forms


class FinancialForm(forms.Form):
    """Показатели, которые используются во всех трёх моделях."""

    current_assets = forms.IntegerField(label='Оборотные активы (1200)')
    current_liabilities = forms.IntegerField(
        label='Краткосрочные обязательства (1500)'
    )
    total_assets = forms.IntegerField(label='Баланс — итого активов (1600)')
    revenue = forms.IntegerField(label='Выручка (2110)')


class AltmanForm(FinancialForm):
    equity = forms.IntegerField(label='Капитал и резервы (1300)')
    retained_earnings = forms.IntegerField(
        label='Нераспределённая прибыль (непокрытый убыток) (1370)'
    )
    long_term_liabilities = forms.IntegerField(
        label='Долгосрочные обязательства (1400)'
    )
    profit_before_tax = forms.IntegerField(
        label='Прибыль (убыток) до налогообложения (2300)'
    )
    interest_payable = forms.IntegerField(label='Проценты к уплате (2330)')
    net_profit = forms.IntegerField(
        label='Чистая прибыль (убыток) (2400)',
        help_text='Этот показатель не используется в расчёте Альтмана.',
    )
    field_order = [
        'current_assets', 'equity', 'retained_earnings',
        'long_term_liabilities', 'current_liabilities', 'total_assets',
        'revenue', 'profit_before_tax', 'interest_payable', 'net_profit',
    ]


class IrkutskForm(FinancialForm):
    equity = forms.IntegerField(label='Капитал и резервы (1300)')
    cost_of_sales = forms.IntegerField(label='Себестоимость продаж (2120)')
    net_profit = forms.IntegerField(label='Чистая прибыль (убыток) (2400)')
    field_order = [
        'current_assets', 'equity', 'current_liabilities', 'total_assets',
        'revenue', 'cost_of_sales', 'net_profit',
    ]


class TafflerForm(FinancialForm):
    long_term_liabilities = forms.IntegerField(
        label='Долгосрочные обязательства (1400)'
    )
    sales_profit = forms.IntegerField(label='Прибыль (убыток) от продаж (2200)')
    field_order = [
        'current_assets', 'long_term_liabilities', 'current_liabilities',
        'total_assets', 'revenue', 'sales_profit',
    ]
