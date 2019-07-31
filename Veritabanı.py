import sqlite3

con = sqlite3.connect ("kütüphane.db")
                       
cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Soyad TEXT,Kan Grubu TEXT,Rh TEXT,Telefon Numarası INT)")
    con.commit()
def veri_ekle():
    cursor.execute("Insert into kitaplık Values('Rasim Fatih','Zengin','X','+',00000000000)")
    con.commit()
def veri_ekle2(isim,soyad,kan_grubu,rh,telefon_numarası):
   cursor.execute("Insert into kitaplık Values(?,?,?,?,?)",(isim,soyad,kan_grubu,rh,telefon_numarası))
   con.commit()


while True:   
    girisler = int(input("Kullanıcı eklemek için {}'i\nSorgulama yapmak için {}'yi tuşlayınız:".format(1,2)))
    if girisler == int("2"):
        print("Sorgulamak istediğiniz kan grubunu ardından Rh faktörünü giriniz.")
        sorgu_grubu_kan=input("Sorgulamak istediğiniz kan grubunu giriniz:")
        sorgu_grubu_rh=input("Sorgulamak istediğiniz rh faktörünü giriniz:")








        if sorgu_grubu_kan==("A"):
            def verileri_al(kan_grubu):
                cursor.execute ("Select * from kitaplık where kan_grubu = ?,",(kan_grubu,))
                liste=cursor.fetchall()
                print("Kan grubuna göre bilgiler...")
                for i in liste:
                    print(i)
            verileri_al("A") 









            

        if sorgu_grubu_kan==("B"):
            def verileri_al(kan_grubu):
                cursor.execute ("Select * from kitaplık where kan_grubu = ?",(kan_grubu,))
                liste=cursor.fetchall()
                print("Kan grubuna göre bilgiler...")
                for i in liste:
                    print(i)
            verileri_al("B")















            
        if sorgu_grubu_kan==("0"):
            def verileri_al(kan_grubu):
                cursor.execute ("Select * from kitaplık where kan_grubu = ?",(kan_grubu,))
                liste=cursor.fetchall()
                print("Kan grubuna göre bilgiler...")
                for i in liste:
                    print(i)
            verileri_al("0")












        
    if girisler == int("1"):
        print("UYARI:Lütfen telefon numarasını vermeyen kullanıcılar için 0 giriniz.Aksi durumlarda hataya yol açacaktır.")
        print("Yeni üye ekleyiniz.")

        isim = input("İsim:")
        soyad = input("Soyad:")
        kan_grubu = input("Kan Grubu:")
        rh = input("Rh:")
        try:
            telefon_numarası = telefon_numarası = int(input("Telefon Numarası:"))
        except ValueError:
            print("Lütfen telefon numarasını rakamlar ile doğru bir biçimde giriniz...")
   


        if telefon_numarası != str(""):    
            print("Üye başarıyla eklenmiştir.")

        else:
            print("Üye eklemeyi atladınız.")


    veri_ekle2(isim,soyad,kan_grubu,rh,telefon_numarası)

    
    con.close()

   

    


                       
                       
