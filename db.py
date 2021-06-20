#!/usr/bin/python3
import sqlite3

class database:
    def __init__(self):
        self.conn = None
        self.dbFile = './nl.sqlite3'
        self.create_connection()

        sql_create_urls_table = """ CREATE TABLE IF NOT EXISTS translations (
                                        id integer PRIMARY KEY,
                                        en text NOT NULL,
                                        nl text NOT NULL
                                    ); """
        self.create_table(sql_create_urls_table)


    def executeSql(self, sql, args=None):
        cur = self.conn.cursor()
        try:
            if args is not None:
                cur.execute(sql,args)
            else:
                cur.execute(sql)

            if sql.startswith('INSERT'):
                self.conn.commit()
            elif sql.startswith('SELECT'):
                return cur.fetchall()
        except Exception:
            print("SQL EXCEPTION!")
            print("[SQL] ERROR: %s"%(sql) )


    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.dbFile)
            #print(sqlite3.version)
        except Error as e:
            print(e)
        #finally:
        #    if conn:
        #       conn.close()

    def create_table(self, createTableSql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            cur = self.conn.cursor()
            cur.execute(createTableSql)
        except Error as e:
            print(e)

    def exists(self, en):
        sql = 'SELECT id FROM translations WHERE en = ? limit 1;'
        rows = self.executeSql(sql, (en,))
        if len(rows) == 0:
            return False
        else:
            return True

    def done(self, en):
        sql = 'SELECT id FROM translations WHERE en = ? AND done = 1 limit 1;'
        rows = self.executeSql(sql, (en,))
        if len(rows) == 0:
            return False
        else:
            return True

    def addTranslation(self, en, nl):
        sql = 'INSERT INTO translations(en, nl) VALUES(?, ? )'
        self.executeSql(sql, (en, nl))

    def getAll(self):
        sql = 'SELECT id, en, nl, done FROM translations'
        return self.executeSql(sql)

