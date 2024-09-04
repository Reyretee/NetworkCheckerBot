class PingHandler:
    def __init__(self, logger):
        self.logger = logger

    def process_ping_data(self, data):
        try:
            lines = data.strip().split('\n')
            ping_data = {}
            for line in lines:
                if ':' in line:
                    player, ping = line.split(':', 1)
                    ping_data[player.strip()] = int(ping.strip())
                else:
                    self.logger.warning(f"Geçersiz format: {line}")
            
            self.logger.info("Gelen veriler:")
            for player, ping in ping_data.items():
                self.logger.info(f"{player}: {ping}ms")

        except Exception as e:
            self.logger.error(f"Ping verisi işlenemedi: {e}")