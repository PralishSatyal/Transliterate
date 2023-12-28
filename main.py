import tkinter as tk
from Lib.translater import TransliteratorApp


def main():
    root = tk.Tk()
    app = TransliteratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
