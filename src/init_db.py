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
    CONSTRAINT Scores_sforeign FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    CONSTRAINT Scores_cforeign FOREIGN KEY (ClassID) REFERENCES Classes(ClassID)
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
    CONSTRAINT Punishtime_sforeign FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    CONSTRAINT Punishtime_pforeign FOREIGN KEY (PunishName) REFERENCES Punishments(PunishName)
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
    CONSTRAINT Prizetime_sforeign FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    CONSTRAINT Prizetime_pforeign FOREIGN KEY (PrizeName) REFERENCES Prizes(PrizeName)
    )
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    
# 存储过程：修改学号
    sql = "DROP PROCEDURE IF EXISTS updateStudentID"
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    sql = """
    CREATE PROCEDURE updateStudentID(IN old_id CHAR(10), IN new_id CHAR(10))
    BEGIN
        ALTER TABLE Scores
        DROP FOREIGN KEY Scores_sforeign;
        
        UPDATE Scores
        SET StudentID = new_id
        WHERE StudentID = old_id;
        
        ALTER TABLE Punishtime
        DROP FOREIGN KEY Punishtime_sforeign;
        
        UPDATE Punishtime
        SET StudentID = new_id
        WHERE StudentID = old_id;

        ALTER TABLE Prizetime
        DROP FOREIGN KEY Prizetime_sforeign;
        
        UPDATE Prizetime
        SET StudentID = new_id
        WHERE StudentID = old_id;

        UPDATE Students
        SET StudentID = new_id
        WHERE StudentID = old_id;
        
        ALTER TABLE Scores
        ADD CONSTRAINT Scores_sforeign FOREIGN KEY (StudentID) REFERENCES Students (StudentID);

        ALTER TABLE Punishtime
        ADD CONSTRAINT Punishtime_sforeign FOREIGN KEY (StudentID) REFERENCES Students (StudentID);

        ALTER TABLE Prizetime
        ADD CONSTRAINT Prizetime_sforeign FOREIGN KEY (StudentID) REFERENCES Students (StudentID);
    END
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
# 存储过程：修改课程号
    sql = "DROP PROCEDURE IF EXISTS updateClassID"
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    sql = """
    CREATE PROCEDURE updateClassID(IN old_id CHAR(10), IN new_id CHAR(10))
    BEGIN
        ALTER TABLE Scores
        DROP FOREIGN KEY Scores_cforeign;
        
        UPDATE Scores
        SET ClassID = new_id
        WHERE ClassID = old_id;

        UPDATE Classes
        SET ClassID = new_id
        WHERE ClassID = old_id;
        
        ALTER TABLE Scores
        ADD CONSTRAINT Scores_cforeign FOREIGN KEY (ClassID) REFERENCES Classes (ClassID);

    END
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
# 存储函数：查询已获得的学生总学分
    sql = "DROP Function IF EXISTS GetTotalPoints"
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    
    sql = """
    CREATE FUNCTION GetTotalPoints (student_id CHAR(10)) RETURNS INT
    DETERMINISTIC
    BEGIN
        DECLARE total_points INT;
        SELECT SUM(Classes.Point) INTO total_points
        FROM Classes
        WHERE ClassID IN (SELECT ClassID FROM Scores WHERE Scores.StudentID = student_id);
        RETURN total_points;
    END
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
# 触发器：删除学生，课程，惩罚，奖项时自动删除相关成绩，日期
    sql = "DROP TRIGGER IF EXISTS trg_delete_student"
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    
    sql = """
    CREATE TRIGGER trg_delete_student
    BEFORE DELETE ON Students
    FOR EACH ROW
    BEGIN
        SELECT COUNT(*) INTO @count FROM Scores WHERE StudentID = OLD.StudentID;
        
        IF @count > 0 THEN
            DELETE FROM Scores WHERE StudentID = OLD.StudentID;
        END IF;
                
        SELECT COUNT(*) INTO @count FROM Punishtime WHERE StudentID = OLD.StudentID;
        
        IF @count > 0 THEN
            DELETE FROM Punishtime WHERE StudentID = OLD.StudentID;
        END IF;
                
        SELECT COUNT(*) INTO @count FROM Prizetime WHERE StudentID = OLD.StudentID;
        
        IF @count > 0 THEN
            DELETE FROM Prizetime WHERE StudentID = OLD.StudentID;
        END IF;
    END
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    
    sql = "DROP TRIGGER IF EXISTS trg_delete_class"
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    
    sql = """
    CREATE TRIGGER trg_delete_class
    BEFORE DELETE ON Classes
    FOR EACH ROW
    BEGIN
        SELECT COUNT(*) INTO @count FROM Scores WHERE ClassID = OLD.ClassID;
        
        IF @count > 0 THEN
            DELETE FROM Scores WHERE ClassID = OLD.ClassID;
        END IF;
    END
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    
    sql = "DROP TRIGGER IF EXISTS trg_delete_punish"
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    
    sql = """
    CREATE TRIGGER trg_delete_punish
    BEFORE DELETE ON Punishments
    FOR EACH ROW
    BEGIN
        SELECT COUNT(*) INTO @count FROM Punishtime WHERE PunishName = OLD.PunishName;
        
        IF @count > 0 THEN
            DELETE FROM Punishtime WHERE PunishName = OLD.PunishName;
        END IF;
              
    END
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return

    sql = "DROP TRIGGER IF EXISTS trg_delete_prize"
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return
    
    sql = """
    CREATE TRIGGER trg_delete_prize
    BEFORE DELETE ON Prizes
    FOR EACH ROW
    BEGIN               
        SELECT COUNT(*) INTO @count FROM Prizetime WHERE PrizeName = OLD.PrizeName;
        
        IF @count > 0 THEN
            DELETE FROM Prizetime WHERE PrizeName = OLD.PrizeName;
        END IF;
    END
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(f"发生错误：{e}")
        db.rollback()
        return