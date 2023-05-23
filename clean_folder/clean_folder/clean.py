import os
import sys
import shutil
import re


def normalize(filename):
    transliteration_map = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'є': 'ye', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'і': 'i', 'ї': 'yi', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ь': '',
        'ы': 'y', 'ъ': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
    }

    # Транслітерація кириличних символів
    normalized = ''.join(transliteration_map.get(c.lower(), c) for c in filename)

    # Заміна неприпустимих символів на "_"
    normalized = re.sub(r'[^a-zA-Z0-9]+', '_', normalized)

    return normalized


def process_folder():
    if len(sys.argv) < 2:
        print("Please provide the folder path.")
    else:
        folder_path = sys.argv[1]
        contents = os.listdir(folder_path)
        for item in contents:
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                filename, extension = os.path.splitext(item)
                new_filename = normalize(filename) + extension
                if extension.lower() in ['.jpeg', '.png', '.jpg', '.svg']:
                    # Зображення - переносимо до папки images
                    destination_folder = os.path.join(folder_path, 'images')
                elif extension.lower() in ['.avi', '.mp4', '.mov', '.mkv']:
                    # Відео файли - переносимо до папки video
                    destination_folder = os.path.join(folder_path, 'video')
                elif extension.lower() in ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']:
                    # Документи - переносимо до папки documents
                    destination_folder = os.path.join(folder_path, 'documents')
                elif extension.lower() in ['.mp3', '.ogg', '.wav', '.amr']:
                    # Аудіо файли - переносимо до папки audio
                    destination_folder = os.path.join(folder_path, 'audio')
                elif extension.lower() in ['.zip', '.gz', '.tar']:
                    # Архіви - розпаковуємо та переносимо вміст до папки archives
                    destination_folder = os.path.join(folder_path, 'archives', filename)
                    os.makedirs(destination_folder, exist_ok=True)
                    shutil.unpack_archive(item_path, destination_folder)
                    continue
                else:
                    # Розширення невідоме - залишаємо без змін
                    continue

                # Переносимо файл до відповідної папки
                os.makedirs(destination_folder, exist_ok=True)
                shutil.move(item_path, os.path.join(destination_folder, new_filename))


if __name__ == '__main__':
    process_folder()