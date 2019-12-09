import pymysql.cursors
from core.settings import DATABASES

class MySQLClient:

    def __init__(self, *, 
                host=DATABASES['default']['HOST'], 
                user=DATABASES['default']['USER'], 
                password=DATABASES['default']['PASSWORD'], 
                db=DATABASES['default']['NAME'], 
                charset='utf8'):

        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.connect = None

    def is_connect(self):
        return (self.connect != None)

    def open(self):
        self.connect = pymysql.connect(
                            host=self.host,
                            user=self.user,
                            password=self.password,
                            db=self.db,
                            charset=self.charset,
                            cursorclass=pymysql.cursors.DictCursor)
        
        return self

    def exec(self, query):
        print('exec query is ： {0}'.format(query))

        results = []
        if self.is_connect():
            with self.connect.cursor() as c:
                c.execute(query)
            
            if 'select' in query or 'SELECT' in query:
                results = c.fetchall()
            elif 'insert' in query or 'INSERT':
                self.connect.commit()

        return results

    def close(self):
        if self.is_connect():
            self.connect.close()