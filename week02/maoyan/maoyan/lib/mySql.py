import pymysql

# 记录信息
dbInfo = {
    'host' : '127.0.0.1',
    'port' : 3306,
    'user' : 'root',
    'password' : '*****', # 自己电脑数据库上的密码
    'db' : 'pythontrain'
}

result = []

class ConnDB(object):
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306
        self.user = 'root'
        self.password = '******' # 自己电脑数据库上的密码
        self.db = 'pythontrain'

    def insertData(self, data):
        conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db
        )
        # 游标建立的时候就开启了一个隐形的事物
        cur = conn.cursor()
        try:
            sql = 'INSERT INTO maoyan_top250 (name, type, date) VALUES (\''+data['name']+'\', \''+data['classic']+'\', \''+data['date']+'\')'
            print(sql)
            cur.execute(sql)

            print(cur.fetchone())
            # 关闭游标
            cur.close()
            conn.commit()
        except Exception as e:
            print('Error in sql:')
            print(e)
            print('-------------')
            conn.rollback()
        # 关闭数据库连接
        conn.close()