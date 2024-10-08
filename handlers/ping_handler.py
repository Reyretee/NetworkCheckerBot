from config.config import Config
import mysql.connector

class PingHandler:
    def __init__(self, logger):
        self.logger = logger
        self.db_connection = self.connect_to_db()

    def connect_to_db(self):
        try:
            conn = mysql.connector.connect(
                host=Config.MYSQL_HOST,
                user=Config.MYSQL_USER,
                password=Config.MYSQL_PASSWORD,
                database=Config.MYSQL_DATABASE
            )
            self.logger.info("MySQL veritabanına başarıyla bağlandı.")
            return conn
        except mysql.connector.Error as err:
            self.logger.error(f"MySQL bağlantı hatası: {err}")
            return None
        
    def check_connection(self):
        if self.db_connection is None:
            self.logger.error("Veritabanı bağlantısı kurulamadı Yeniden deneniyor...")
            self.db_connection = self.connect_to_db()

        try:
            self.db_connection.ping(reconnect=True, attempts=3, delay=5)
            self.logger.info("Veritabanı bağlantısı aktif.")
        except mysql.connector.Error as err:
            self.logger.error(f"Veritabanına yeniden bağlanılamadı: {err}")
            self.db_connection = None

    def save_to_database(self, player, ms):
        if self.db_connection is None:
            self.logger.error("Veritabanı bağlantısı yok.")
            return

        try:
            with self.db_connection.cursor() as cursor:
                query = "INSERT INTO Aincrad (player, date, ms) VALUES (%s, UTC_TIMESTAMP(), %s)"
                cursor.execute(query, (player, ms))
                self.db_connection.commit()
                self.logger.info(f"{player} verisi başarıyla kaydedildi.")
        except mysql.connector.Error as err:
            self.logger.error(f"Veritabanına kayıt yapılırken hata oluştu: {err}")