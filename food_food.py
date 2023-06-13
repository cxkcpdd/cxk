from PIL import ImageTk, Image
import food_foods
import tkinter as tk


class Food:
    i = 0

    def __init__(self, b):
        self.label_password = None
        self.food_win = tk.Tk()
        self.c = b

    def tomato_window(self):
        self.food_win.title("番茄炒蛋")

        # 获取屏幕宽度和高度
        screen_width = self.food_win.winfo_screenwidth()
        screen_height = self.food_win.winfo_screenheight()

        # 计算窗口的位置坐标
        window_width = 880
        window_height = 550
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # 设置窗口位置
        self.food_win.geometry(f"{window_width}x{window_height}+{x}+{y}")

        image = Image.open("../img/logo.png")
        image = image.resize((100, 75))
        photo = ImageTk.PhotoImage(image)
        bg_label = tk.Label(self.food_win, image=photo)
        bg_label.place(x=20, y=460)

        image3_file = ['../img/番茄1.jpg', '../img/番茄.png', '../img/番茄3.jpg', '../img/番茄2.jpg']
        image3_list = []
        for index, file in enumerate(image3_file):
            image3 = Image.open(file).resize((200, 170))
            image3 = ImageTk.PhotoImage(image3)
            image3_list.append(image3)
        for i in range(len(image3_list)):
            tk.Label(self.food_win, image=image3_list[i]).place(x=i * 220, y=15)

        self.label_password = tk.Label(self.food_win, text="原料：番茄、鸡蛋、食用油、盐、葱花。", font=('微软雅黑', 11),
                                       bg='#E0D365', width=45, height=2, )
        self.label_password.place(x=5, y=200, anchor='nw')
        self.label_password = tk.Label(self.food_win, text="第1步、准备好食材备用", font=('微软雅黑', 11),
                                       bg='#E3D345', width=45, height=2, )
        self.label_password.place(x=5, y=230, anchor='nw')
        self.label_password = tk.Label(self.food_win, text="第2步 番茄洗净，切丁", font=('微软雅黑', 11),
                                       bg='#E1D445', width=45, height=2, )
        self.label_password.place(x=5, y=260, anchor='nw')
        self.label_password = tk.Label(self.food_win, text="第3步 锅中油预热，放入蛋液，炒好的鸡蛋盛出备用",
                                       font=('微软雅黑', 11),
                                       bg='#E1D445', width=45, height=2)
        self.label_password.place(x=5, y=290, anchor='nw')
        self.label_password = tk.Label(self.food_win, text="第4步、锅中油预热，放入番茄煸炒。", font=('微软雅黑', 11),
                                       bg='#E1D445', width=45, height=2)
        self.label_password.place(x=5, y=320, anchor='nw')

        self.label_password = tk.Label(self.food_win, text="第5步、放入炒好的鸡蛋。", font=('微软雅黑', 11),
                                       bg='#E1D445', width=45, height=2)
        self.label_password.place(x=5, y=350, anchor='nw')
        self.label_password = tk.Label(self.food_win, text="第6步、放入一勺盐。", font=('微软雅黑', 11),
                                       bg='#E1D445', width=45, height=2)
        self.label_password.place(x=5, y=380, anchor='nw')
        self.label_password = tk.Label(self.food_win, text="第7步、放入葱花煸炒一分钟即可出锅。", font=('微软雅黑', 11),
                                       bg='#E1D445', width=45, height=2)
        self.label_password.place(x=5, y=410, anchor='nw')
        self.label_password = tk.Label(self.food_win, text="色泽鲜艳，口味宜人", font=('微软雅黑', 11),
                                       bg='#E1D445', width=45, height=2)
        self.label_password.place(x=440, y=200, anchor='nw')
        self.label_password = tk.Label(self.food_win, text="爽口、开胃，营养搭配合理", font=('微软雅黑', 11),
                                       bg='#E1D445', width=45, height=2)
        self.label_password.place(x=440, y=230, anchor='nw')
        self.label_password = tk.Label(self.food_win, text="提高免疫力，有人体不可或缺的矿物质", font=('微软雅黑', 11),
                                       bg='#E1D445', width=45, height=2)
        self.label_password.place(x=440, y=260, anchor='nw')
        self.label_password = tk.Label(self.food_win, text="营养价值丰富",
                                       font=('微软雅黑', 11),
                                       bg='#E1D445', width=45, height=2)
        self.label_password.place(x=440, y=290, anchor='nw')
        self.label_password = tk.Label(self.food_win, text="具有营养素互补的特点",
                                       font=('微软雅黑', 11),
                                       bg='#E1D445', width=45, height=2)
        self.label_password.place(x=440, y=320, anchor='nw')
        self.label_password = tk.Label(self.food_win, text="以及健美抗衰老的作用",
                                       font=('微软雅黑', 11),
                                       bg='#E1D445', width=45, height=2)
        self.label_password.place(x=440, y=350, anchor='nw')
        self.label_password = tk.Label(self.food_win, text="可有效清除体内自由基，保护细胞",
                                       font=('微软雅黑', 11),
                                       bg='#E1D445', width=45, height=2)
        self.label_password.place(x=440, y=410, anchor='nw')
        self.label_password = tk.Label(self.food_win, text="番茄炒蛋中含有丰富维生素c",
                                       font=('微软雅黑', 11),
                                       bg='#E1D445', width=45, height=2)
        self.label_password.place(x=440, y=380, anchor='nw')
        food_button = tk.Button(self.food_win, text="返回", font=('楷体', 15), width=10,
                                command=self.open_foods_window, bg='#E2D4A4')
        food_button.place(x=740, y=480)
        # 主循环
        tk.mainloop()

    # 打开详情界面
    def open_foods_window(self):
        self.food_win.destroy()  # 关闭登录窗口
        q = food_foods.Foods(self.c)
        q.foods_window()
