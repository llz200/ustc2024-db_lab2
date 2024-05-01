import pymysql

# 添加奖项
def add_prize(db, cursor, name, grade):
    sql = "INSERT INTO Prizes (PrizeName, Grade) VALUES (%s, %s)"
    try:
        cursor.execute(sql, (name, grade)) 
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    

# 删除奖项
def delete_prize(db, cursor, name):
    sql = "DELETE FROM Prizes WHERE PrizeName = %s"
    try:
        cursor.execute(sql, (name, )) 
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    
# 创建获奖时间
def add_prizetime(db, cursor, sID, name, date):
    sql = "INSERT INTO Prizetime (StudentID, PrizeName, Date) VALUES (%s, %s, %s)"
    try:
        cursor.execute(sql, (sID, name, date)) 
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    
# 修改获奖时间
def change_prizetime(db, cursor, sID, name, newinf):
    sql = "UPDATE Prizetime SET Date = %s WHERE StudentID = %s AND PrizeName = %s"
    try:
        cursor.execute(sql, (newinf, sID, name)) 
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return    

# 删除获奖时间
def delete_prizetime(db, cursor, sID, name):
    sql = "DELETE FROM Prizetime WHERE StudentID = %s AND PrizeName = %s"
    try:
        cursor.execute(sql, (sID, name)) 
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return