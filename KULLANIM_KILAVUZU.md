# Kapak İndirici - Kullanım Kılavuzu

## İçindekiler
1. [Giriş](#giriş)
2. [Kurulum](#kurulum)
3. [Arayüz Tanıtımı](#arayüz-tanıtımı)
4. [Oyun Kapakları İndirme](#oyun-kapakları-indirme)
5. [Film Kapakları İndirme](#film-kapakları-indirme)
6. [PDF Oluşturma](#pdf-oluşturma)
7. [Metin Düzenleme](#metin-düzenleme)
8. [Sık Sorulan Sorular](#sık-sorulan-sorular)
9. [Hata Çözümleri](#hata-çözümleri)

## Giriş

Kapak İndirici, oyun ve film kapaklarını otomatik olarak indirmenizi sağlayan kapsamlı bir araçtır. Bu kılavuz, uygulamanın tüm özelliklerini detaylı bir şekilde açıklamaktadır.

## Kurulum

### Sistem Gereksinimleri
- Python 3.8 veya üzeri
- İnternet bağlantısı
- En az 1GB boş disk alanı

### Kurulum Adımları
1. Python'u [python.org](https://python.org) adresinden indirin ve kurun
2. Projeyi bilgisayarınıza indirin
3. Komut satırında proje dizinine gidin
4. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```
5. Uygulamayı başlatın:
```bash
python main.py
```

## Arayüz Tanıtımı

Uygulama dört ana sekmeden oluşmaktadır:

### 1. Oyunlar Sekmesi
- Oyun listesi seçme
- Kapak indirme
- İndirme durumu takibi

### 2. Filmler Sekmesi
- Film listesi seçme
- Kapak indirme
- İngilizce isim dönüştürme
- İndirme durumu takibi

### 3. PDF Oluşturucu Sekmesi
- Resim seçme
- Sayfa düzeni ayarları
- PDF oluşturma

### 4. Metin Düzenleyici Sekmesi
- Metin dosyası seçme
- Metin düzenleme
- Sıralama ve temizleme
- Kaydetme

## Oyun Kapakları İndirme

### Oyun Listesi Hazırlama
1. Oyun isimlerini bir metin dosyasına yazın
2. Her satıra bir oyun ismi gelecek şekilde düzenleyin
3. Dosyayı UTF-8 kodlaması ile kaydedin

### Kapak İndirme
1. "Oyunlar" sekmesine geçin
2. "Oyun Listesi Seç" butonuna tıklayın
3. Hazırladığınız dosyayı seçin
4. "Oyun Kapaklarını İndir" butonuna tıklayın
5. İndirme işlemi başlayacaktır

### İndirme Sonrası
- Başarılı indirmeler yeşil tik ile işaretlenir
- Başarısız indirmeler kırmızı çarpı ile işaretlenir
- Başarısız indirmeler "failed_games.txt" dosyasına kaydedilir

## Film Kapakları İndirme

### Film Listesi Hazırlama
1. Film isimlerini bir metin dosyasına yazın
2. Her satıra bir film ismi gelecek şekilde düzenleyin
3. Dosyayı UTF-8 kodlaması ile kaydedin

### Kapak İndirme
1. "Filmler" sekmesine geçin
2. "Film Listesi Seç" butonuna tıklayın
3. Hazırladığınız dosyayı seçin
4. "Film Kapaklarını İndir" butonuna tıklayın
5. İndirme işlemi başlayacaktır

### İngilizce İsim Dönüştürme
1. "İngilizce İsimlerle Değiştir" butonuna tıklayın
2. Dönüştürme işlemi başlayacaktır
3. Sonuçlar "FilmList_English.txt" dosyasına kaydedilecektir

## PDF Oluşturma

### Resim Seçme
1. "PDF Oluşturucu" sekmesine geçin
2. "Resim Seç" butonuna tıklayın
3. İstediğiniz kapakları seçin
4. Birden fazla resim seçmek için Ctrl tuşunu basılı tutun

### Sayfa Düzeni
1. Sayfa boyutunu seçin
2. Kapaklar arası boşluğu ayarlayın
3. Sayfa kenar boşluklarını ayarlayın

### PDF Oluşturma
1. "PDF Oluştur" butonuna tıklayın
2. PDF dosyası otomatik olarak oluşturulacaktır
3. İşlem tamamlandığında bildirim alacaksınız

## Metin Düzenleme

### Dosya Seçme
1. "Metin Düzenleyici" sekmesine geçin
2. "Metin Dosyası Seç" butonuna tıklayın
3. Düzenlemek istediğiniz dosyayı seçin

### Metin Düzenleme
1. Metni doğrudan düzenleyebilirsiniz
2. "Sırala" butonu ile alfabetik sıralama yapabilirsiniz
3. "Tekrarları Temizle" butonu ile tekrar eden satırları silebilirsiniz

### Kaydetme
1. "Kaydet" butonuna tıklayın
2. Değişiklikler otomatik olarak kaydedilecektir

## Sık Sorulan Sorular

### 1. API Anahtarları Nasıl Alınır?
- Steam API: [Steam Developer](https://steamcommunity.com/dev/apikey)
- Twitch API: [Twitch Developer Console](https://dev.twitch.tv/console)
- OMDb API: [OMDb API](http://www.omdbapi.com/apikey.aspx)
- TMDB API: [TMDB API](https://www.themoviedb.org/settings/api)

### 2. İndirme Hızı Nasıl Artırılır?
- İnternet bağlantınızı kontrol edin
- API limitlerini kontrol edin
- Aynı anda çok fazla istek göndermekten kaçının

### 3. Kapaklar Nereye İndirilir?
- Oyun kapakları: "Oyunlar" klasörü
- Film kapakları: "Filmler" klasörü

## Hata Çözümleri

### 1. API Bağlantı Hataları
- API anahtarlarınızı kontrol edin
- İnternet bağlantınızı kontrol edin
- API limitlerini kontrol edin

### 2. Dosya Okuma/Yazma Hataları
- Dosya izinlerini kontrol edin
- Dosya yolunun doğru olduğundan emin olun
- UTF-8 kodlamasını kullanın

### 3. PDF Oluşturma Hataları
- Seçilen resimlerin geçerli olduğundan emin olun
- Yeterli disk alanı olduğunu kontrol edin
- Resim formatlarını kontrol edin

### 4. Uygulama Çökme Sorunları
- Python sürümünüzü kontrol edin
- Gerekli paketlerin yüklü olduğundan emin olun
- Hata mesajını kontrol edin 