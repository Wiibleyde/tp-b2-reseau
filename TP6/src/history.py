import mysql.connector

class History:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        self.db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def disconnect(self):
        self.db.close()

    def insert(self, data):
        self.connect()
        cursor = self.db.cursor()
        sql = "INSERT INTO history (date, time, temperature, humidity) VALUES (%s, %s, %s, %s)"
        val = (data['date'], data['time'], data['temperature'], data['humidity'])
        cursor.execute(sql, val)
        self.db.commit()
        self.disconnect()

    def select(self):
        self.connect()
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM history")
        result = cursor.fetchall()
        self.disconnect()
        return result

    def delete(self):
        self.connect()
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM history")
        self.db.commit()
        self.disconnect()