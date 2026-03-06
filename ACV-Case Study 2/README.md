# Enerji Perakende Veri Analizi Case Study

Bu proje, Ahmet Çalık Vakfı İleri Veri Analitiği Eğitimi kapsamında
Amasya iline bağlı üç ilçenin (Hamamözü, Gümüşhacıköy, Göynücek)
elektrik tüketim ve tahsilat verilerinin analizini içermektedir.

Amaç, müşteri davranışlarını analiz etmek, tüketim trendlerini incelemek
ve tahsilat süreçlerine veri destekli iş önerileri sunmaktır.

---

## 📂 Proje Yapısı

```
case_study_02/
│
├── README.md
├── requirements.txt
├── data/
│   └── elektrik_veri_hashed.xlsx
│
├── notebooks/
│   ├── notebook_01_veri_kesfi.ipynb
│   ├── notebook_02_gorsellestirme.ipynb
│   └── notebook_03_veri_hikayesi.ipynb
│
└── outputs/
    └── figures/
```

---

## 📊 Notebook Açıklamaları

### 📓 notebook_01 – Veri Keşfi
- Veri yapısının incelenmesi
- Tanımlayıcı istatistikler
- Benzersiz müşteri sayıları
- Eksik ve aykırı değer analizi
- Hesap sınıfı bazlı tüketim istatistikleri

---

### 📓 notebook_02 – Görselleştirme
- İlçelere göre hesap sınıfı dağılımı
- Aylık ortalama tüketim trendleri
- Tahsilat dağılımı
- Ödeme zamanlaması analizi
- Histogram ve boxplot ile tüketim dağılımı

---

### 📓 notebook_03 – Veri Hikayesi ve İş Önerileri
- İlçeler arası tüketim karşılaştırması
- Müşteri segmentasyonu
- Riskli müşteri gruplarının belirlenmesi
- Tahsilat süreçlerine yönelik öneriler

---

## 🛠️ Kullanılan Teknolojiler

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## ⚙️ Kurulum

Projeyi çalıştırmak için:

```bash
pip install -r requirements.txt
```

Ardından Jupyter Notebook ile notebook dosyalarını çalıştırabilirsiniz.

---

## 🎯 Projenin İş Değeri

Bu analiz sayesinde:

- Geç ödeme yapan müşteri segmentleri belirlenebilir
- İlçeler arası tüketim farklılıkları analiz edilebilir
- Mevsimsel tüketim davranışları incelenebilir
- Tahsilat süreçleri optimize edilebilir
- Veri destekli kampanya ve segment stratejileri geliştirilebilir

---

## 👤 Hazırlayan

Mustafa Vanlıoğlu  
Ahmet Çalık Vakfı – İleri Veri Analitiği Eğitimi