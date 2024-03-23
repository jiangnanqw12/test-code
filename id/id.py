import sqlite3
from time import time

# 连接到SQLite数据库
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 创建表
cursor.execute('''CREATE TABLE IF NOT EXISTS my_table
               (id TEXT PRIMARY KEY, name TEXT)''')

# 生成ID的函数


def generate_id(key_info):
    timestamp = int(time() * 1000)  # 获取当前时间的毫秒级时间戳
    return f"{key_info}_{timestamp}"

# 插入数据的函数


def insert_data(key_info, name):
    id = generate_id(key_info)
    cursor.execute("INSERT INTO my_table (id, name) VALUES (?, ?)", (id, name))
    conn.commit()


# 示例
insert_data('001', 'John Doe')
insert_data('002', 'Jane Doe')

# 查询并打印所有数据
cursor.execute("SELECT * FROM my_table")
print(cursor.fetchall())

# 关闭数据库连接
conn.close()
