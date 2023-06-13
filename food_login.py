import sqlite3
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import food_register
import food_order


# 登录窗口
class Login:
    i = 0

    def __init__(self):
        self.entry_password = None
        self.label_password = None
        self.entry_username = None
        self.label_username = None
        self.label1_username = None
        self.login_win = tk.Tk()

    def login_window(self):

        self.login_win.title("登录")

        # 获取屏幕宽度和高度
        screen_width = self.login_win.winfo_screenwidth()
        screen_height = self.login_win.winfo_screenheight()

        # 计算窗口的位置坐标
        window_width = 500
        window_height = 400
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # 设置窗口位置
        self.login_win.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # 在窗口中放置背景图片(背景)
        image = Image.open("../img/11.png")

        if self.i:
            photo = ImageTk.PhotoImage(image)
            bg_label = tk.Label(self.login_win, image=photo)
        else:
            photo1 = ImageTk.PhotoImage(image)
            bg_label = tk.Label(self.login_win, image=photo1)
        self.i += 1

        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # 在窗口中放置背景图片(logo)
        image = Image.open("../img/logo.png")
        image = image.resize((60, 45))
        photo = ImageTk.PhotoImage(image)
        bg_label = tk.Label(self.login_win, image=photo)
        bg_label.place(x=0, y=0)

        # 系统名
        self.label1_username = tk.Label(self.login_win, text="老班长点餐", font=('楷体', 28), width=12, bg='#C6D1DB')
        self.label1_username.place(x=130, y=60, anchor='nw')

        # 账号输入提示框和输入框
        self.label_username = tk.Label(self.login_win, text="账  号 :", font=('微软雅黑', 15), width=8, bg="#8193AB")
        self.label_username.place(x=105, y=150, anchor='nw')
        self.entry_username = tk.Entry(self.login_win, font=('微软雅黑', 15), width=15)
        self.entry_username.place(x=220, y=150, anchor='nw')

        # 密码输入提示框和输入框
        self.label_password = tk.Label(self.login_win, text="密  码 :", font=('微软雅黑', 15), width=8, bg="#8193AB")
        self.label_password.place(x=105, y=200, anchor='nw')
        self.entry_password = tk.Entry(self.login_win, show="*", font=('微软雅黑', 15), width=15)
        self.entry_password.place(x=220, y=200, anchor='nw')

        # 登录按钮
        login_button = tk.Button(self.login_win, text="登 录", font=('微软雅黑', 15), width=15, command=self.login,
                                 bg='#E2D4A4')
        login_button.place(x=165, y=260)

        # 注册按钮
        register_button = tk.Button(self.login_win, text="注  册", font=('微软雅黑', 15), width=15,
                                    command=self.open_register_window, bg='#E2D4A4')
        register_button.place(x=165, y=320)

        # 主循环
        tk.mainloop()

    # 登录函数，输入账号密码，与数据库内的数据对比查询，查询到了就登录成功
    # noinspection SqlNoDataSourceInspection
    def login(self):
        # 连接到数据库
        conn = sqlite3.connect('点餐系统.db')
        c = conn.cursor()

        username = self.entry_username.get()
        password = self.entry_password.get()

        # noinspection SqlDialectInspection
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        # 如果账号密码匹配到了，c.fetchone()为Ture否则为False
        user = c.fetchone()

        if user:
            # messagebox.showinfo("登录成功", "登录成功！")
            self.login_win.destroy()
            # 关闭数据库连接
            conn.close()
            p = food_order.Order(user)
            p.order_window()
        else:
            messagebox.showerror("登录失败", "用户名或密码错误。")

    def open_register_window(self):
        self.login_win.destroy()
        p = food_register.Register()
        p.register_window()
