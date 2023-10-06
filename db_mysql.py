#!/usr/bin/env python

# 控制台执行  pip install pymysql  安装 mysql 驱动
import pymysql
from pymysql import cursors


# 声明全局对象用于保存数据库连接
global connection


def __init__():
    """获取数据连接"""
    global connection
    connection = pymysql.connect(
        host="172.27.176.1",
        port=3306,
        user="root",
        passwd="root",
        db="blog",
        charset="utf8",
        cursorclass=cursors.DictCursor)


def close_conn():
    """关闭数据连接"""
    global connection
    if connection is not connection:
        connection.close()
    else:
        connection = None


def test_insert():
    # 1、测试向mysql数据库表中插入数据
    global connection
    if connection is None:
        return
    try:
        # 获取数据库游标
        with connection.cursor() as cursor:
            sql = """
                insert into author(username,password,nickname,email,mobile,bio)
                values('Alex','123456','Pick','Alex@163.com','13667819876','code');
            """
            result = cursor.execute(sql)
            if result == 1:
                print("添加成功")
                # 默认开启事务，没有自动提交，需要手动提交
                connection.commit()
    except pymysql.MySQLError as error:
        print(error)
        connection.rollback()


def test_delete():
    # 2、测试删除mysql数据库表中数据
    global connection
    if connection is None:
        return
    try:
        # 获取数据库游标
        with connection.cursor() as cursor:
            sql = "delete from author where id = %s ;"
            result = cursor.execute(sql, (1277, ))
            if result == 1:
                print("删除成功")
                # 默认开启事务，没有自动提交，需要手动提交
                connection.commit()
            else:
                print("没有找到数据！！")
    except pymysql.MySQLError as error:
        print(error)
        connection.rollback()


def test_update():
    # 3、测试更新mysql数据库表中数据
    global connection
    if connection is None:
        return
    try:
        # 获取数据库游标
        with connection.cursor() as cursor:
            sql = "update author set bio='焦兰殿内 臣弑君，子弑父' where id = %s;"
            result = cursor.execute(sql, (1296, ))
            if result == 1:
                print("修改成功")
                # 默认开启事务，没有自动提交，需要手动提交
                connection.commit()
    except pymysql.MySQLError as error:
        print(error)
        connection.rollback()


def test_select():
    # # 4、测试查询mysql数据库表中数据
    global connection
    if connection is None:
        return
    try:
        # 获取数据库游标
        with connection.cursor() as cursor:
            sql = "select * from author;"
            cursor.execute(sql)

            # 默认的游标类型是元组
            # 获取到一个元组的结果（元组中包含的每一行数据又是一个元组）
            # 可以在获取连接的时候可以指定游标的类型为DictCursor,每一行是一个字典
            # cursor.fetchone()
            # sursor.fetchall()
            # cursor.fetchmany()

            for row in cursor.fetchall():
                print(row["username"], end="\t")
                print(row["password"], end="\t")
                print(row["nickname"], end="\t")
                print(row["email"], end="\t")
                print(row["mobile"], end="\t")
                print(row["bio"], end="\t")
                print("")
            print("-------------------------------------")
    except pymysql.MySQLError as error:
        print(error)


if __name__ == '__main__':
    __init__()
    test_insert()
    test_update()
    test_delete()
    test_select()
    close_conn()
