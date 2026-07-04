import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import threading
import yt_dlp
import imageio_ffmpeg

# Domyślny folder zapisu
folder_zapisu = "."


def wybierz_folder():
    global folder_zapisu
    folder = filedialog.askdirectory()
    if folder:
        folder_zapisu = folder
        lbl_folder.config(text=folder)


def pobierz_film():

    url = entry_url.get().strip()

    if not url:
        messagebox.showwarning("Błąd", "Wpisz adres filmu.")
        return

    btn_pobierz.config(state="disabled")
    progress["value"] = 0
    status.config(text="Łączenie z YouTube...")

    def hook(d):

        if d["status"] == "downloading":

            if d.get("total_bytes"):
                procent = d["downloaded_bytes"] / d["total_bytes"] * 100
                root.after(0, lambda: progress.configure(value=procent))

            elif d.get("total_bytes_estimate"):
                procent = d["downloaded_bytes"] / d["total_bytes_estimate"] * 100
                root.after(0, lambda: progress.configure(value=procent))

            txt = d.get("_percent_str", "").strip()
            root.after(0, lambda: status.config(text=f"Pobieranie {txt}"))

        elif d["status"] == "finished":
            root.after(0, lambda: status.config(text="Scalanie plików..."))

    def praca():

        try:

            ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

            opcje = {
                "format": "bestvideo+bestaudio/best",
                "outtmpl": folder_zapisu + "/%(title)s.%(ext)s",
                "ffmpeg_location": ffmpeg,
                "progress_hooks": [hook],
                "merge_output_format": "mp4"
            }

            with yt_dlp.YoutubeDL(opcje) as ydl:
                info = ydl.extract_info(url, download=True)

            tytul = info["title"]

            root.after(
                0,
                lambda: messagebox.showinfo(
                    "Gotowe",
                    f"Pobrano:\n\n{tytul}"
                )
            )

        except Exception as e:

            root.after(
                0,
                lambda: messagebox.showerror(
                    "Błąd",
                    str(e)
                )
            )

        finally:

            root.after(
                0,
                lambda: (
                    btn_pobierz.config(state="normal"),
                    status.config(text="Gotowy"),
                    progress.configure(value=0)
                )
            )

    threading.Thread(target=praca, daemon=True).start()


# ================= GUI =================

root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("620x260")
root.resizable(False, False)

tk.Label(
    root,
    text="Link do filmu:",
    font=("Arial", 11)
).pack(pady=8)

entry_url = tk.Entry(
    root,
    width=75
)

entry_url.pack()

tk.Button(
    root,
    text="Wybierz folder zapisu",
    command=wybierz_folder
).pack(pady=10)

lbl_folder = tk.Label(
    root,
    text=folder_zapisu,
    fg="blue"
)

lbl_folder.pack()

progress = ttk.Progressbar(
    root,
    length=500,
    mode="determinate"
)

progress.pack(pady=15)

status = tk.Label(
    root,
    text="Gotowy"
)

status.pack()

btn_pobierz = tk.Button(
    root,
    text="Pobierz film",
    bg="red",
    fg="white",
    font=("Arial", 11, "bold"),
    command=pobierz_film
)

btn_pobierz.pack(pady=15)

root.mainloop()