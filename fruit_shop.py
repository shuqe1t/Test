import tkinter as tk


def clear():
    for w in root.winfo_children():
        w.destroy()


def show_login():
    clear()
    root.title("Вход")

    tk.Label(root, text="Фруктовый магазин", font=("Arial", 18, "bold")).pack(pady=30)
    tk.Label(root, text="Логин:").pack()
    entry_login = tk.Entry(root, width=25)
    entry_login.pack(pady=5)

    tk.Button(root, text="Войти", width=15,
              command=lambda: show_catalog(entry_login.get())).pack(pady=15)


def show_catalog(login):
    clear()
    root.title("Каталог")

    top = tk.Frame(root, bg="lightgray")
    top.pack(fill="x")
    tk.Button(top, text="Корзина", command=lambda: show_cart(login)).pack(side="left", padx=5, pady=5)
    tk.Button(top, text="Выйти", command=show_login).pack(side="left", padx=5, pady=5)
    tk.Label(top, text=login, bg="lightgray").pack(side="right", padx=10)

    tk.Label(root, text="КАТАЛОГ", font=("Arial", 16, "bold")).pack(pady=15)

    for fruit in ["Помело", "Апельсин", "Слива"]:
        tk.Label(root, text=fruit, font=("Arial", 14), width=25, pady=15,
                 relief="solid", bd=1, bg="white").pack(pady=8)


def show_cart(login):
    clear()
    root.title("Корзина")

    top = tk.Frame(root, bg="lightgray")
    top.pack(fill="x")
    tk.Button(top, text="Назад в каталог", command=lambda: show_catalog(login)).pack(side="left", padx=5, pady=5)
    tk.Label(top, text=login, bg="lightgray").pack(side="right", padx=10)

    tk.Label(root, text="КОРЗИНА", font=("Arial", 16, "bold")).pack(pady=15)
    tk.Label(root, text="Корзина пуста").pack()


root = tk.Tk()
root.geometry("500x450")
show_login()
root.mainloop()
