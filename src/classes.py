import pymysql

# 添加课程
def add_class(db, cursor, ID, name, point):
    sql = "INSERT INTO Classes (ClassID, Name, Point) VALUES (%s, %s, %s)"
    try:
        cursor.execute(sql, (ID, name, point)) 
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    

# 对课程的属性进行修改
def change_class(db, cursor, ID, num, newinf):
    STR = ["ClassID","Name", "Point"]
    sql = "UPDATE Classes SET %s = %s WHERE ClassID = %s"
    try:
        cursor.execute(sql, (STR[num], newinf, ID)) 
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return    

# 删除课程
def delete_class(db, cursor, ID):
    sql = "DELETE FROM Classes WHERE ClassID = %s"
    try:
        cursor.execute(sql, (ID, )) 
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    