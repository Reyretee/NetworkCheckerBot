# PingBot

Minecraft sunucusundan gelen oyuncu ping verilerini alan ve işleyen bir bot.

## Özellikler

- TCP üzerinden veri alır.
- Gelen verileri loglar ve SQLite veritabanına kaydeder.
- Modüler yapısı sayesinde kolay genişletilebilir.
- Hem senkron hem de asenkron sunucu desteği.

## Kurulum

1. **Python Yükleyin**: Python 3.7 veya üzeri sürüme sahip olun.


2. **Konfigürasyonu Ayarlayın**:
    - `config/config.py` dosyasını açın ve gerekli ayarları yapın (HOST, PORT, LOG dosyası vb.).

3. **Botu Başlatın**:
    ```bash
    python main.py
    ```

## Kullanım

Minecraft sunucunuzdan gelen ping verilerini botun dinlediği IP ve port'a gönderin. Bot, gelen verileri log dosyasına yazacak ve SQLite veritabanına kaydedecektir.

## Geliştirme

- **Veri İşleme**: `handlers/ping_handler.py` dosyasını düzenleyerek gelen veriler üzerinde ek işlemler yapabilirsiniz.
- **Loglama**: `utils/logger.py` dosyasını düzenleyerek loglama seviyesini ve formatını değiştirebilirsiniz.
- **Sunucu Yönetimi**: `server.py` dosyasında sunucu yönetimi ile ilgili ek özellikler ekleyebilirsiniz.

## Docker ile Çalıştırma

Botu Docker ile çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

## Lisans

MIT Lisansı. Ayrıntılar için `LICENSE` dosyasına bakın.
