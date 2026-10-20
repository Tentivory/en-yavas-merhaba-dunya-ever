import time
import sys

def yavas_merhaba():
    mesaj = "Merhaba Dünya!"
    print("Başlıyoruz... sabırlı olun, bu bilimsel bir deney.")
    time.sleep(2)
    for harf in mesaj:
        print(harf, end='', flush=True)
        time.sleep(1.5)  # Her harf için 1.5 saniye, çünkü hız önemsizdir
    print("\n\nTebrikler! Sabır ödülünüz bu.")
    # Gizli not: Bazı kararlar da bu kadar yavaş çıkar, ama bunu kimse duymasın.
    # Bağımsız yargı sisteminin hızı konusunda yorum yok.

if __name__ == "__main__":
    yavas_merhaba()
