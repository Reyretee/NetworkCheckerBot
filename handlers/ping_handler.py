import sqlite3
import logging

class PingHandler:
    def __init__(self, logger, db_path='ping_data.db'):
        self.logger = logger
        self.db_path = db_path
        self.setup_database()

    def setup_database(self):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS ping_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    player TEXT NOT NULL,
                    ping INTEGER NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
                '''
            )
            conn.commit()
            conn.close()
            self.logger.info("Veritabanı kuruldu.")
        except Exception as e:
            self.logger.error(f"Veritabanı kurulumunda bir hata oluştu: {e}")

    def process_ping_data(self, data):
        try:
            lines = data.strip().split('\n')
            ping_data = []
            for line in lines:
                if ':' in line:
                    player, ping = line.split(':', 1)
                    ping_data.append((player.strip(), int(ping.strip())))
                else:
                    self.logger.warning(f"Geçersiz format: {line}")
            
            self.save_to_database(ping_data)
            
            self.logger.info("Gelen veriler:")
            for player, ping in ping_data:
                self.logger.info(f"{player}: {ping}ms")

        except Exception as e:
            self.logger.error(f"Ping verisi işlenemedi: {e}")

    def save_to_database(self, ping_data):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.executemany(
                '''
                INSERT INTO ping_data (player, ping) VALUES (?, ?)
                ''', ping_data
            )
            conn.commit()
            conn.close()
            self.logger.debug("Ping verileri kaydedildi.")
        except sqlite3.Error as e:
            self.logger.error(f"Veritabanına kayıt yapılırken bir hata oluştu: {str(e)}")


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('NetworkCheckerBot')

ping_handler = PingHandler(logger)