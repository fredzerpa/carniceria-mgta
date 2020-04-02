def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (width / 2))
    y_cordinate = int((screen_height / 2) - (height / 2))

    win.geometry(f"{width}x{height}+{x_cordinate}+{y_cordinate}")


def open_window(win_class, width, height, *class_attr):
    global window
    try:
        if window.root.state() == "normal": window.root.focus()
    except:
        try:
            window = win_class(class_attr[0], class_attr[1])
            center_window(window.root, width, height)
        except IndexError:
            window = win_class()
            center_window(window.root, width, height)
    print(window.root.winfo_geometry())
    print(window.root.winfo_screenwidth())