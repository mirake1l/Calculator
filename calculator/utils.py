"""Формулы и границы оценок перенесены из practicum.py без изменений."""


def assess_three_zones(score, lower, upper, favorable_message):
    """Общая схема оценки Альтмана и Таффлера."""
    if score < lower:
        return 'Высокая вероятность банкротства'
    if score <= upper:
        return 'Зона неопределенности'
    return favorable_message


def calculate_altman(data):
    assets = data['total_assets']
    liabilities = data['long_term_liabilities'] + data['current_liabilities']
    score = (
        0.717 * ((data['current_assets'] - data['current_liabilities']) / assets)
        + 0.847 * (data['retained_earnings'] / assets)
        + 3.107 * ((data['profit_before_tax'] + data['interest_payable']) / assets)
        + 0.420 * (data['equity'] / liabilities)
        + 0.998 * (data['revenue'] / assets)
    )
    conclusion = assess_three_zones(
        score, 1.23, 2.89, 'Низкая вероятность банкротства'
    )
    return score, conclusion


def assess_irkutsk(score):
    if score < 0:
        return 'Максимальная вероятность банкротства (90-100%)'
    if score <= 0.18:
        return 'Высокая вероятность банкротства (60-80%)'
    if score <= 0.32:
        return 'Средняя вероятность банкротства (30-50%)'
    return 'Низкая вероятность банкротства (менее 10%)'


def calculate_irkutsk(data):
    assets = data['total_assets']
    profit = data['net_profit']
    score = (
        8.38 * ((data['current_assets'] - data['current_liabilities']) / assets)
        + profit / data['equity']
        + 0.05 * (data['revenue'] / assets)
        + 0.63 * (profit / data['cost_of_sales'])
    )
    return score, assess_irkutsk(score)


def calculate_taffler(data):
    assets = data['total_assets']
    liabilities = data['long_term_liabilities'] + data['current_liabilities']
    score = (
        0.53 * (data['sales_profit'] / data['current_liabilities'])
        + 0.13 * (data['current_assets'] / liabilities)
        + 0.18 * (liabilities / assets)
        + 0.16 * (data['revenue'] / assets)
    )
    conclusion = assess_three_zones(
        score, 0.2, 0.3,
        'Хорошие перспективы для предприятия, финансовая устойчивость высокая',
    )
    return score, conclusion
