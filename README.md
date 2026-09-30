# 🚀 End-to-End E-Commerce Shipping Delay Prediction with Random Forest & FastAPI

Bu proje, e-ticaret lojistik operasyonlarında kargoların zamanında ulaşıp ulaşmayacağını tahmin etmek amacıyla geliştirilmiş uçtan uca bir makine öğrenmesi ve web API entegrasyonu (MLOps) çalışmasıdır. Lojistik süreçlerindeki depo bilgileri, kargo detayları, taşıma modları ve müşteri geçmişi analiz edilerek operasyonel gecikme riski önceden tahmin edilmektedir. 

Modelin eğitimi aşamasında sızıntısız (data leakage-free) bir makine öğrenmesi boru hattı (Pipeline) kurgulanmış, kategorik ve sayısal veriler için gerekli ölçeklendirme ve kodlama işlemleri tek çatı altında toplanmıştır. Lojistik verisinin doğasındaki gürültü (noise) göz önüne alınarak, genel doğruluk (accuracy) yerine **Hassasiyet (Precision)** metriği maksimize edilmiş; hiperparametre optimizasyonu tamamlanan Balanced Random Forest modeli FastAPI kullanılarak modern bir web arayüzü ile canlıya alınmıştır.

## 🛠️ Kullanılan Teknolojiler
* **Makine Öğrenmesi & Veri Bilimi:** Python, Pandas, NumPy, Scikit-Learn, Random Forest Classifier
* **Arka Plan (Backend) & API:** FastAPI, Uvicorn, Pydantic
* **Ön Yüz (Frontend):** HTML5, Bootstrap 5, JavaScript (Fetch API), Jinja2Templates
* **Model Kayıt (Serialization):** Pickle

## 🧠 Makine Öğrenmesi Boru Hattı (Pipeline) Mimarisi
Eğitim aşamasında veri ön işleme (preprocessing) ve modelleme adımları tek bir `Pipeline` nesnesi içinde birleştirilmiştir. Bu mimari sayesinde dışarıdan gelen yepyeni bir kargo parametresi, canlı ortamda manuel dönüşümlere ihtiyaç duymadan doğrudan sisteme beslenebilmektedir. GridSearchCV kullanılarak Random Forest algoritmasının hiperparametreleri (max_depth, min_samples_split, class_weight vb.) optimize edilmiştir. Model, "Gecikecek" (1) tahmini yaptığında **%97 oranında doğru risk tespiti** yaparak e-ticaret firmaları için (VIP kurye atama, erken müşteri bilgilendirmesi gibi) son derece güvenilir bir otomasyon kararı üretmektedir.

## 💻 Canlıya Alma (Deployment) ve Kullanım
Proje, bir REST API olarak hizmet vermektedir ve kullanıcı dostu bir web arayüzüne sahiptir. Gelen JSON formatındaki HTTP POST istekleri FastAPI arka planında işlenir, eğitilmiş Pickle modeli üzerinden geçirilir ve anında kargo durum raporu (Sorunsuz/Riskli) olarak geri döndürülür.
![Kargo Risk Tahmin Arayüzü](shipping_screenshot.png)

### Kurulum Adımları
Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. Repoyu bilgisayarınıza indirin:
```bash
git clone [https://github.com/mervesgrtlpnr/ECommerce-Shipping-Delay-Predictor.git](https://github.com/mervesgrtlpnr/ECommerce-Shipping-Delay-Predictor.git)
cd ECommerce-Shipping-Delay-Predictor
