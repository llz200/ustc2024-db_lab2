import pymysql

# 初始化表格
def init(db, cursor):

    # 删除表
    sql = """
    DROP TABLE IF EXISTS Scores
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    sql = """
    DROP TABLE IF EXISTS Punishtime
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    sql = """
    DROP TABLE IF EXISTS Prizetime
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    sql = """
    DROP TABLE IF EXISTS Students 
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    sql = """
    DROP TABLE IF EXISTS Classes
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    sql = """
    DROP TABLE IF EXISTS Prizes
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    sql = """
    DROP TABLE IF EXISTS Punishments
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return

    # 创建表
    sql = """
    CREATE TABLE Students (
    StudentID CHAR(10),
    Name VARCHAR(64) NOT NULL,
    Age INT NOT NULL,
    Major VARCHAR(64) NOT NULL,
    Photo LONGBLOB,
    PRIMARY KEY (StudentID)
    )
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return

    sql = """
    CREATE TABLE Classes (
    ClassID CHAR(10),
    Name VARCHAR(64) NOT NULL,
    Point INT NOT NULL,
    PRIMARY KEY (ClassID)
    )
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    
    sql = """
    CREATE TABLE Scores (
    StudentID CHAR(10),
    ClassID CHAR(10),
    Score INT,
    PRIMARY KEY (StudentID, ClassID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID)
    )
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return

    sql = """
    CREATE TABLE Punishments (
    PunishName VARCHAR(64) NOT NULL,
    PRIMARY KEY (PunishName)
    )
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return

    sql = """
    CREATE TABLE Punishtime (
    StudentID CHAR(10),
    PunishName VARCHAR(64) NOT NULL,
    Date DATE,
    PRIMARY KEY (PunishName),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (PunishName) REFERENCES Punishments(PunishName)
    )
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return

    sql = """
    CREATE TABLE Prizes (
    PrizeName VARCHAR(64) NOT NULL,
    Grade VARCHAR(64),
    PRIMARY KEY (PrizeName)
    )
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return

    sql = """
    CREATE TABLE Prizetime (
    StudentID CHAR(10),
    PrizeName VARCHAR(64) NOT NULL,
    Date DATE,
    PRIMARY KEY (PrizeName),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (PrizeName) REFERENCES Prizes(PrizeName)
    )
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    
