from PIL import ImageTk, Image
import food_order
import tkinter as tk
import food_food


# 登录窗口
class Foods:
    i = 0

    def __init__(self, a):
        self.food_button = None
        self.label_password = None
        self.foods_win = tk.Tk()
        self.d = a

    def foods_window(self):

        self.foods_win.title("部分菜单详情")

        # 获取屏幕宽度和高度
        screen_width = self.foods_win.winfo_screenwidth()
        screen_height = self.foods_win.winfo_screenheight()

        # 计算窗口的位置坐标
        window_width = 1000
        window_height = 700
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # 设置窗口位置
        self.foods_win.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # 登录函数，输入账号密码，与数据库内的数据对比查询，查询到了就登录成功
        image_file = ['../img/番茄炒蛋.jpg', '../img/宫保虾球.jpg', '../img/蒜蓉西兰花.jpg', '../img/麻婆豆腐.png', ]
        image_list = []
        for index, file in enumerate(image_file):
            image = Image.open(file).resize((160, 120))
            image = ImageTk.PhotoImage(image)
            image_list.append(image)
        for i in range(len(image_list)):
            tk.Label(self.foods_win, image=image_list[i]).place(x=40, y=i * 160)

        image1_file = ['../img/水煮鱼.jpg', '../img/红烧狮子头.jpg', '../img/干锅排骨.png', '../img/清蒸鲈鱼.png', ]
        image1_list = []
        for index, file in enumerate(image1_file):
            image1 = Image.open(file).resize((160, 120))
            image1 = ImageTk.PhotoImage(image1)
            image1_list.append(image1)
        for i in range(len(image1_list)):
            tk.Label(self.foods_win, image=image1_list[i]).place(x=260, y=i * 160)

        image2_file = ['../img/椒盐虾.jpg', '../img/鱼香茄子.jpg', '../img/蚝油生菜.png', '../img/三杯鸡.png', ]
        image2_list = []
        for index, file in enumerate(image2_file):
            image2 = Image.open(file).resize((160, 120))
            image2 = ImageTk.PhotoImage(image2)
            image2_list.append(image2)
        for i in range(len(image2_list)):
            tk.Label(self.foods_win, image=image2_list[i]).place(x=480, y=i * 160)

        image3_file = ['../img/香辣蟹.jpg', '../img/菠萝咕唠肉.jpg', '../img/青椒牛肉.png', '../img/韭菜盒子.png', ]
        image3_list = []
        for index, file in enumerate(image3_file):
            image3 = Image.open(file).resize((160, 120))
            image3 = ImageTk.PhotoImage(image3)
            image3_list.append(image3)
        for i in range(len(image3_list)):
            tk.Label(self.foods_win, image=image3_list[i]).place(x=700, y=i * 160)

        self.food_button = tk.Button(self.foods_win, text="番茄炒蛋 25.0", font=('微软雅黑', 11), width=12,
                                     command=self.open_food_window,bg="#8193AB")
        self.food_button.place(x=60, y=125, anchor='nw')
        self.label_password = tk.Label(self.foods_win, text="宫保虾球 58.0", font=('微软雅黑', 11), width=12,
                                       bg="#8193AB")
        self.label_password.place(x=60, y=290, anchor='nw')
        self.label_password = tk.Label(self.foods_win, text="蒜蓉西兰花 32.0", font=('微软雅黑', 11), width=12,
                                       bg="#8193AB")
        self.label_password.place(x=60, y=445, anchor='nw')
        self.label_password = tk.Label(self.foods_win, text="麻婆豆腐 28.9", font=('微软雅黑', 11), width=12,
                                       bg="#8193AB")
        self.label_password.place(x=60, y=610, anchor='nw')

        self.label_password = tk.Label(self.foods_win, text="水煮鱼 68.5", font=('微软雅黑', 11), width=12,
                                       bg="#8193AB")
        self.label_password.place(x=285, y=125, anchor='nw')
        self.label_password = tk.Label(self.foods_win, text="红烧狮子头 42.0", font=('微软雅黑', 11), width=12,
                                       bg="#8193AB")
        self.label_password.place(x=285, y=290, anchor='nw')
        self.label_password = tk.Label(self.foods_win, text="干锅排骨 48.0", font=('微软雅黑', 11), width=12,
                                       bg="#8193AB")
        self.label_password.place(x=285, y=445, anchor='nw')
        self.label_password = tk.Label(self.foods_win, text="清蒸鲈鱼 55.9", font=('微软雅黑', 11), width=12,
                                       bg="#8193AB")
        self.label_password.place(x=285, y=610, anchor='nw')

        self.label_password = tk.Label(self.foods_win, text="椒盐虾 65.0", font=('微软雅黑', 11), width=12,
                                       bg="#8193AB")
        self.label_password.place(x=510, y=125, anchor='nw')
        self.label_password = tk.Label(self.foods_win, text="鱼香茄子 28.0", font=('微软雅黑', 11), width=12,
                                       bg="#8193AB")
        self.label_password.place(x=510, y=290, anchor='nw')
        self.label_password = tk.Label(self.foods_win, text="蚝油生菜 22.0", font=('微软雅黑', 11), width=12,
                                       bg="#8193AB")
        self.label_password.place(x=510, y=445, anchor='nw')
        self.label_password = tk.Label(self.foods_win, text="三杯鸡 38.0", font=('微软雅黑', 11), width=12,
                                       bg="#8193AB")
        self.label_password.place(x=510, y=610, anchor='nw')

        self.label_password = tk.Label(self.foods_win, text="香辣蟹  78.0", font=('微软雅黑', 11), width=12,
                                       bg="#8193AB")
        self.label_password.place(x=725, y=125, anchor='nw')
        self.label_password = tk.Label(self.foods_win, text="菠萝咕咾肉 45.0", font=('微软雅黑', 11), width=12,
                                       bg="#8193AB")
        self.label_password.place(x=725, y=290, anchor='nw')
        self.label_password = tk.Label(self.foods_win, text="青椒牛肉 48.0", font=('微软雅黑', 11), width=12,
                                       bg="#8193AB")
        self.label_password.place(x=725, y=445, anchor='nw')
        self.label_password = tk.Label(self.foods_win, text="韭菜盒子 18.0", font=('微软雅黑', 11), width=12,
                                       bg="#8193AB")
        self.label_password.place(x=725, y=610, anchor='nw')

        login_button = tk.Button(self.foods_win, text="返回", font=('楷体', 15), width=10,
                                 command=self.open_order_window,
                                 bg='#E2D4A4')
        login_button.place(x=875, y=600)

        # 主循环
        tk.mainloop()

    def open_order_window(self):
        self.foods_win.destroy()  # 关闭登录窗口
        q = food_order.Order(self.d)
        q.order_window()

    def open_food_window(self):
        self.foods_win.destroy()  # 关闭登录窗口
        q = food_food.Food(self.d)
        q.tomato_window()
