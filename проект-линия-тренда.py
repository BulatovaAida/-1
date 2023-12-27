import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tkinter import Tk, filedialog, Button, Canvas, Frame, Label
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def calculate_trend_line(x, y):
    coefficients = np.polyfit(x, y, 1)
    trend_line = np.polyval(coefficients, x)
    return trend_line

def plot_graph(frame, label, file_path):
    try:
        # Загрузка данных из Excel-файла
        df = pd.read_excel(file_path)

        # Проверка наличия нужных данных в DataFrame
        if 'День месяца' not in df.columns or 'Температура' not in df.columns:
            raise ValueError("Недостающие данные")
    except (FileNotFoundError, ValueError) as e:
        label.config(text="ОШИБКА - НЕ СОВПАДЕНИЕ ДАННЫХ, пожалуйста, выберите файл с корректными данными")
        return

    # Извлечение данных из DataFrame
    days = df['День месяца'].tolist()
    temperatures = df['Температура'].tolist()

    # Расчет линии тренда
    trend_line = calculate_trend_line(days, temperatures)

    # Создание графика
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(days, temperatures, label='Температура')
    ax.plot(days, trend_line, color='red', label='Линия тренда')
    ax.set_xlabel('День месяца')
    ax.set_ylabel('Температура')
    ax.set_title('График температурного режима с линией тренда')
    ax.legend()

    # Вставка графика в окно
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

def on_button_click(frame, label):
    file_path = choose_excel_file()
    if file_path:
        label.config(text="")
        plot_graph(frame, label, file_path)

def choose_excel_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx;*.xls")])
    root.destroy()
    return file_path

def main():
    # Создание главного окна
    root = Tk()
    root.title("График с линией тренда")

    # Фрейм для размещения графика, кнопки и текста ошибки
    frame = Frame(root, bg='black')
    frame.pack(expand=True, fill='both')

    # Label для текста ошибки
    error_label = Label(frame, text="", fg="red", bg='black')
    error_label.pack(pady=10)

    # Кнопка "Выбрать файл" в середине графического окна
    button_select_file = Button(frame, text="Выбрать файл", command=lambda: on_button_click(frame, error_label), bg='white')
    button_select_file.pack(pady=10)

    # Запуск главного цикла обработки событий
    root.mainloop()

if __name__ == "__main__":
    main()
