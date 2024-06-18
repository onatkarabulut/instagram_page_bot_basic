# Instagram Bot

Bu proje, Instagram API'sini kullanarak çeşitli işlevleri yerine getiren bir bot içerir.

## Kurulum

1. Gerekli bağımlılıkları yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

2. `.env` dosyasını oluşturun ve Instagram kullanıcı adı, şifrenizi ve hedef hesaplarınızı ekleyin:
    ```env
    USERNAME=your_username
    PASSWORD=your_password
    TARGET_ACCOUNTS=account1,account2,account3
    ```

## Kullanım

Ana scripti çalıştırın:
```bash
python main.py
