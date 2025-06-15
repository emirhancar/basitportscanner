<div align="center">
  <img src="https://img.shields.io/github/languages/count/emirhancar/basitportscanner?style=flat-square&color=blueviolet" alt="Language Count">
  <img src="https://img.shields.io/github/languages/top/emirhancar/basitportscanner?style=flat-square&color=1e90ff" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/emirhancar/basitportscanner?style=flat-square&color=ff69b4" alt="Last Commit">
  <img src="https://img.shields.io/github/license/emirhancar/basitportscanner?style=flat-square&color=yellow" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square" alt="Contributions">
</div>

simple port scanner
basit port tarayıcı

This project helps you detect potential vulnerabilities in your network by quickly scanning open ports on the target IP address. Developed in Python and Kali Linux environment, this port scanner works efficiently and quickly using multi-threading. It is both a practical application for those who want to learn and an ideal tool for basic security testing.

Bu proje, hedef IP adresindeki açık portları hızlıca tarayarak ağınızdaki potansiyel güvenlik açıklarını tespit etmenize yardımcı olur. Python ve Kali Linux ortamında geliştirilen bu port tarayıcı, çoklu iş parçacığı kullanarak verimli ve hızlı çalışır. Hem öğrenmek isteyenler için pratik bir uygulama hem de temel güvenlik testleri için ideal bir araçtır.



---

Features / Özellikler
Fast Port Scanning: Quickly scans ports 1-1024 on the specified IP address.
Hızlı Port Tarama: Belirtilen IP adresindeki 1-1024 arası portları hızlıca tarar.

Multithreading Support: Uses ThreadPoolExecutor to perform parallel and faster scanning.
Çoklu İş Parçacığı Desteği: ThreadPoolExecutor kullanarak tarama işlemini paralel ve hızlı yapar.

User-Friendly Interface: Easy to run by entering target IP in the terminal.
Kullanıcı Dostu Arayüz: Terminal üzerinden kolayca hedef IP girilip çalıştırılabilir.

Easily Extensible: Simple and clear code structure allows easy addition of new features.
Kolay Geliştirilebilir: Kod basit ve anlaşılır olduğu için kolayca yeni özellikler eklenebilir.

Cross-Platform: Written in Python, it can run on different operating systems.
Platform Bağımsız: Python ile yazıldığı için farklı işletim sistemlerinde çalışabilir.

---

## Team / *Ekip*

- 2320191048 - Emirhan Acar: project owner and management
  2320191048 - Emirhan Acar: proje sahibi ve yönetimi


---

## Roadmap / *Yol Haritası*

See our plans in [ROADMAP.md](ROADMAP.md).  
*Yolculuğu görmek için [ROADMAP.md](ROADMAP.md) dosyasına göz atın.*

---

Topic / Başlık	Link	Description / Açıklama
Port Scanner Project	researchs/port-scanner.md	A Python-based tool to scan open ports on target IPs quickly. / Hedef IP’deki açık portları hızlıca tarayan Python tabanlı araç.
Multithreaded Network Scan	researchs/multithreaded-scan.md	Explains the use of threading to speed up network scanning. / Ağ taramalarını hızlandırmak için iş parçacığı kullanımının açıklaması.
Network Security Basics	researchs/network-security-basics.md	Overview of fundamental concepts in network security. / Ağ güvenliği temel kavramlarının genel özeti.



---

## Installation / *Kurulum*

1. **Clone the Repository / *Depoyu Klonlayın***:  
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO
   ```

2. **Set Up Virtual Environment / *Sanal Ortam Kurulumu*** (Recommended):  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies / *Bağımlılıkları Yükleyin***:  
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage / *Kullanım*

Run the project:  
*Projeyi çalıştırın:*

```bash
python main.py --input your_file.pcap --output results.txt
```

**Steps**:  
1. Prepare input data (*explain data needed*).  
2. Run the script with arguments (*explain key arguments*).  
3. Check output (*explain where to find results*).  

*Adımlar*:  
1. Giriş verilerini hazırlayın (*ne tür verilere ihtiyaç duyulduğunu açıklayın*).  
2. Betiği argümanlarla çalıştırın (*önemli argümanları açıklayın*).  
3. Çıktıyı kontrol edin (*sonuçları nerede bulacağınızı açıklayın*).

---

## Contributing / *Katkıda Bulunma*

We welcome contributions! To help:  
1. Fork the repository.  
2. Clone your fork (`git clone git@github.com:YOUR_USERNAME/YOUR_REPO.git`).  
3. Create a branch (`git checkout -b feature/your-feature`).  
4. Commit changes with clear messages.  
5. Push to your fork (`git push origin feature/your-feature`).  
6. Open a Pull Request.  

Follow our coding standards (see [CONTRIBUTING.md](CONTRIBUTING.md)).  

*Topluluk katkilerini memnuniyetle karşılıyoruz! Katkıda bulunmak için yukarıdaki adımları izleyin ve kodlama standartlarımıza uyun.*

---

## License / *Lisans*

Licensed under the [MIT License](LICENSE.md).  
*MIT Lisansı altında lisanslanmıştır.*

---

## Acknowledgements / *Teşekkürler* (Optional)

Thanks to:  
- Awesome Library: For enabling X.  
- Inspiration Source.  
- Special thanks to...  

*Teşekkürler: Harika kütüphaneler ve ilham kaynakları için.*

---

## Contact / *İletişim* (Optional)

Project Maintainer: [Your Name/Org Name] - [your.email@example.com]  
Found a bug? Open an issue.  

*Proje Sorumlusu: [Adınız/Kuruluş Adınız] - [e-posta.adresiniz@ornek.com]. Hata bulursanız bir sorun bildirin.*

---

*Replace placeholders (e.g., YOUR_USERNAME/YOUR_REPO) with your project details.*
