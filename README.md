YouTube Downloader (GUI, Python, yt‑dlp)
Prosty i wygodny downloader filmów z YouTube z graficznym interfejsem opartym o Tkinter.
Aplikacja pozwala pobierać filmy w najlepszej dostępnej jakości (automatyczne łączenie wideo + audio), pokazuje pasek postępu oraz umożliwia wybór folderu zapisu.

🚀 Funkcje
Pobieranie filmów z YouTube w najwyższej jakości (bestvideo+bestaudio).

Automatyczne scalanie plików do formatu MP4.

Graficzny interfejs użytkownika (Tkinter).

Pasek postępu pobierania.

Informacje o statusie (łączenie, pobieranie, scalanie).

Wybór folderu zapisu.

Obsługa błędów i komunikaty dla użytkownika.

Pobieranie w osobnym wątku — aplikacja nie zawiesza się.

📦 Wymagania
Aby uruchomić aplikację, potrzebujesz:

Python 3.8+

Biblioteki:

yt-dlp

imageio-ffmpeg

tkinter (wbudowany w Pythona)

ttk (część tkinter)

🔧 Instalacja
Zainstaluj wymagane pakiety:

bash
pip install yt-dlp imageio-ffmpeg
▶️ Uruchamianie
Po prostu uruchom plik:

bash
python main.py
Aplikacja otworzy okno GUI.

🖥️ Jak używać
Wklej link do filmu z YouTube.

Wybierz folder zapisu.

Kliknij Pobierz film.

Obserwuj pasek postępu.

Po zakończeniu otrzymasz komunikat z tytułem pobranego filmu.

🧩 Struktura działania
Aplikacja korzysta z:

yt-dlp — pobieranie wideo i audio.

imageio-ffmpeg — wskazanie lokalizacji ffmpeg.

threading — pobieranie w tle.

Tkinter — GUI, pasek postępu, komunikaty.

Postęp pobierania jest aktualizowany przez progress_hooks, a GUI odświeżany przez root.after().

📁 Kod źródłowy
Cały kod znajduje się w jednym pliku i zawiera:

Funkcję wyboru folderu

Funkcję pobierania filmu

Hook postępu

Wątek pobierania

Interfejs Tkinter

⚠️ Uwagi
Program pobiera tylko publiczne materiały zgodnie z regulaminem YouTube.

Wymagane jest działające ffmpeg (automatycznie wykrywane przez imageio_ffmpeg).

📜 Licencja
APACHE
