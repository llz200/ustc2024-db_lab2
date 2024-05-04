import pymysql

# 查询某个学生的基本信息
def select_student_baseinfo(db, cursor, ID):
    sql = "SELECT * FROM Students WHERE StudentID = %s"
    try:
        cursor.execute(sql, (ID, )) 
        student_info = cursor.fetchone()
        return student_info
    except Exception as e:
        print(f"发生错误：{e}")
        return
    
# 查询某个学生获得的奖项
def select_student_prizes(db, cursor, ID):
    sql = "SELECT * FROM Prizetime WHERE StudentID = %s"
    try:
        cursor.execute(sql, (ID, )) 
        student_info = cursor.fetchall()
        return student_info
    except Exception as e:
        print(f"发生错误：{e}")
        return
    
# 查询某个学生获得的惩罚
def select_student_punish(db, cursor, ID):
    sql = "SELECT * FROM Punishtime WHERE StudentID = %s"
    try:
        cursor.execute(sql, (ID, )) 
        student_info = cursor.fetchall()
        return student_info
    except Exception as e:
        print(f"发生错误：{e}")
        return
    
# 查询某个学生的全部成绩
def select_student_score(db, cursor, ID):
    sql = "SELECT * FROM Scores WHERE StudentID = %s"
    try:
        cursor.execute(sql, (ID, )) 
        Scores = cursor.fetchall()
        return Scores
    except Exception as e:
        print(f"发生错误：{e}")
        return
        
# 查询某个学生在某门课上的成绩
def select_student_class_score(db, cursor, sID, cID):
    sql = "SELECT * FROM Scores WHERE StudentID = %s AND ClassID = %s"
    try:
        cursor.execute(sql, (sID, cID)) 
        Score = cursor.fetchone()
        return Score
    except Exception as e:
        print(f"发生错误：{e}")
        return

# 查询某个学生某个奖项
def select_student_prize_one(db, cursor, ID, name):
    sql = "SELECT * FROM Prizetime WHERE StudentID = %s AND PrizeName = %s"
    try:
        cursor.execute(sql, (ID, name)) 
        student_info = cursor.fetchone()
        return student_info
    except Exception as e:
        print(f"发生错误：{e}")
        return
    
# 查询某个学生某个惩罚
def select_student_punish_one(db, cursor, ID, name):
    sql = "SELECT * FROM Punishtime WHERE StudentID = %s AND PunishName = %s"
    try:
        cursor.execute(sql, (ID, name)) 
        student_info = cursor.fetchone()
        return student_info
    except Exception as e:
        print(f"发生错误：{e}")
        return

# 查询学生列表
def select_students_all(db, cursor):
    sql = "SELECT * FROM Students"
    try:
        cursor.execute(sql) 
        student_info = cursor.fetchall()
        return student_info
    except Exception as e:
        print(f"发生错误：{e}")
        return
    
# 查询课程列表
def select_classes_all(db, cursor):
    sql = "SELECT * FROM Classes"
    try:
        cursor.execute(sql) 
        student_info = cursor.fetchall()
        return student_info
    except Exception as e:
        print(f"发生错误：{e}")
        return

# 查询奖项列表
def select_prize_all(db, cursor):
    sql = "SELECT * FROM Prizes"
    try:
        cursor.execute(sql) 
        student_info = cursor.fetchall()
        return student_info
    except Exception as e:
        print(f"发生错误：{e}")
        return
    
# 查询惩罚列表
def select_punish_all(db, cursor):
    sql = "SELECT * FROM Punishments"
    try:
        cursor.execute(sql) 
        student_info = cursor.fetchall()
        return student_info
    except Exception as e:
        print(f"发生错误：{e}")
        return
    
# 按名字查询学生
def select_students_name(db, cursor, name):
    sql = "SELECT * FROM Students WHERE Name = %s"
    try:
        cursor.execute(sql, (name, )) 
        student_info = cursor.fetchall()
        return student_info
    except Exception as e:
        print(f"发生错误：{e}")
        return
    
# 按课程号查询课程
def select_class_ID(db, cursor, ID):
    sql = "SELECT * FROM Classes WHERE ClassID = %s"
    try:
        cursor.execute(sql, (ID, )) 
        student_info = cursor.fetchone()
        return student_info
    except Exception as e:
        print(f"发生错误：{e}")
        return
    
# 按名字查询奖项
def select_prize_name(db, cursor, name):
    sql = "SELECT * FROM Prizes WHERE PrizeName = %s"
    try:
        cursor.execute(sql, (name, )) 
        student_info = cursor.fetchone()
        return student_info
    except Exception as e:
        print(f"发生错误：{e}")
        return
    
# 按名字查询惩罚
def select_punish_name(db, cursor, name):
    sql = "SELECT * FROM Punishments WHERE PunishName = %s"
    try:
        cursor.execute(sql, (name, )) 
        student_info = cursor.fetchone()
        return student_info
    except Exception as e:
        print(f"发生错误：{e}")
        return