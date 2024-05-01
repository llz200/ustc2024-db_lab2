import pymysql

# 添加惩罚
def add_punishment(db, cursor, name):
    sql = "INSERT INTO Punishments (PunishName) VALUES (%s)"
    try:
        cursor.execute(sql, (name, )) 
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    

# 删除惩罚
def delete_punishment(db, cursor, name):
    sql = "DELETE FROM Punishments WHERE PunishName = %s"
    try:
        cursor.execute(sql, (name, )) 
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    
# 创建获惩时间
def add_punishtime(db, cursor, sID, name, date):
    sql = "INSERT INTO Punishtime (StudentID, PunishName, Date) VALUES (%s, %s, %s)"
    try:
        cursor.execute(sql, (sID, name, date)) 
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    
# 修改获惩时间
def change_punishtime(db, cursor, sID, name, newinf):
    sql = "UPDATE Punishtime SET Date = %s WHERE StudentID = %s AND PunishName = %s"
    try:
        cursor.execute(sql, (newinf, sID, name)) 
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return    

# 删除获惩时间
def delete_punishtime(db, cursor, sID, name):
    sql = "DELETE FROM Punishtime WHERE StudentID = %s AND PunishName = %s"
    try:
        cursor.execute(sql, (sID, name)) 
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return