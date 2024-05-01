# 本文件供学习测试用
import pymysql
import init_db
import students

# 打开数据库连接
try:
    db = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306, autocommit=False)
    #print('连接成功！')
except:
    print('something wrong!')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 切换database到lab2
sql = "USE lab2"
try:
    cursor.execute(sql)
except Exception as e:
    print(f"发生错误：{e}")

init_db.init(db, cursor)

with open('./picture/11z.png', 'rb') as image_file:
    image_blob = image_file.read()

students.add_student(db, cursor, "PB21111716", "牢", 22, "CS", image_blob)

# 关闭游标
cursor.close()

#关闭连接
db.close()