def calculate_ssd(data_size_gb, price_per_unit, speed_mbps=550):

    data_size_mbits = data_size_gb * 8000
    time_seconds = data_size_mbits / speed_mbps
    
    # Расчет цены за ГБ
    price_per_gb = price_per_unit / (1000 if price_per_unit > 1000 else 512)
    
    return {
        'type': 'SSD',
        'time': time_seconds,
        'price_per_gb': price_per_gb,
        'speed': speed_mbps
    }