import mysql.connector

# 连接到数据库
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="your_database"
        )
        print("成功连接到数据库")
        return conn
    except mysql.connector.Error as err:
        print(f"连接错误: {err}")
        return None

# 创建表
def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS example_table (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                age INT
            )
        """)
        print("表创建成功")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"创建表错误: {err}")

# 插入数据
def insert_data(conn, name, age):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO example_table (name, age) VALUES (%s, %s)", (name, age))
        conn.commit()
        print("数据插入成功")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"插入数据错误: {err}")

# 查询数据
def fetch_data(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM example_table")
        rows = cursor.fetchall()
        print("查询结果:")
        for row in rows:
            print(row)
        cursor.close()
    except mysql.connector.Error as err:
        print(f"查询数据错误: {err}")

# 主函数
def main():
    # 连接到数据库
    conn = connect_to_database()
    if conn is None:
        return

    # 创建表
    create_table(conn)

    # 插入数据
    insert_data(conn, "Alice", 30)
    insert_data(conn, "Bob", 25)

    # 查询数据
    fetch_data(conn)

    # 关闭连接
    conn.close()

if __name__ == "__main__":
    main()
