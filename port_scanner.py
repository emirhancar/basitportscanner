import socket

def port_tarama(host, baslangic_port, bitis_port):
    print(f"{host} için port taraması başlıyor...")
    for port in range(baslangic_port, bitis_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sonuc = sock.connect_ex((host, port))
        if sonuc == 0:
            print(f"Port {port} açık")
        sock.close()

if __name__ == "__main__":
    hedef_ip = input("Hedef IP adresini girin: ")
    port_tarama(hedef_ip, 1, 1024)
