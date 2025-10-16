def calculate_hdd(data_size_gb, price_per_unit, speed_mbps=120):

    # Конвертация ГБ в Мбиты (1 ГБ = 8 Гбит = 8000 Мбит)
    data_size_mbits = data_size_gb * 8000
    time_seconds = data_size_mbits / speed_mbps
    
    # Расчет цены за ГБ
    price_per_gb = price_per_unit / (1000 if price_per_unit > 1000 else 256)  # Предполагаем типичный объем
    
    return {
        'type': 'HDD',
        'time': time_seconds,
        'price_per_gb': price_per_gb,
        'speed': speed_mbps
    }