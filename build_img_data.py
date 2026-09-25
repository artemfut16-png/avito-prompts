"""Собирает img-data.js из всех картинок в папке img/.
Нужен, чтобы кнопка «Копировать» на странице работала и при открытии файла двойным кликом (file://).
Запускать после добавления новых картинок:  python build_img_data.py
"""
import base64, json, pathlib

MIME = {'.webp': 'image/webp', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png'}

root = pathlib.Path(__file__).parent
data = {}
for f in sorted((root / 'img').iterdir()):
    if f.suffix.lower() in MIME:
        mime = MIME[f.suffix.lower()]
        data['img/' + f.name] = f'data:{mime};base64,' + base64.b64encode(f.read_bytes()).decode()
(root / 'img-data.js').write_text('window.IMG_DATA = ' + json.dumps(data) + ';\n', encoding='utf-8')
print(len(data), 'images ->', (root / 'img-data.js').stat().st_size // 1024, 'KB')
