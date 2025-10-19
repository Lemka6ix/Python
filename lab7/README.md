```python
from abc import ABC, abstractmethod
from appJar import gui
from openpyxl import Workbook
from docx import Document
import os

class StorageDevice(ABC):
    def __init__(self, name, default_speed):
        self.name = name
        self.default_speed = default_speed
        self._price = 0
        self._data_size = 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @property
    def data_size(self):
        return self._data_size

    @data_size.setter
    def data_size(self, value):
        if value <= 0:
            raise ValueError("Data size must be positive")
        self._data_size = value

    @abstractmethod
    def calculate_time(self):
        pass

    @abstractmethod
    def calculate_price_per_gb(self):
        pass

    def __str__(self):
        return f"{self.name} device (speed: {self.default_speed} Mbps)"

    def __repr__(self):
        return f"<{self.__class__.__name__} name='{self.name}'>"

class HDD(StorageDevice):
    def __init__(self):
        super().__init__("HDD", 120)
        self._typical_capacities = {True: 1000, False: 256}

    def calculate_time(self):
        data_size_mbits = self.data_size * 8000
        return data_size_mbits / self.default_speed

    def calculate_price_per_gb(self):
        is_expensive = self.price > 1000
        return self.price / self._typical_capacities[is_expensive]

class SSD(StorageDevice):
    def __init__(self):
        super().__init__("SSD", 550)
        self._typical_capacities = {True: 1000, False: 512}

    def calculate_time(self):
        data_size_mbits = self.data_size * 8000
        return data_size_mbits / self.default_speed

    def calculate_price_per_gb(self):
        is_expensive = self.price > 1000
        return self.price / self._typical_capacities[is_expensive]

class FlashDrive(StorageDevice):
    def __init__(self):
        super().__init__("Flash", 100)
        self._typical_capacities = {True: 64, False: 32}

    def calculate_time(self):
        data_size_mbits = self.data_size * 8000
        return data_size_mbits / self.default_speed

    def calculate_price_per_gb(self):
        is_expensive = self.price > 1000
        return self.price / self._typical_capacities[is_expensive]

class StorageAnalyzerApp:
    def __init__(self):
        self.app = gui("Storage Device Analyzer", "800x600")
        self.devices = {
            "HDD": HDD(),
            "SSD": SSD(),
            "Flash": FlashDrive()
        }
        self.results = []

    def setup_ui(self):
        self.app.setFont(size=12)
        
        self.app.addLabel("title", "Storage Device Analysis", colspan=2)
        self.app.addLabel("data_label", "Data size (GB):", row=1, column=0)
        self.app.addEntry("data_size", row=1, column=1)
        self.app.setEntry("data_size", "100")
        
        for i, (name, device) in enumerate(self.devices.items(), start=2):
            self.app.addLabel(f"{name.lower()}_price_label", f"{name} price (руб):", row=i, column=0)
            self.app.addEntry(f"{name.lower()}_price", row=i, column=1)
            self.app.setEntry(f"{name.lower()}_price", "3000" if name != "Flash" else "1000")
        
        self.app.addButton("Calculate", self.calculate, row=5, colspan=2)
        
        self.app.addLabel("results_title", "Results:", row=6, colspan=2)
        
        for i, (name, device) in enumerate(self.devices.items(), start=7):
            self.app.addLabel(f"{name.lower()}_result", f"{name}: ", row=i, column=0)
            self.app.addLabel(f"{name.lower()}_time", "", row=i, column=1)
        
        self.app.addLabel("best_device", "", row=10, colspan=2)
        
        self.app.addButtons(["Save to Excel", "Save to Word"], 
                          [self.save_to_excel, self.save_to_word], row=11, colspan=2)

    def calculate(self, button):
        try:
            data_size = float(self.app.getEntry("data_size"))
            
            for name, device in self.devices.items():
                device.data_size = data_size
                device.price = float(self.app.getEntry(f"{name.lower()}_price"))
            
            self.results = []
            for name, device in self.devices.items():
                time = device.calculate_time()
                price_per_gb = device.calculate_price_per_gb()
                self.results.append({
                    'type': name,
                    'time': time,
                    'price_per_gb': price_per_gb,
                    'speed': device.default_speed
                })
                
                self.app.setLabel(f"{name.lower()}_time", 
                                f"Time: {time:.2f} sec, Price per GB: {price_per_gb:.2f} руб")
            
            best = min(self.results, key=lambda x: x['price_per_gb'])
            self.app.setLabel("best_device", 
                            f"Best device: {best['type']}\n"
                            f"Price per GB: {best['price_per_gb']:.2f} руб\n"
                            f"Transfer time: {best['time']:.2f} sec")
        
        except ValueError as e:
            self.app.errorBox("Error", str(e))

    def save_to_excel(self, button):
        if not self.results:
            self.app.warningBox("Warning", "No data to save")
            return
        
        wb = Workbook()
        ws = wb.active
        ws.title = "Analysis Results"
        
        ws.append(["Device Type", "Time (sec)", "Price per GB (руб)", "Speed (Mbps)"])
        
        for device in self.results:
            ws.append([device['type'], device['time'], device['price_per_gb'], device['speed']])
        
        filename = "storage_analysis.xlsx"
        wb.save(filename)
        os.startfile(filename)

    def save_to_word(self, button):
        if not self.results:
            self.app.warningBox("Warning", "No data to save")
            return
        
        doc = Document()
        doc.add_heading('Storage Device Analysis', 0)
        
        best = min(self.results, key=lambda x: x['price_per_gb'])
        doc.add_paragraph(f"Best device: {best['type']}", style='Heading 2')
        
        table = doc.add_table(rows=1, cols=4)
        table.style = 'Table Grid'
        
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'Device Type'
        hdr_cells[1].text = 'Time (sec)'
        hdr_cells[2].text = 'Price per GB (руб)'
        hdr_cells[3].text = 'Speed (Mbps)'
        
        for device in self.results:
            row_cells = table.add_row().cells
            row_cells[0].text = device['type']
            row_cells[1].text = f"{device['time']:.2f}"
            row_cells[2].text = f"{device['price_per_gb']:.2f}"
            row_cells[3].text = str(device['speed'])
        
        filename = "storage_analysis.docx"
        doc.save(filename)
        os.startfile(filename)

    def run(self):
        self.setup_ui()
        self.app.go()

if __name__ == "__main__":
    app = StorageAnalyzerApp()
    app.run()
```
## 1. Абстрактный базовый класс (StorageDevice)

