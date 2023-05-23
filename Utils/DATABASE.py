import pymysql.cursors

# 本地数据库链接
CONN = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='bs',
    cursorclass=pymysql.cursors.DictCursor
)
