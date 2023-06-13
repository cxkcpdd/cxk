import re
import sqlite3
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import food_login


class Register:
    i = 0

    def __init__(self):
        self.label2_username = None
        self.entry_email = None
        self.label_email = None
        self.entry_password = None
        self.label_password = None
        self.entry_username = None
        self.label_username = None
        self.register_win = tk.Tk()

    # 注册窗口
    def register_window(self):
        self.register_win.title("注册")

        # 获取屏幕宽度和高度
        screen_width = self.register_win.winfo_screenwidth()
        screen_height = self.register_win.winfo_screenheight()

        # 计算窗口的位置坐标
        window_width = 500
        window_height = 450
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # 设置窗口位置
        self.register_win.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # 在窗口中放置背景图片(背景)
        image = Image.open("../img/11.png")
        # image = image.resize((60, 45))
        if self.i:
            photo = ImageTk.PhotoImage(image)
            bg_label = tk.Label(self.register_win, image=photo)
        else:
            photo1 = ImageTk.PhotoImage(image)
            bg_label = tk.Label(self.register_win, image=photo1)
        self.i += 1

        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # 在窗口中放置背景图片(logo)
        image = Image.open("../img/logo.png")
        image = image.resize((60, 45))
        photo = ImageTk.PhotoImage(image)
        bg_label = tk.Label(self.register_win, image=photo)
        bg_label.place(x=0, y=0)

        self.label2_username = tk.Label(self.register_win, text="老班长点餐", font=('楷体', 28), width=12, bg='#C6D1DB')
        self.label2_username.place(x=130, y=60, anchor='nw')

        # 账号提示框和输入框
        self.label_username = tk.Label(self.register_win, text="账  号 ：", font=('微软雅黑', 15), width=8, bg="#8193AB")
        self.label_username.place(x=105, y=150, anchor='nw')
        self.entry_username = tk.Entry(self.register_win, font=('微软雅黑', 15), width=15)
        self.entry_username.place(x=220, y=150, anchor='nw')

        # 密码提示框和输入框
        self.label_password = tk.Label(self.register_win, text="密  码 ：", font=('微软雅黑', 15), width=8, bg="#8193AB")
        self.label_password.place(x=105, y=200, anchor='nw')
        self.entry_password = tk.Entry(self.register_win, show="*", font=('微软雅黑', 15), width=15)
        self.entry_password.place(x=220, y=200, anchor='nw')

        # 邮箱提示框和输入框
        self.label_email = tk.Label(self.register_win, text="邮  箱：", font=('微软雅黑', 15), width=8, bg="#8193AB")
        self.label_email.place(x=105, y=250, anchor='nw')
        self.entry_email = tk.Entry(self.register_win, font=('微软雅黑', 15), width=15)
        self.entry_email.place(x=220, y=250, anchor='nw')

        # 注册提交按钮
        register_button = tk.Button(self.register_win, text="注  册", font=('微软雅黑', 15), width=15,
                                    command=self.register, bg='#E2D4A4')
        register_button.place(x=170, y=310)

        # 返回登录按钮
        return_login_button = tk.Button(self.register_win, text="返回登录", font=('微软雅黑', 15), width=15,
                                        command=self.return_login, bg='#E2D4A4')
        return_login_button.place(x=170, y=370)

        # 主循环
        tk.mainloop()

    # 注册信息录入函数
    # noinspection SqlNoDataSourceInspection
    def register(self):
        # 连接到数据库
        conn = sqlite3.connect('点餐系统.db')
        c = conn.cursor()

        # 获取注册时输入的数据
        username = self.entry_username.get()
        password = self.entry_password.get()
        email = self.entry_email.get()

        # 检查输入信息是否满足限定要求
        if not (8 <= len(username) <= 16):
            messagebox.showerror("注册失败", "用户名长度应为 8 到 16 个字符。")
            return
        if not (6 <= len(password) <= 18):
            messagebox.showerror("注册失败", "密码长度应为 6 到 18 个字符。")
            return
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("注册失败", "请输入有效的邮箱地址。")
            return
        try:
            # noinspection SqlDialectInspection
            c.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                      (username, password, email))
            conn.commit()
            messagebox.showinfo("注册成功", "注册成功！")
            # 关闭注册窗口
            self.register_win.destroy()
            # 打开登录窗口
            p = food_login.Login()
            p.login_window()
        except sqlite3.IntegrityError:
            messagebox.showerror("注册失败", "用户名已存在，请尝试其他用户名。")

    # 返回登录函数
    def return_login(self):
        # 关闭注册窗口
        self.register_win.destroy()
        # 打开登录窗口
        p = food_login.Login()
        p.login_window()