```python
class StorageDevice(ABC):
```
Это абстрактный класс, определяющий общий интерфейс для всех устройств хранения.

### Ключевые элементы:

* @abstractmethod - методы, которые должны быть реализованы в дочерних классах

* @property и @setter - обеспечивают контроль за установкой значений (валидация)

* ```__str__``` и ```__repr__``` - методы для строкового представления объектов


## 2. Конкретные реализации устройств
HDD, SSD, FlashDrive

Каждый класс наследует от `StorageDevice` и реализует:

* Конкретные значения скорости по умолчанию

* Специфичную логику расчета цены за GB на основе типичных емкостей

* Одинаковую формулу расчета времени передачи

### Формула времени передачи
```python
data_size_mbits = self.data_size * 8000  # GB → Mbit (1 byte = 8 bit)
return data_size_mbits / self.default_speed  # время в секундах
```


## 3. Графический интерфейс (StorageAnalyzerApp)
Инициализация:
```python
self.app = gui("Storage Device Analyzer", "800x600")
```
Создается окно приложения с помощью библиотеки `appJar`.
Настройка UI (`setup_ui`):

* Добавляются поля ввода для размера данных и цены каждого устройства

* Устанавливаются значения по умолчанию

* Добавляются кнопки для расчетов и экспорта

Логика расчета (`calculate`):

* Получает значения из полей ввода

* Для каждого устройства вычисляет:

    * Время передачи данных

    * Цену за GB

* Находит устройство с наилучшим соотношением цены за GB

* Обновляет интерфейс с результатами

## 4. Экспорт результатов
В Excel (**save_to_excel**):

* Создает XLSX-файл с помощью `openpyxl`

* Добавляет заголовки и данные результатов

* Автоматически открывает файл (os.startfile)

В Word (**save_to_word**):

* Создает DOCX-документ с помощью `python-docx`

* Добавляет заголовок, информацию о лучшем устройстве

* Создает таблицу с результатами

* Автоматически открывает файл

## 5. Запуск приложения
```python
if __name__ == "__main__":
    app = StorageAnalyzerApp()
    app.run()
```
При запуске скрипта создается экземпляр приложения и запускается главный цикл.

## Как работает программа:
1. **Пользователь** вводит объем данных и цены устройств

2. **Программа** вычисляет для каждого устройства:

    * Время передачи данных (в секундах)

    * Стоимость хранения 1 GB данных

3. **Определяется** оптимальное устройство по цене за GB

4. **Результаты** отображаются в интерфейсе

5. **Пользователь** может экспортировать данные в Excel или Word



## Результат работы программы

### Интерфейс программы
![result1](https://github.com/Lemka6ix/Python/blob/main/lab7/png/program.png)

### Сохраненные данные в формате Word
![result2](https://github.com/Lemka6ix/Python/blob/main/lab7/png/wordf.png)

### Сохраненные данные в формате Excel
![result2](https://github.com/Lemka6ix/Python/blob/main/lab7/png/excelf.png)