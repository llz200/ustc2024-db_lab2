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
    if (num == 1):
        sql = "UPDATE Students SET Name = %s WHERE StudentID = %s"
    if (num == 2):
        sql = "UPDATE Students SET Age = %s WHERE StudentID = %s"
    if (num == 3):
        sql = "UPDATE Students SET Major = %s WHERE StudentID = %s"
    if (num == 4):
        sql = "UPDATE Students SET Photo = %s WHERE StudentID = %s"
    try:
        cursor.execute(sql, (newinf, ID)) 
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
    
# 修改学号
def changeid_student(db, cursor, oldID, newID):
    sql = "CALL updateStudentID(%s, %s)"
    try:
        cursor.execute(sql, (oldID, newID)) 
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return

# 查询已获得总学分
def get_total_points(db, cursor, ID):
    sql = "SELECT GetTotalPoints(%s) as TotalCredits"
    try:
        cursor.execute(sql, (ID, )) 
        result = cursor.fetchone()
        return result
    except Exception as e:
        print(f"发生错误：{e}")
        return