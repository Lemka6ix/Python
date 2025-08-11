import dearpygui.dearpygui as dpg
from storage_devices import calculate_hdd, calculate_ssd, calculate_flash
from openpyxl import Workbook
from docx import Document
from docx.shared import Pt
import os

# Константы
RESULTS = []

def calculate_callback():
    """Обработчик кнопки расчета"""
    try:
        data_size = dpg.get_value("data_size")
        hdd_price = dpg.get_value("hdd_price")
        ssd_price = dpg.get_value("ssd_price")
        flash_price = dpg.get_value("flash_price")
        
        # Получаем результаты для каждого устройства
        hdd = calculate_hdd(data_size, hdd_price)
        ssd = calculate_ssd(data_size, ssd_price)
        flash = calculate_flash(data_size, flash_price)
        
        global RESULTS
        RESULTS = [hdd, ssd, flash]
        
        # Находим лучшее устройство по цене за ГБ
        best_device = min(RESULTS, key=lambda x: x['price_per_gb'])
        
        # Обновляем UI
        dpg.set_value("hdd_time", f"{hdd['time']:.2f} сек")
        dpg.set_value("hdd_price_gb", f"{hdd['price_per_gb']:.2f} руб/ГБ")
        
        dpg.set_value("ssd_time", f"{ssd['time']:.2f} сек")
        dpg.set_value("ssd_price_gb", f"{ssd['price_per_gb']:.2f} руб/ГБ")
        
        dpg.set_value("flash_time", f"{flash['time']:.2f} сек")
        dpg.set_value("flash_price_gb", f"{flash['price_per_gb']:.2f} руб/ГБ")
        
        dpg.set_value("best_device", 
                     f"Лучшее устройство: {best_device['type']}\n"
                     f"Цена за ГБ: {best_device['price_per_gb']:.2f} руб\n"
                     f"Время обработки: {best_device['time']:.2f} сек")
        
    except Exception as e:
        dpg.set_value("best_device", f"Ошибка: {str(e)}")

def save_to_excel():
    """Сохранение результатов в Excel"""
    if not RESULTS:
        return
        
    wb = Workbook()
    ws = wb.active
    ws.title = "Результаты анализа"
    
    # Заголовки
    ws.append(["Тип устройства", "Время (сек)", "Цена за ГБ (руб)", "Скорость (Мбит/с)"])
    
    # Данные
    for device in RESULTS:
        ws.append([device['type'], device['time'], device['price_per_gb'], device['speed']])
    
    # Сохраняем файл
    filename = "storage_analysis.xlsx"
    wb.save(filename)
    os.startfile(filename)

def save_to_word():
    """Сохранение результатов в Word"""
    if not RESULTS:
        return
        
    doc = Document()
    
    # Заголовок
    doc.add_heading('Анализ устройств хранения данных', 0)
    
    # Лучшее устройство
    best_device = min(RESULTS, key=lambda x: x['price_per_gb'])
    doc.add_paragraph(f"Лучшее устройство: {best_device['type']}", style='Heading 2')
    
    # Таблица с результатами
    table = doc.add_table(rows=1, cols=4)
    table.style = 'Table Grid'
    
    # Заголовки таблицы
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Тип устройства'
    hdr_cells[1].text = 'Время (сек)'
    hdr_cells[2].text = 'Цена за ГБ (руб)'
    hdr_cells[3].text = 'Скорость (Мбит/с)'
    
    # Данные таблицы
    for device in RESULTS:
        row_cells = table.add_row().cells
        row_cells[0].text = device['type']
        row_cells[1].text = f"{device['time']:.2f}"
        row_cells[2].text = f"{device['price_per_gb']:.2f}"
        row_cells[3].text = str(device['speed'])
    
    # Сохраняем файл
    filename = "storage_analysis.docx"
    doc.save(filename)
    os.startfile(filename)

def create_gui():
    """Создание графического интерфейса"""
    dpg.create_context()
    dpg.create_viewport(title='Анализ устройств хранения данных', width=800, height=600)
    
    with dpg.window(label="Основное окно", width=780, height=580):
        # Ввод данных
        with dpg.group(horizontal=True):
            dpg.add_text("Объем данных (ГБ):")
            dpg.add_input_float(tag="data_size", default_value=100, width=100)
        
        with dpg.group(horizontal=True):
            dpg.add_text("Цена HDD (руб):")
            dpg.add_input_float(tag="hdd_price", default_value=3000, width=100)
        
        with dpg.group(horizontal=True):
            dpg.add_text("Цена SSD (руб):")
            dpg.add_input_float(tag="ssd_price", default_value=5000, width=100)
        
        with dpg.group(horizontal=True):
            dpg.add_text("Цена Flash (руб):")
            dpg.add_input_float(tag="flash_price", default_value=1000, width=100)
        
        dpg.add_button(label="Рассчитать", callback=calculate_callback)
        
        # Результаты
        with dpg.collapsing_header(label="Результаты"):
            with dpg.group(horizontal=True):
                dpg.add_text("HDD:")
                dpg.add_text(tag="hdd_time", label="Время: ")
                dpg.add_text(tag="hdd_price_gb", label="Цена за ГБ: ")
            
            with dpg.group(horizontal=True):
                dpg.add_text("SSD:")
                dpg.add_text(tag="ssd_time", label="Время: ")
                dpg.add_text(tag="ssd_price_gb", label="Цена за ГБ: ")
            
            with dpg.group(horizontal=True):
                dpg.add_text("Flash:")
                dpg.add_text(tag="flash_time", label="Время: ")
                dpg.add_text(tag="flash_price_gb", label="Цена за ГБ: ")
            
            dpg.add_text(tag="best_device", label="")
        
        # Кнопки экспорта
        with dpg.group(horizontal=True):
            dpg.add_button(label="Сохранить в Excel", callback=save_to_excel)
            dpg.add_button(label="Сохранить в Word", callback=save_to_word)
    
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    create_gui()