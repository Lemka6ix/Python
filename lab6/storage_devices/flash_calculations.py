def calculate_flash(data_size_gb, price_per_unit, speed_mbps=100):
    """
    Рассчитывает время и стоимость для Flash-накопителя
    :param data_size_gb: объем данных в ГБ
    :param price_per_unit: цена устройства
    :param speed_mbps: скорость в Мбит/с (по умолчанию 100)
    :return: словарь с результатами
    """
    data_size_mbits = data_size_gb * 8000
    time_seconds = data_size_mbits / speed_mbps
    
    # Расчет цены за ГБ
    price_per_gb = price_per_unit / (64 if price_per_unit > 1000 else 32)
    
    return {
        'type': 'Flash',
        'time': time_seconds,
        'price_per_gb': price_per_gb,
        'speed': speed_mbps
    }