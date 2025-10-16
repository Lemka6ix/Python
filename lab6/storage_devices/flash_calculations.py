def calculate_flash(data_size_gb, price_per_unit, speed_mbps=100):

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