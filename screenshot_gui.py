import tkinter as tk
import pyautogui
import time

def take_screenshot():
    name = time.time()
    name = f"{name}.png"
    screenshot = pyautogui.screenshot()
    screenshot.save(name)
    screenshot.show()

def close_app():
    root.destroy()

root = tk.Tk()
root.title("Screenshot Tool")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

screenshot_button = tk.Button(frame, text="Take Screenshot", command=take_screenshot)
screenshot_button.pack()

close_button = tk.Button(frame, text="Close", command=close_app)
close_button.pack()

root.mainloop()
