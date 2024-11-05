import PyPDF2
import os

# 1. Путь к папке с PDF файлами
pdf_folder = "/home/aplelsin/wlan_parsing/asgasdf"

# 2. Создаем объект PdfMerger для объединения PDF
merger = PyPDF2.PdfMerger()

# 3. Получаем список всех файлов в указанной папке
for filename in sorted(os.listdir(pdf_folder)):
    if filename.endswith(".pdf"):  # Проверяем, что файл имеет расширение .pdf
        pdf_file = os.path.join(pdf_folder, filename)  # Получаем полный путь к файлу
        try:
            # Добавляем каждый PDF файл в итоговый документ
            merger.append(pdf_file)
            print(f"Добавлен файл: {pdf_file}")
        except Exception as e:
            print(f"Ошибка при добавлении {pdf_file}: {e}")

# 4. Сохраняем итоговый объединенный PDF файл
output_filename = "Wlan_final.pdf"
merger.write(output_filename)
merger.close()

print(f"Объединенный PDF файл сохранен как {output_filename}")