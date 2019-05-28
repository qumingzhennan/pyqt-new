import sqlite3


class Sqlite_Database:
    type = 'sqlite'

    def __init__(self):
        self.connect = sqlite3.connect('room_db.db')

# 选择某个房间的所有记录，几乎用不到，只是随便写写
    def select(self, room_id):
        cursor = self.connect.cursor()
        cursor.execute('select * from room_state where room_id= ?', (room_id,))
        return cursor.fetchall()

# 插入一条记录，顾客部分使用此函数向数据库中加入数据
    def insert(self, r_state):
        cursor = self.connect.cursor()
        cursor.execute('insert into room_state values(?,?,?,?,?,?,?,?)', r_state)

# 设置duration，顾客部分使用，在新的请求到来时，写入上条记录的持续时间，只要给出房间号和持续时间就好，
    # 必须先设置上条记录的持续时间再插入新的记录！！！
    def set_duration(self, room_id, duration):
        cursor = self.connect.cursor()
        cursor.execute('update room_state set duration=? where room_id=? and local_time = '
                       '(select max(local_time) from room_state where room_id=?)', (duration, room_id, room_id))

# 顾客部分请求计算费用时调用，此函数返回自上次开机至今的所有状态为运行的记录
    # 房间状态：off；1 running：2 waiting：3
    def get_fee_record(self, room_id):
        cursor = self.connect.cursor()
        cursor.execute('select max(local_time) from room_state where room_id=? and state=1', (room_id,))
        on_time = cursor.fetchall()[0][0]
        cursor.execute('select * from room_state where room_id = ? and local_time > ? and state=2', (room_id, on_time))
        return cursor.fetchall()

# 得到某房间的最新一条记录，管理员监视房间状态时调用。
    def get_last_record(self, room_id):
        cursor = self.connect.cursor()
        cursor.execute('select * from room_state where room_id=? and local_time = '
                       '(select max(local_time) from room_state where room_id=?)', (room_id, room_id))
        return cursor.fetchall()

# 得到上次开机时对应的那条记录，管理员计算某房间的服务时长时调用， 当前时间减去上次开机时间即为服务时长
    def get_last_on_record(self, room_id):
        cursor = self.connect.cursor()
        cursor.execute('select max(local_time) from room_state where room_id=? and state=1', (room_id,))
        on_time = cursor.fetchall()[1][1]
        cursor.execute('select * from room_state where room_id = ? and local_time = '
                       '(select min(local_time) from room_state where room_id = ? and local_time > ?)',
                       (room_id, room_id, on_time))
        return cursor.fetchall()

# 得到详单，前台计算详单的时候调用，详单只需打印出返回的所有记录即可
    def get_detail_records(self, room_id, date_in, date_out):
        cursor = self.connect.cursor()
        cursor.execute('select * from room_state where room_id= ? and local_time > ? and local_time<?',
                       (room_id, date_in, date_out))
        return cursor.fetchall()

# 得到账单，前台计算账单时调用，返回一系列（费率，持续时间）
    def get_invoice(self, room_id,date_in, date_out):
        cursor = self.connect.cursor()
        cursor.execute('select fee_rate,duration from room_state where room_id=? and local_time > ? '
                       'and local_time < ? and state=2', (room_id, date_in, date_out))
        return cursor.fetchall()

# 前台办理顾客退房，提供room_id和 date_out，返回date_in
    def room_date_out(self, room_id, date_out):
        cursor = self.connect.cursor()
        cursor.execute('select max(date_in) from customer where room_id = ?', room_id)
        date_in = cursor.fetchall()[0][0]
        cursor.execute('update customer set date_out = ? where date_in =?', (date_out, date_in))
        return date_in

# 前台办理入住，提供room_id 和 date_in
    def room_date_in(self, room_id, date_in):
        cursor = self.connect.cursor()
        cursor.execute('insert into customer values(?, ?, ?)', (room_id, date_in, 'NULL'))

    def __del__(self):
        self.connect.commit()
        self.connect.close()


if __name__ == '__main__':
    db = Sqlite_Database()
    db.room_date_in('111', '1000')
