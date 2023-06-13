import sqlite3
import tkinter as tk
from tkinter import messagebox
import food_login
import food_user_massage
from PIL import ImageTk, Image
import food_foods


class Order:
    i = 0

    def __init__(self, U_id):
        self.massages = None
        self.entry_order_id = None
        self.massage_listbox = None
        self.order_listbox = None
        self.order_name = None
        self.menu_listbox = None
        self.menu_name = None
        self.order_win = tk.Tk()
        self.name_id = U_id

    # 点餐窗口
    def order_window(self):
        self.order_win.title("点餐")

        # 获取屏幕宽度和高度
        screen_width = self.order_win.winfo_screenwidth()
        screen_height = self.order_win.winfo_screenheight()

        # 计算窗口的位置坐标
        window_width = 850
        window_height = 630
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # 设置窗口位置
        self.order_win.geometry(f"{window_width}x{window_height}+{x}+{y - 20}")

        # 在窗口中放置背景图片(背景)
        image = Image.open("../img/11.png")
        # image = image.resize((60, 45))
        if self.i:
            photo = ImageTk.PhotoImage(image)
            bg_label = tk.Label(self.order_win, image=photo)
        else:
            photo1 = ImageTk.PhotoImage(image)
            bg_label = tk.Label(self.order_win, image=photo1)
        self.i += 1

        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # 在窗口中放置背景图片(logo)
        image = Image.open("../img/logo.png")
        image = image.resize((80, 60))
        photo = ImageTk.PhotoImage(image)
        bg_label = tk.Label(self.order_win, image=photo)
        bg_label.place(x=0, y=0)

        # 菜单提示栏
        self.menu_name = tk.Label(self.order_win, text="菜单", font=('微软雅黑', 15), width=12, bg="#8193AB")
        self.menu_name.place(x=120, y=50)

        # 菜单列表
        self.menu_listbox = tk.Listbox(self.order_win, bg='white')
        self.menu_listbox.place(x=50, y=100, width=320, height=500)

        # 订单提示栏
        self.order_name = tk.Label(self.order_win, text="订单", font=('微软雅黑', 15), width=12, bg="#8193AB")
        self.order_name.place(x=570, y=50)

        # 订单列表
        self.order_listbox = tk.Listbox(self.order_win)
        self.order_listbox.place(x=500, y=100, width=300, height=210)

        # 查询信息列表
        self.massage_listbox = tk.Listbox(self.order_win)
        self.massage_listbox.place(x=500, y=390, width=300, height=210)

        # 添加到订单按钮
        add_button = tk.Button(self.order_win, text="加入订单", command=self.add_to_order, font=('微软雅黑', 11),
                               width=8, bg='#F0D6E3')
        add_button.place(x=400, y=100)

        # 从订单移除按钮
        remove_button = tk.Button(self.order_win, text="菜品移除", command=self.remove_from_order,
                                  font=('微软雅黑', 11), width=8, bg='#F0D6E3')
        remove_button.place(x=400, y=150)

        # 提交订单按钮
        submit_button = tk.Button(self.order_win, text="提交订单", command=self.submit_order, font=('微软雅黑', 11),
                                  width=8, bg='#F0D6E3')
        submit_button.place(x=400, y=200)

        # 个人信息
        massage_button = tk.Button(self.order_win, text="个人信息", command=self.open_massage, font=('微软雅黑', 11),
                                   width=8, bg='#F0D6E3')
        massage_button.place(x=400, y=250)

        # 切换账号
        change_button = tk.Button(self.order_win, text="切换账号", command=self.change_massage, font=('微软雅黑', 11),
                                  width=8, bg='#F0D6E3')
        change_button.place(x=400, y=350)

        # 订单号输入提示框
        label_order_id = tk.Label(self.order_win, text="订 单 号:", font=('微软雅黑', 8), width=8, bg='#F0D6E3')
        label_order_id.place(x=500, y=340)

        # 查询订单文本框
        self.entry_order_id = tk.Entry(self.order_win)
        self.entry_order_id.place(x=570, y=340, width=120)

        # 查询订单按钮
        query_button = tk.Button(self.order_win, text="查询订单", command=self.query_order, font=('微软雅黑', 11),
                                 width=8, bg='#F0D6E3')
        query_button.place(x=700, y=333)

        # 订单详情按钮
        query_button = tk.Button(self.order_win, text="部分菜单", font=('微软雅黑', 11), width=8, bg='#F0D6E3',
                                 command=self.open_foods_window)
        query_button.place(x=400, y=300)

        # 订单打印按钮
        print_button = tk.Button(self.order_win, text="订单打印", font=('微软雅黑', 11), width=10, bg="#8193AB",
                                 command=self.print_order)
        print_button.place(x=400, y=510)

        # 订单ID输入框
        self.entry_order_id = tk.Entry(self.order_win, font=('微软雅黑', 11), width=10)
        self.entry_order_id.place(x=400, y=460)

        # 订单ID提示文本
        order_id_label = tk.Label(self.order_win, text="订单ID：", font=('微软雅黑', 11), bg="#8193AB")
        order_id_label.place(x=400, y=410)

        # 在左侧listbox中展示所有菜品
        self.load_menu()

        # 主循环
        tk.mainloop()

    # 获取菜单数据
    # noinspection SqlNoDataSourceInspection
    def load_menu(self):
        # 连接到数据库
        conn = sqlite3.connect('点餐系统.db')
        c = conn.cursor()

        # noinspection SqlDialectInspection
        c.execute("SELECT * FROM Menu")
        menu_items = c.fetchall()
        for item in menu_items:
            self.menu_listbox.insert(tk.END, f"菜品ID： {item[0]}  菜名： {item[1]}  价格： {item[2]}")
            conn.commit()

        # 关闭数据库连接
        conn.close()

    # 添加菜品到订单
    def add_to_order(self):
        selected_item = self.menu_listbox.curselection()
        if selected_item:
            dish_info = self.menu_listbox.get(selected_item).split()
            dish_id = dish_info[1]
            dish_name = dish_info[3]
            dish_price = dish_info[5]
            self.order_listbox.insert(tk.END, f"菜品ID： {dish_id}  菜名： {dish_name}  价格： {dish_price}")

    # 移除菜品从订单
    def remove_from_order(self):
        selected_item = self.order_listbox.curselection()
        if selected_item:
            self.order_listbox.delete(selected_item)

    # 上传订单
    # noinspection SqlNoDataSourceInspection
    def submit_order(self):
        # 检查订单是否为空
        if self.order_listbox.size() == 0:
            messagebox.showinfo("提示", "您还未点餐，请先选择菜品")
            return

        # 获取用户ID
        user_id = self.name_id[0]

        # 连接到数据库
        conn = sqlite3.connect('点餐系统.db')
        c = conn.cursor()

        # 将订单信息存入订单表
        # noinspection SqlDialectInspection
        c.execute("SELECT * FROM Orders ORDER BY Order_id DESC LIMIT 1")
        conn.commit()
        row = c.fetchone()

        if row is not None:
            order_id = row[0] + 1
        else:
            order_id = 1

        # noinspection SqlDialectInspection
        c.execute("INSERT INTO Orders (User_id, Order_id) VALUES (?, ?)", (user_id, order_id))
        conn.commit()

        # 逐条写入订单明细表
        for item in self.order_listbox.get(0, tk.END):
            dish_id = item.split()[1]
            dish_name = item.split()[3]
            dish_price = item.split()[5]
            # noinspection SqlDialectInspection
            c.execute("INSERT INTO order_details (Order_id, Dish_id, quantity, price) VALUES (?, ?, ?, ?)",
                      (order_id, dish_id, dish_name, dish_price))
            conn.commit()

        # 计算总金额
        total_amount = self.calculate_total_amount(order_id)

        # 将总金额和订单ID存入账单表
        # noinspection SqlDialectInspection
        c.execute("INSERT INTO bills (Order_id, total_amount) VALUES (?, ?)", (order_id, total_amount))
        conn.commit()

        # 提交事务并关闭数据库连接
        conn.close()

        # 构建订单明细字符串
        order_details_str = "\n".join(
            [f"菜品ID：{item.split()[1]}  菜名：{item.split()[3]}  价格：{item.split()[5]}" for item in
             self.order_listbox.get(0, tk.END)])

        # 清空订单列表
        self.order_listbox.delete(0, tk.END)

        # 构建订单信息字符串
        order_info = f"订单ID：{order_id}\n\n订单明细：\n{order_details_str}\n\n总金额：{total_amount}"

        # 弹出新窗口显示订单信息
        messagebox.showinfo("订单信息", order_info)

    # 查询订单
    # noinspection SqlNoDataSourceInspection
    def query_order(self):
        order_id = self.entry_order_id.get()

        # 连接到数据库
        conn = sqlite3.connect('点餐系统.db')
        c = conn.cursor()

        # 查询订单明细
        # noinspection SqlDialectInspection
        c.execute("SELECT * FROM order_details WHERE Order_id = ?", (order_id,))
        order_details = c.fetchall()

        if order_details:
            # 计算总金额
            total_amount = self.calculate_total_amount(order_id)

            # 构建查询结果元组列表
            order_details_tuples = [(f"菜品ID：{item[1]}", f"菜名：{item[2]}", f"价格：{item[3]}") for item in
                                    order_details]

            # 在message_listbox中显示查询结果和总金额
            self.massage_listbox.delete(0, tk.END)  # 清空列表框
            self.massage_listbox.insert(tk.END, f"订单ID：{order_id}")
            self.massage_listbox.insert(tk.END, "")
            self.massage_listbox.insert(tk.END, "订单明细：")
            for item in order_details_tuples:
                self.massage_listbox.insert(tk.END, f"{item[0]} {item[1]} {item[2]} 元")
            self.massage_listbox.insert(tk.END, "")
            self.massage_listbox.insert(tk.END, f"总金额：{total_amount} 元")
        else:
            # 没有找到订单，显示提示信息
            self.massage_listbox.delete(0, tk.END)  # 清空列表框
            self.massage_listbox.insert(tk.END, "未找到该订单")

        # 关闭数据库连接
        conn.close()

    # 计算总金额
    # noinspection PyMethodMayBeStatic,SqlNoDataSourceInspection
    def calculate_total_amount(self, order_id):
        # 连接到数据库
        conn = sqlite3.connect('点餐系统.db')
        c = conn.cursor()

        # 查询订单明细的价格并求和
        # noinspection SqlDialectInspection
        c.execute("SELECT SUM(price) FROM Order_Details WHERE Order_id = ?", (order_id,))
        conn.commit()
        total_amount = c.fetchone()[0]

        # 关闭数据库连接
        conn.close()

        return total_amount

    def open_foods_window(self):
        self.order_win.destroy()  # 关闭登录窗口
        p = food_foods.Foods(self.name_id)
        p.foods_window()

    # 信息窗口函数
    def open_massage(self):
        self.order_win.destroy()
        self.massages = food_user_massage.Massage(self.name_id)
        self.massages.massage_window()

    # 切换账号函数
    def change_massage(self):
        self.order_win.destroy()  # 关闭order窗口
        op = food_login.Login()
        op.login_window()

    # 订单打印
    def print_order(self):
        order_id = self.entry_order_id.get()

        # 连接到数据库
        conn = sqlite3.connect('点餐系统.db')
        c = conn.cursor()

        if order_id == "":
            messagebox.showinfo("提示", "请输入订单ID！")
        else:
            # 查询订单明细
            # noinspection SqlDialectInspection
            c.execute("SELECT * FROM order_details WHERE Order_id = ?", (order_id,))
            order_details = c.fetchall()

            if order_details:
                # 计算总金额
                total_amount = self.calculate_total_amount(order_id)

                # 构建查询结果元组列表
                order_details_tuples = [(f"菜品ID：{item[1]}", f"菜名：{item[2]}", f"价格：{item[3]}") for item in
                                        order_details]

                with open(f"order_{order_id}.txt", "w") as file:
                    file.write("订单号：" + order_id + "\n")
                    for item in order_details_tuples:
                        line = ' '.join(map(str, item)) + "\n"  # 将元组中的每个元素转换为字符串并用空格连接
                        file.write(line)
                    file.write("总金额：" + str(total_amount) + "\n")
                self.massage_listbox.delete(0, tk.END)  # 清空列表框
                self.massage_listbox.insert(tk.END, "打印成功")
            else:
                # 没有找到订单，显示提示信息
                self.massage_listbox.delete(0, tk.END)  # 清空列表框
                self.massage_listbox.insert(tk.END, "未找到该订单")

        # 关闭数据库连接
        conn.close()
