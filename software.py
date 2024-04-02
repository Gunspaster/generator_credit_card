import tkinter as tk
import webbrowser
from faker import Faker

def zaloguj():
    username = entry_username.get()
    password = entry_password.get()

    if username == "Guns" and password == "Guns123":
        label_info.config(text="Successfully logged in!", fg="green")
        root.withdraw()
        otworz_aplikacje()
    else:
        label_info.config(text="Login error. Try again!", fg="red")

def otworz_aplikacje():
    app_window = tk.Toplevel()
    app_window.title("Guns Software")

    button_open_website = tk.Button(app_window, text="Open Website", command=otworz_strone, font=("Arial", 12))
    button_open_website.pack(padx=10, pady=5)

    frame_buttons = tk.Frame(app_window)
    frame_buttons.pack(padx=10, pady=5)

    button_generate_visa_card = tk.Button(frame_buttons, text="Generate Visa Card", command=lambda: generuj_karte_kredytowa('visa'), font=("Arial", 12))
    button_generate_visa_card.grid(row=0, column=0, padx=5)

    button_generate_mastercard = tk.Button(frame_buttons, text="Generate Mastercard", command=lambda: generuj_karte_kredytowa('mastercard'), font=("Arial", 12))
    button_generate_mastercard.grid(row=0, column=1, padx=5)

def otworz_strone():
    webbrowser.open_new("https://doxbin.net/")

def generuj_karte_kredytowa(typ_karty):
    fake = Faker()
    if typ_karty == 'visa':
        numer_karty = fake.credit_card_number(card_type='visa16')
    elif typ_karty == 'mastercard':
        numer_karty = fake.credit_card_number(card_type='mastercard')
    
    data_waznosci = fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y")
    ccv = fake.credit_card_security_code(card_type=typ_karty)
    
    label_credit_card.config(text=f"Generated {typ_karty.capitalize()} Credit Card: {numer_karty}\nExpiration Date: {data_waznosci}\nCCV: {ccv}", font=("Arial", 12), fg="blue")
    
    zapisz_do_pliku(numer_karty, data_waznosci, ccv)

def zapisz_do_pliku(numer_karty, data_waznosci, ccv):
    with open("GunsSoftware_credit_cards.txt", "a") as file:
        file.write(f"Card Number: {numer_karty}, Expiration Date: {data_waznosci}, CCV: {ccv}\n")

root = tk.Tk()
root.title("Guns Software")

label_username = tk.Label(root, text="Username:", font=("Arial", 12))
label_username.grid(row=0, column=0, padx=10, pady=5)

entry_username = tk.Entry(root, font=("Arial", 12))
entry_username.grid(row=0, column=1, padx=10, pady=5)

label_password = tk.Label(root, text="Password:", font=("Arial", 12))
label_password.grid(row=1, column=0, padx=10, pady=5)

entry_password = tk.Entry(root, show="*", font=("Arial", 12))
entry_password.grid(row=1, column=1, padx=10, pady=5)

button_login = tk.Button(root, text="Login", command=zaloguj, font=("Arial", 12))
button_login.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

label_info = tk.Label(root, text="", font=("Arial", 12))
label_info.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

label_credit_card = tk.Label(root, text="", font=("Arial", 12))
label_credit_card.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
