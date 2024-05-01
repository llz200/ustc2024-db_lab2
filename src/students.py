import pymysql

# 添加学生
def add_student(db, cursor, ID, name, Age, major, image):
    sql = "INSERT INTO Students (StudentID, Name, Age, Major, Photo) VALUES (%s, %s, %s, %s, %s)"
    try:
        cursor.execute(sql, (ID, name, Age, major, image)) 
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    

# 对学生的属性进行修改
def change_student(db, cursor, ID, num, newinf):
    STR = ["StudentID","Name", "Age", "Major", "Photo"]
    sql = "UPDATE Students SET %s = %s WHERE StudentID = %s"
    try:
        cursor.execute(sql, (STR[num], newinf, ID)) 
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return    

# 删除学生
def delete_student(db, cursor, ID):
    sql = "DELETE FROM Students WHERE StudentID = %s"
    try:
        cursor.execute(sql, (ID, )) 
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    
# 创建成绩
def add_score(db, cursor, sID, cID, Score):
    sql = "INSERT INTO Scores (StudentID, ClassID, Score) VALUES (%s, %s, %s)"
    try:
        cursor.execute(sql, (sID, cID, Score)) 
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    
# 修改成绩
def change_score(db, cursor, sID, cID, newinf):
    sql = "UPDATE Scores SET Score = %s WHERE StudentID = %s AND ClassID = %s"
    try:
        cursor.execute(sql, (newinf, sID, cID)) 
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return    

# 删除成绩
def delete_score(db, cursor, sID, cID):
    sql = "DELETE FROM Scores WHERE StudentID = %s AND ClassID = %s"
    try:
        cursor.execute(sql, (sID, cID)) 
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return