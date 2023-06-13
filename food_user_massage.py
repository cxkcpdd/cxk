import sqlite3
import tkinter as tk
import food_order
from PIL import ImageTk, Image


class Massage:
    i = 0

    def __init__(self, ids):
        self.massage_win = tk.Tk()
        self.id = ids
        self.u_id = ids[0]

    def massage_window(self):
        self.massage_win.title("个人信息")

        # 获取屏幕宽度和高度
        screen_width = self.massage_win.winfo_screenwidth()
        screen_height = self.massage_win.winfo_screenheight()

        # 计算窗口的位置坐标
        window_width = 400
        window_height = 500
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # 设置窗口位置
        self.massage_win.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # 在窗口中放置背景图片(背景)
        image = Image.open("../img/11.png")
        # image = image.resize((60, 45))
        if self.i:
            photo = ImageTk.PhotoImage(image)
            bg_label = tk.Label(self.massage_win, image=photo)
        else:
            photo1 = ImageTk.PhotoImage(image)
            bg_label = tk.Label(self.massage_win, image=photo1)
        self.i += 1

        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # 在窗口中放置背景图片(logo)
        image = Image.open("../img/logo.png")
        image = image.resize((80, 60))
        photo = ImageTk.PhotoImage(image)
        bg_label = tk.Label(self.massage_win, image=photo)
        bg_label.place(x=0, y=0)

        # 账号展示
        a = self.select_username(self.u_id)
        massage_zhanghao = tk.Label(self.massage_win, text=f"账 号：{a}", font=('微软雅黑', 11), width=15, bg="#8193AB")
        massage_zhanghao.place(x=135, y=50)

        # 邮箱展示
        b = self.select_email(self.u_id)
        massage_email = tk.Label(self.massage_win, text=f"邮箱：{b}", font=('微软雅黑', 11), width=20, bg="#8193AB")
        massage_email.place(x=110, y=100)

        # 历史订单提示框
        massage_order = tk.Label(self.massage_win, text=f"历史订单", font=('微软雅黑', 11), width=13, bg='#F0D6E3')
        massage_order.place(x=140, y=150)

        # 历史订单列表
        c = self.select_all_order(self.u_id)
        massage_old = tk.Listbox(self.massage_win)
        massage_old.place(x=50, y=200, width=300, height=200)
        for item in c:
            massage_old.insert(tk.END, f"订单号：{item[0]}      订单金额： {item[1]}  元")

        # 返回点餐按钮
        return_button = tk.Button(self.massage_win, text="返回点餐", command=self.return_order, font=('微软雅黑', 11),
                                  width=15, bg='#E2D4A4')
        return_button.place(x=130, y=430)

        # 主循环
        tk.mainloop()

    # 获取账号
    # noinspection PyMethodMayBeStatic,SqlNoDataSourceInspection
    def select_username(self, u_id):
        # 连接到数据库
        conn = sqlite3.connect('点餐系统.db')
        c = conn.cursor()

        # 执行查询操作获取用户名
        # noinspection SqlDialectInspection
        c.execute("SELECT username FROM users WHERE User_id = ?", (u_id,))
        result = c.fetchone()

        # 关闭数据库连接
        conn.close()

        # 如果查询结果不为空，则返回用户名；否则返回空字符串
        return result[0] if result else ""

    # 获取邮箱
    # noinspection PyMethodMayBeStatic,SqlNoDataSourceInspection
    def select_email(self, u_id):
        # 连接到数据库
        conn = sqlite3.connect('点餐系统.db')
        c = conn.cursor()

        # 执行查询操作获取用户名
        # noinspection SqlDialectInspection
        c.execute("SELECT email FROM users WHERE User_id = ?", (u_id,))
        result = c.fetchone()

        # 关闭数据库连接
        conn.close()

        # 如果查询结果不为空，则返回用户名；否则返回空字符串
        return result[0] if result else ""

    # 获取所有当前ID所点过的单，以及金额
    # noinspection PyMethodMayBeStatic,SqlNoDataSourceInspection
    def select_all_order(self, u_id):
        # 连接到数据库
        conn = sqlite3.connect('点餐系统.db')
        c = conn.cursor()

        # 执行连表查询操作获取订单信息
        # noinspection SqlDialectInspection
        c.execute(
            "SELECT orders.Order_id, bills.total_amount FROM orders JOIN bills ON orders.Order_id = bills.Order_id "
            "WHERE orders.User_id = ?",
            (u_id,))
        order_info = c.fetchall()
        # 关闭数据库连接
        conn.close()

        # 返回订单信息
        return order_info

    # 返回点餐界面
    def return_order(self):
        self.massage_win.destroy()
        p = food_order.Order(self.id)
        p.order_window()
