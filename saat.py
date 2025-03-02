from tkinter import *  
import time  

# Ana pencereyi oluştur
clock_window = Tk()
clock_window.title("Dijital Saat")  # Pencere başlığını belirle
clock_window.geometry("400x200")  # Pencerenin boyutlarını ayarla
clock_window.config(bg="#0C1E28")  # Arka plan rengini belirle

# Saat etiketleri (saat, dakika, saniye)
label_hour = Label(clock_window, text="00", font=("Arial", 40), fg="white", bg="#0C1E28")
label_hour.place(x=50, y=70)  # Saat etiketi için konumlandırma

label_minute = Label(clock_window, text="00", font=("Arial", 40), fg="white", bg="#0C1E28")
label_minute.place(x=150, y=70)  # Dakika etiketi için konumlandırma

label_second = Label(clock_window, text="00", font=("Arial", 40), fg="white", bg="#0C1E28")
label_second.place(x=250, y=70)  # Saniye etiketi için konumlandırma

# Saati güncelleyen fonksiyon
def update_clock():
    hour = str(time.strftime("%H"))  # Saat bilgisini al (24 saat formatında)
    minute = str(time.strftime("%M"))  # Dakika bilgisini al
    second = str(time.strftime("%S"))  # Saniye bilgisini al

    label_hour.config(text=hour)  # Saat etiketini güncelle
    label_minute.config(text=minute)  # Dakika etiketini güncelle
    label_second.config(text=second)  # Saniye etiketini güncelle
    
    clock_window.after(1000, update_clock)  # Her saniyede bir fonksiyonu çağır

update_clock()  # İlk çağırma
clock_window.mainloop()  # Arayüzü çalıştır