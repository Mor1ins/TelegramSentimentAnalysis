import sqlite3 as lite


# "(1423136, 1, 2, 'hu', 'date', 'text', 2)"
def tuple2str(t):
    return "({}, {}, {}. '{}', '{}', '{}', {})".format(t[0], t[1], t[2], t[3], t[4], t[5], t[6])


class DB:
    def __init__(self, filename):
        global c
        self.tablename = filename.split('.')[0]
        try:
            self.table = lite.connect(filename)
            c = self.table.cursor()
            create = "CREATE TABLE {} (message_id INT NOT NULL, id INT NOT NULL, id_chat INT NOT NULL, name TEXT NOT " \
                     "NULL, date TEXT NOT NULL, text TEXT NOT NULL, tonal INT NOT NULL)".format(self.tablename)
            c.execute(create)
            self.table.commit()
        except:
            pass
        finally:
            c.close()

    # record - строка вида (message_id, id, id_chat, name, date, text, tonal)
    def insert(self, record):
        c = self.table.cursor()
        command = "insert into {} values {}".format(self.tablename, record)
        c.execute(command)

    # record - строка вида (id, id_chat, name, date, text, tonal)
    def update(self, record):
        c = self.table.cursor()
        command = "update {} date='{}' text='{}' tonal={} where message_id={}".format(self.tablename, record[4],
                                                                                      record[5],
                                                                                      record[6], record[0])
        c.execute(command)

    def delete(self, message_id):
        c = self.table.cursor()
        command = "delete from {} where message_id={}".format(self.tablename, message_id)
        c.execute(command)

    def commit(self):
        self.table.commit()

    def close(self):
        self.table.close()

    # def search_by_id(self, id):
    #     conn = lite.connect(self.table)
    #     with conn:
    #         command = "select * from {} where id={}".format(self.table, id)
    #         conn.execute(command)
    #         conn.commit()
    #         conn.close()ц
    #
    #
