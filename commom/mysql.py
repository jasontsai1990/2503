import pymysql

class Mysql():
    def __init__(self, host='localhost', port=3306, user='root', passwd=''):
        try:
            self.conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd)
            self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        except:
            print('database connect error - host: %s' % host)

    def exec(self, sql):
        try:
            self.cursor.execute(sql)
        except:
            print('sql error: %s' % sql)
        return self.cursor

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def close(self):
        self.cursor.close()
        self.conn.close()

