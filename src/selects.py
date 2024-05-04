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