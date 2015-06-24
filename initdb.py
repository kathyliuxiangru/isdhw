#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

from dbconn import db_cursor

def create_db():
    sqlstr = """
    DROP TABLE IF EXISTS course;

    CREATE TABLE IF NOT EXISTS course  (
        cou_sn   INTEGER,     --序号
        cou_no   TEXT,        --学号
        name     TEXT,        --姓名
        birth    TEXT,        --出生日期
        sex      TEXT,        --性别
        grade    TEXT,        --班级
        notes    TEXT,        --说明
        PRIMARY KEY(cou_sn)
    );
    -- CREATE UNIQUE INDEX idx_course_no ON course(cou_no);

    CREATE SEQUENCE seq_cou_sn 
        START 10000 INCREMENT 1 OWNED BY course.cou_sn;

    """
    with db_cursor() as cur :
        cur.execute(sqlstr) # 执行SQL语句
    
def init_data():
    sqlstr = """
    DELETE FROM course;
    INSERT INTO course (cou_sn, cou_no, name, birth, sex, grade)  VALUES 
        (101, '1310601',  '糖饼', '19950101', '女', '化学1301'), 
        (102, '1310602',  '小梦', '19950102', '女', '化学1302');

   
    """
    with db_cursor() as cur :
        cur.execute(sqlstr)    

if __name__ == '__main__':
    create_db()
    init_data()
    print('数据库已初始化完毕！')

