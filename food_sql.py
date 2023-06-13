import sqlite3

# 连接到数据库
conn = sqlite3.connect('点餐系统.db')
c = conn.cursor()

# noinspection SqlDialectInspection,SqlNoDataSourceInspection
c.execute('''CREATE TABLE IF NOT EXISTS users
             (User_id INTEGER PRIMARY KEY AUTOINCREMENT,
             username TEXT NOT NULL CHECK(length(username) >= 8 AND length(username) <= 16),
             password TEXT NOT NULL CHECK(length(password) >= 6 AND length(password) <= 18),
             email TEXT NOT NULL CHECK (email like '%@%'))''')
conn.commit()
# 创建菜单表
# noinspection SqlDialectInspection,SqlNoDataSourceInspection
c.execute('''CREATE TABLE IF NOT EXISTS menu
             (Dish_id INTEGER PRIMARY KEY AUTOINCREMENT,
             dish_name TEXT NOT NULL,
             price REAL NOT NULL)''')
conn.commit()

# 创建订单表
# noinspection SqlDialectInspection,SqlNoDataSourceInspection
c.execute('''CREATE TABLE IF NOT EXISTS orders
             (Order_id INTEGER PRIMARY KEY,
             User_id INTEGER NOT NULL,
             FOREIGN KEY(User_id) REFERENCES users(User_id))''')
conn.commit()

# 创建订单明细表
# noinspection SqlDialectInspection,SqlNoDataSourceInspection
c.execute('''CREATE TABLE IF NOT EXISTS order_details
             (Order_id INTEGER NOT NULL,
             Dish_id INTEGER NOT NULL,
             quantity INTEGER NOT NULL,
             price REAL NOT NULL,
             FOREIGN KEY(Order_id) REFERENCES orders(Order_id),
             FOREIGN KEY(Dish_id) REFERENCES menu(Dish_id))''')
conn.commit()

# 创建账单表
# noinspection SqlDialectInspection,SqlNoDataSourceInspection
c.execute('''CREATE TABLE IF NOT EXISTS bills
             (Order_id INTEGER NOT NULL,
             total_amount REAL NOT NULL,
             FOREIGN KEY(Order_id) REFERENCES orders(Order_id))''')
conn.commit()

# 菜单数据
menu_data = [
    ("番茄炒蛋", 25.0),
    ("宫保虾球", 58.0),
    ("蒜蓉西兰花", 32.0),
    ("麻婆豆腐", 28.9),
    ("水煮鱼", 68.5),
    ("红烧狮子头", 42.0),
    ("干锅排骨", 48.0),
    ("清蒸鲈鱼", 55.9),
    ("椒盐虾", 65.0),
    ("鱼香茄子", 28.0),
    ("蚝油生菜", 22.0),
    ("三杯鸡", 38.0),
    ("香辣蟹", 78.0),
    ("菠萝咕咾肉", 45.0),
    ("青椒牛肉", 48.0),
    ("香煎韭菜盒子", 18.0),
    ("腊肠炒饭", 28.0),
    ("油焖大虾", 68.0),
    ("糖醋鲤鱼", 58.0),
    ("豉椒蒸排骨", 38.0),
    ("蒜泥白肉", 32.0),
    ("剁椒鱼头", 68.0),
    ("麻辣香锅", 56.7),
    ("干煸豆角", 22.3),
    ("东坡肉", 68.9),
    ("小笼包", 15.5),
    ("糖醋排骨", 32.7),
    ("麻辣烫", 20.0),
    ("清蒸鲈鱼", 55.9),
    ("鱼香肉丝", 26.4),
    ("锅贴", 16.8),
    ("京酱肉丝", 42.5),
    ("葱油饼", 12.3),
    ("蛋炒饭", 18.5),
    ("麻辣小龙虾", 88.0),
    ("扬州炒饭", 25.0),
    ("干锅牛蛙", 68.0),
    ("麻辣兔头", 58.0),
    ("水煮肉片", 38.0),
    ("辣子鸡", 48.0),
    ("农家小炒肉", 32.0),
    ("口水鸡", 28.0),
    ("剁椒鱼", 68.0),
    ("麻辣香锅", 56.7)
]

# 懒，先转化为‘集合’再转回‘列表’，达到去重的目的
menu_data = list(set(menu_data))

# 添加菜单数据
for dish_name, price in menu_data:
    # noinspection SqlDialectInspection,SqlNoDataSourceInspection
    c.execute("INSERT INTO menu (dish_name, price) VALUES (?, ?)", (dish_name, price))
    conn.commit()

# 关闭数据库连接
conn.close()

