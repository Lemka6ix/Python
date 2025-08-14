# Часть 1: Модули для расчетов (пакет storage_devices)
## 1. Файл ```hdd_calculations.py``` (расчеты для жестких дисков)

```python
def calculate_hdd(data_size_gb, price_per_unit, speed_mbps=120):
    # Переводим объем данных из ГБ в Мбиты (1 ГБ = 8000 Мбит)
    data_size_mbits = data_size_gb * 8000
    
    # Рассчитываем время: объем в мегабитах / скорость в мегабитах в секунду
    time_seconds = data_size_mbits / speed_mbps
    
    # Определяем типичный объем диска (если цена >1000 руб - диск на 1000ГБ, иначе на 256ГБ)
    typical_capacity = 1000 if price_per_unit > 1000 else 256
    
    # Рассчитываем цену за 1 ГБ: цена устройства / его объем
    price_per_gb = price_per_unit / typical_capacity
    
    # Возвращаем результаты в виде словаря
    return {
        'type': 'HDD',
        'time': time_seconds,
        'price_per_gb': price_per_gb,
        'speed': speed_mbps
    }
```
## Как работает:
* Принимает объем данных, цену диска и его скорость (по умолчанию 120 Мбит/с)
* Переводит объем данных в мегабиты
* Рассчитывает время передачи: объем данных / скорость
* Определяет примерную емкость диска по его цене
* Рассчитывает цену за 1 ГБ: цена диска / его емкость
* Возвращает все данные в удобном формате


## 2. Файл ```ssd_calculations.py``` (расчеты для SSD)
Работает аналогично, но с другими параметрами:

* Скорость по умолчанию: 550 Мбит/с (выше чем у HDD)
* Типичные объемы: 1000 ГБ для дорогих SSD, 512 ГБ для дешевых

## 3. Файл flash_calculations.py (расчеты для флешек)

* Скорость по умолчанию: 100 Мбит/с (ниже чем у SSD)
* Типичные объемы: 64 ГБ для дорогих флешек, 32 ГБ для дешевых



# Часть 2: Графический интерфейс (main.py)
## Как работает интерфейс:
- Импорт библиотек - подключение всех необходимых инструментов

- Глобальная переменная RESULTS - хранит результаты расчетов
- Функция calculate_callback() - вызывается при нажатии кнопки "Calculate"


```python
def calculate_callback():
    # Получаем значения из полей ввода
    data_size = dpg.get_value("data_size")
    hdd_price = dpg.get_value("hdd_price")
    ssd_price = dpg.get_value("ssd_price")
    flash_price = dpg.get_value("flash_price")
    
    # Выполняем расчеты для каждого типа устройств
    hdd = calculate_hdd(data_size, hdd_price)
    ssd = calculate_ssd(data_size, ssd_price)
    flash = calculate_flash(data_size, flash_price)
    
    # Сохраняем результаты в глобальную переменную
    global RESULTS
    RESULTS = [hdd, ssd, flash]
    
    # Находим самое выгодное устройство (с минимальной ценой за ГБ)
    best_device = min(RESULTS, key=lambda x: x['price_per_gb'])
    
    # Обновляем интерфейс с результатами
    dpg.set_value("hdd_time", f"{hdd['time']:.2f} сек")
    # ... аналогично для других устройств ...
    
    dpg.set_value("best_device", 
                 f"Лучшее устройство: {best_device['type']}\n"
                 f"Цена за ГБ: {best_device['price_per_gb']:.2f} руб\n"
                 f"Время обработки: {best_device['time']:.2f} сек")
```

## Функции сохранения отчетов:
### Сохранение в Excel:
```python
def save_to_excel():
    # Создаем новую книгу Excel
    wb = Workbook()
    ws = wb.active
    ws.title = "Результаты анализа"
    
    # Добавляем заголовки столбцов
    ws.append(["Тип устройства", "Время (сек)", "Цена за ГБ (руб)", "Скорость (Мбит/с)"])
    
    # Добавляем данные по каждому устройству
    for device in RESULTS:
        ws.append([device['type'], device['time'], device['price_per_gb'], device['speed']])
    
    # Сохраняем файл и открываем его
    filename = "storage_analysis.xlsx"
    wb.save(filename)
    os.startfile(filename)
```

### Сохранение в Word:
```python
def save_to_word():
    # Создаем новый документ Word
    doc = Document()
    
    # Добавляем заголовок
    doc.add_heading('Анализ устройств хранения данных', 0)
    
    # Добавляем информацию о лучшем устройстве
    best_device = min(RESULTS, key=lambda x: x['price_per_gb'])
    doc.add_paragraph(f"Лучшее устройство: {best_device['type']}", style='Heading 2')
    
    # Создаем таблицу с результатами
    table = doc.add_table(rows=1, cols=4)
    # Добавляем заголовки таблицы
    # Добавляем данные устройств
    # Сохраняем и открываем файл
```
### Создание графического интерфейса:
```python
def create_gui():
    # Инициализация библиотеки
    dpg.create_context()
    dpg.create_viewport(title='Анализ устройств хранения данных', width=800, height=600)
    
    # Создание главного окна
    with dpg.window(label="Основное окно", width=780, height=580):
        # Группа полей ввода для объема данных
        with dpg.group(horizontal=True):
            dpg.add_text("Объем данных (ГБ):")
            dpg.add_input_float(tag="data_size", default_value=100, width=100)
        
        # Аналогичные группы для цен устройств...
        
        # Кнопка расчета
        dpg.add_button(label="Рассчитать", callback=calculate_callback)
        
        # Область для вывода результатов
        with dpg.collapsing_header(label="Результаты"):
            # Группа для вывода результатов по HDD
            with dpg.group(horizontal=True):
                dpg.add_text("HDD:")
                dpg.add_text(tag="hdd_time", label="Время: ")
                dpg.add_text(tag="hdd_price_gb", label="Цена за ГБ: ")
            
            # Аналогично для SSD и Flash...
            
            # Вывод лучшего устройства
            dpg.add_text(tag="best_device", label="")
        
        # Кнопки экспорта
        with dpg.group(horizontal=True):
            dpg.add_button(label="Сохранить в Excel", callback=save_to_excel)
            dpg.add_button(label="Сохранить в Word", callback=save_to_word)
    
    # Запуск интерфейса
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
```

# Как пользоваться программой
1. Запустите программу - дважды щелкните на файле main.py

2. Введите данные:

    * Объем данных, который нужно передать (в ГБ)

    * Цены на HDD, SSD и Flash-накопители

3. Нажмите "Calculate":

    * Программа покажет время передачи для каждого устройства

    * Рассчитает цену за 1 ГБ для каждого устройства

    * Выделит самое выгодное устройство

4. Сохраните отчет:

    * Нажмите "Сохранить в Excel" для создания таблицы

    * Или "Сохранить в Word" для создания документа