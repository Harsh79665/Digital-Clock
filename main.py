import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("600x260")
root.minsize(450, 200)

is_24h = False
show_sec = True
show_date = True
dark = True
fullscreen = False
on_top = False


def update_time():
    now = datetime.now()
    if is_24h:
        fmt = "%H:%M:%S" if show_sec else "%H:%M"
    else:
        fmt = "%I:%M:%S %p" if show_sec else "%I:%M %p"

    time_label.config(text=now.strftime(fmt))

    if show_date:
        date_label.config(text=now.strftime("%A, %B %d, %Y"))

    root.after(200, update_time)


def toggle_format():
    global is_24h
    is_24h = not is_24h
    btn_format.config(text="12H" if is_24h else "24H")
    update_time()


def toggle_sec():
    global show_sec
    show_sec = not show_sec
    btn_sec.config(text="Show Sec" if not show_sec else "Hide Sec")
    update_time()


def toggle_date():
    global show_date
    show_date = not show_date
    if show_date:
        date_label.pack(pady=(0, 10))
        btn_date.config(text="Hide Date")
    else:
        date_label.pack_forget()
        btn_date.config(text="Show Date")
    update_time()


def toggle_theme():
    global dark
    dark = not dark
    bg = "#1e1e1e" if dark else "#f4f4f4"
    fg = "#00e5ff" if dark else "#222222"
    btn_bg = "#333333" if dark else "#e0e0e0"
    btn_fg = "#ffffff" if dark else "#111111"

    root.config(bg=bg)
    frame.config(bg=bg)
    time_label.config(bg=bg, fg=fg)
    date_label.config(bg=bg, fg="#aaaaaa" if dark else "#555555")
    btn_theme.config(text="Light Mode" if dark else "Dark Mode")

    for btn in buttons:
        btn.config(bg=btn_bg, fg=btn_fg, relief="flat", activebackground=btn_bg, activeforeground=btn_fg)


def toggle_top():
    global on_top
    on_top = not on_top
    root.attributes("-topmost", on_top)
    btn_top.config(text="Unpin" if on_top else "Always on Top")


def toggle_fullscreen(event=None):
    global fullscreen
    fullscreen = not fullscreen
    root.attributes("-fullscreen", fullscreen)
    btn_fs.config(text="Windowed" if fullscreen else "Fullscreen")


def exit_fullscreen(event=None):
    global fullscreen
    if fullscreen:
        fullscreen = False
        root.attributes("-fullscreen", False)
        btn_fs.config(text="Fullscreen")


# Widgets
time_label = tk.Label(root, font=("Consolas", 44, "bold"))
time_label.pack(expand=True)

date_label = tk.Label(root, font=("Segoe UI", 13))
date_label.pack(pady=(0, 10))

frame = tk.Frame(root)
frame.pack(side="bottom", pady=12)

btn_format = tk.Button(frame, text="24H", command=toggle_format, padx=8, pady=3)
btn_theme = tk.Button(frame, text="Light Mode", command=toggle_theme, padx=8, pady=3)
btn_sec = tk.Button(frame, text="Hide Sec", command=toggle_sec, padx=8, pady=3)
btn_date = tk.Button(frame, text="Hide Date", command=toggle_date, padx=8, pady=3)
btn_top = tk.Button(frame, text="Always on Top", command=toggle_top, padx=8, pady=3)
btn_fs = tk.Button(frame, text="Fullscreen", command=toggle_fullscreen, padx=8, pady=3)
btn_exit = tk.Button(frame, text="Exit", command=root.destroy, padx=8, pady=3)

buttons = [btn_format, btn_theme, btn_sec, btn_date, btn_top, btn_fs, btn_exit]
for btn in buttons:
    btn.pack(side="left", padx=3)

root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", exit_fullscreen)

# Initialize theme and start clock
dark = False
toggle_theme()
update_time()

root.mainloop()
