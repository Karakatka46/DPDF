import PyPDF2
import os

pdf_folder = "/home/aplelsin/wlan_parsing/asgasdf"
# Создаем объект PdfMerger для объединения PDF
merger = PyPDF2.PdfMerger()

# Получаем список всех файлов в указанной папке
for filename in sorted(os.listdir(pdf_folder)):
    if filename.endswith(".pdf"):  # Проверяем, что файл имеет расширение .pdf
        pdf_file = os.path.join(pdf_folder, filename)  # Получаем полный путь к файлу
        try:
            # Добавляем каждый PDF файл в итоговый документ
            merger.append(pdf_file)
            print(f"Добавлен файл: {pdf_file}")
        except Exception as e:
            print(f"Ошибка при добавлении {pdf_file}: {e}")

# Сохраняем итоговый объединенный PDF файл
output_filename = "Wlan_prefinal.pdf"
merger.write(output_filename)
merger.close()

print(f"Объединенный PDF файл сохранен как {output_filename}")