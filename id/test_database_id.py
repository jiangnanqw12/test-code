import sqlite3
from datetime import datetime

# 连接到SQLite数据库
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 创建表
cursor.execute('''CREATE TABLE IF NOT EXISTS my_table
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT,
                timestamp INTEGER)''')

# 插入数据


def insert_data(category, timestamp):
    cursor.execute(
        "INSERT INTO my_table (category, timestamp) VALUES (?, ?)", (category, timestamp))
    conn.commit()

# 根据时间戳和分类标识生成ID


def generate_id(category, timestamp):
    cursor.execute(
        "SELECT id FROM my_table WHERE category=? AND timestamp=?", (category, timestamp))
    row = cursor.fetchone()
    if row:
        return f"{category}_{row[0]}"
    else:
        return None


# 示例
insert_data('01', int(datetime.now().timestamp()))
generated_id = generate_id('01', int(datetime.now().timestamp()))
print(f"Generated ID: {generated_id}")

# 关闭数据库连接
conn.close()
