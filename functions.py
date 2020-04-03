def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (width / 2))
    y_cordinate = int((screen_height / 2) - (height / 2))

    win.geometry(f"{width}x{height}+{x_cordinate}+{y_cordinate}")

