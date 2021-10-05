# -*- coding: utf-8 -*-
from tkinter import * #* komutuyla tkinter kütüphanesindeki bütün sınıfları import ettik
from tkinter import ttk # combobox kullanımı için ttk sınıfını import ettik
import os,sys,subprocess,random #farklı uygulamalar için çeşitli kütüphaneler
from tkinter import messagebox #uyarı mesajları için tkinter sınıfı
import sqlite3 as sql #veritabanı programı ve erişimi için sqlite3 modülü
try:
    from PIL import ImageTk, Image #ikon eklemek dolayısıyla jpg ya da png formatındaki dosyaları ekleyebilmek için pillow kütüphanesi
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow']) #try,except bloğuyla kütüphane yüklü değilse önce windows cmd de işlem yaparak pillow kütüphanesini yükleme işlemi
    from PIL import ImageTk, Image 

class Mutfak(): #mutfak ismiyle sınıfımızı oluşturduk.
    
    def __init__(self):#sınıflar ilk çağrıldığında beraber çalışan init fonksiyonuna her her fonksiyondan erişilmesi istenebilecek değişken değerleri atadık ve anaekran adlı başlangıç ekranını çalıştırdık.
        self.ikon="Veritabani/ikon1.ico"
        self.anaekran()    
    def OptionCallBack(self,event):
        if self.box_value.get() != "Tür:":
            self.a=self.box_value.get()
            self.b=os.listdir(os.getcwd()+"/Veritabani/Tarifler/"+self.a)
            y=[]
            for f in self.b:
                y.append(f.lower().capitalize()[:-4].replace("_"," "))
            self.cb2["values"]=y
    def OptionCallBack2(self,event):
        if self.box_value2.get() !="Ürün:":
            self.cb2a=self.box_value2.get()    
    def OptionCallBack3(self,event):
        if self.box_value3.get() !="Tür:":
            self.a1=self.box_value3.get()
    def buton(self,pencere,yazi,komut,x,y,rw,rh,renk,renk2,kabartma,border,hoverbg,butonbg):
        buton=Button(pencere,text=yazi,command=komut,fg=renk,bg=renk2,relief=kabartma,bd=border)            
        def on_button(self):
            buton.configure(bg=hoverbg)        
        def leave_button(self):
            buton.configure(bg=butonbg)
        buton.bind('<Leave>',leave_button)
        buton.bind('<Enter>',on_button)
        buton.place(relx=x,rely=y,relheight=rh,relwidth=rw)

    def geometri(self,pencere,arkaplan_rengi):
        self.ekrangen = int(pencere.winfo_screenwidth()/4)
        self.ekranyuks = int(pencere.winfo_screenheight()/4)
        self.xkon=int((pencere.winfo_screenwidth()-self.ekrangen)/2)
        self.ykon=int((pencere.winfo_screenheight()-self.ekranyuks)/2)
        pencere.geometry("%dx%d+%d+%d"%(self.ekrangen,self.ekranyuks,self.xkon,self.ykon))
        pencere.config(background=arkaplan_rengi)
        pencere.resizable(width=FALSE, height=FALSE)    
    def ana_menu_butonu(self):
        self.te.destroy()
        self.anaekran()        
    def ana_menu_butonu2(self):
        self.bnp.destroy()
        self.anaekran()
    def ana_menu_butonu3(self):
        self.mnv.destroy()
        self.anaekran()
    def etiket(self,pencere,yazi,kon1,kon2,renk1,renk2,fontt,fsize,italic):
        etiket=Label(pencere,text=yazi,fg=renk1,bg=renk2,font=(fontt,fsize,italic))
        etiket.place(relx=kon1,rely=kon2)
    def Cerceve(self,pencere,renk,boy,girinti,kabartma,border,konum):
        cerceve=Frame(pencere,height=boy,relief=kabartma,bd=border)
        cerceve.config(background=renk)
        cerceve.pack(fill=X,pady=girinti,side=konum)    
    def baslik(self,pencere,baslik):
        pencere.title(baslik)    
    def resim_ekle(self,pencere,dosya,x,y,boyutx,boyuty):
        img = Image.open(dosya)
        img = img.resize((boyutx, boyuty), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(pencere, image = img,bg="gray96") 
        panel.image = img 
        panel.place(relx=x,rely=y)    
    def anaekran(self):
        self.anasayfa=Tk()        
        self.geometri(self.anasayfa,"gray96")
        self.anasayfa.iconbitmap(self.ikon) 
        self.baslik(self.anasayfa, "Mutfak")        
        self.resim_ekle(
            self.anasayfa,self.ikon,"0.03","0.06",100,100)        
        self.etiket(
            self.anasayfa,"Mutfak programina hosgeldin.",
                    "0.425" , "0.145","gray20","gray96","Arial",11,"normal")
        self.etiket(
            self.anasayfa,"Lutfen asagidakilerden birini sec:",
                    "0.455" , "0.245","gray20","gray96","Arial",8,"normal")        
        self.buton(
            self.anasayfa,"Mutfagimda ne var?", self.mutfagimda_ne_var,
                   "0.635","0.370",
                   "0.30","0.10",
                   "gray5","gray96",GROOVE,0,"lightblue","gray96")        
        self.buton(
            self.anasayfa,"Bugun ne pişirsem", self.bugun_ne_pisirsem,
                   "0.635","0.530",
                   "0.28","0.10",
                   "gray5","gray96",GROOVE,0,"lightblue","gray96")            
        self.buton(
            self.anasayfa,"Tarif ekle",self.tarif_ekle,
                   "0.440","0.370",
                   "0.14","0.10",
                   "gray5","gray96",GROOVE,0,"lightblue","gray96")        
        self.buton(
            self.anasayfa,"Tarif görüntüle",self.tarif_goruntule,
                   "0.36","0.530",
                   "0.22", "0.10",
                   "gray5","gray96",GROOVE,0,"lightblue","gray96")
        self.box_value=StringVar()        
        cb=ttk.Combobox(
            self.anasayfa,
            state="readonly",
            textvariable=self.box_value)
        cb["values"]=os.listdir(
            os.getcwd()+"/Veritabani/Tarifler")
        cb.set("Tür:")
        cb.bind("<<ComboboxSelected>>",
                self.OptionCallBack)
        cb.place(
            relx="0.2",rely="0.685",
            relwidth="0.38",relheight="0.1")
        self.box_value2=StringVar()        
        self.cb2=ttk.Combobox(
            self.anasayfa,
            state="readonly",
            textvariable=self.box_value2)
        self.cb2["values"]=None
        self.cb2.set("Ürün:")
        self.cb2.bind("<<ComboboxSelected>>",
                      self.OptionCallBack2)
        self.cb2.place(
            relx="0.2",rely="0.795",
            relwidth="0.38",relheight="0.1") 
                              
    def tarif_ekle(self):
        self.anasayfa.destroy()
        self.te=Tk()
        self.te.iconbitmap(self.ikon)
        self.te.geometry(
            "%dx%d+%d+%d"%(
                self.ekranyuks,self.ekrangen,
                self.xkon,self.ykon))
        self.te.config(background="gray96")
        self.baslik(
            self.te, "Tarif ekle")
        
        self.etiket(
            self.te,"Lütfen ürün türünü seç:",
            0.030,0.15,"gray20","gray96","Arial",8,"normal")
        self.etiket(
            self.te,"Lütfen ürününün ismini gir:",
            0.030,0.27,"gray20","gray96","Arial",8,"normal")
        self.etiket(
            self.te,"Malzemeler",
            0.015,0.42,"black","gray96","Arial",8,"normal")
        self.etiket(
            self.te,"Tarif",
            0.015,0.62,"black","gray96","Arial",8,"normal")        
        
        c=Canvas(
            self.te, width=55, height=1,bg="gray96",highlightthickness=0)
        c.place(relx=0.022,rely=0.47)
        c.create_line(0,0,150,0,fill="black",width=2)        
        c1=Canvas(
            self.te, width=25, height=1,bg="gray96",highlightthickness=0)
        c1.place(relx=0.022,rely=0.67)
        c1.create_line(0,0,150,0,fill="black",width=2)
        
        self.buton(
            self.te, "Ana menu", self.ana_menu_butonu,
                   "0.035", "0.02",
                   "0.3","0.06",
                   "gray5","gray96",GROOVE,0,"lightblue","gray96")    
        self.buton(
            self.te, "Tarifi kaydet", self.tarif_kaydet,
                   "0.65", "0.35",
                   "0.3","0.06",
                   "gray5","gray96",GROOVE,0,"lightblue","gray96")
        
        self.resim_ekle(
            self.te,self.ikon , "0.70","0.02" ,55, 55)
        
        self.box_value3=StringVar()        
        cb3=ttk.Combobox(
            self.te,
            state="readonly",
            textvariable=self.box_value3)
        cb3["values"]=os.listdir(
            os.getcwd()+"/Veritabani/Tarifler")
        cb3.set("Tür:")
        cb3.bind("<<ComboboxSelected>>",
                self.OptionCallBack3)
        cb3.place(
            relx="0.035",rely="0.2",
            relwidth="0.4",relheight="0.05")
        
        def text_temizle(event):
            self.metin.delete("1.0","end")
        def text2_temizle(event):
            self.metin_m.delete("1.0","end")
        def temizle(event):
            self.metin2.delete(0, "end")                       
        kaydirma = Scrollbar(self.te)
        kaydirma.place(relx=0.92,rely=0.49,relwidth=0.08,relheight=0.13)
        self.metin_m=Text(yscrollcommand=kaydirma.set)        
        self.metin_m.insert(END,"Lütfen malzemelerin arasına virgül koy...")
        self.metin_m.place(relx="0.0",rely="0.49",relwidth="0.92",relheight="0.13")
        self.metin_m.bind("<Button-1>",text2_temizle)
        kaydirma.config(command=self.metin_m.yview)
        
        kaydirma2 = Scrollbar(self.te)
        kaydirma2.place(relx=0.92,rely=0.69,relwidth=0.08,relheight=0.31)
        self.metin=Text(yscrollcommand=kaydirma2.set)
        self.metin.insert(END,"Tarifini buraya yazabilirsin...")        
        self.metin.place(relx="0.0",rely="0.69",relwidth="0.92",relheight="0.31")
        self.metin.bind("<Button-1>",text_temizle)
        kaydirma2.config(command=self.metin.yview)
        
        self.metin2=Entry(self.te,width=14)
        self.metin2.insert(0, "Ürün :")         
        self.metin2.place(relx=0.035,rely=0.325)
        self.metin2.bind("<Button-1>", temizle)
    def tarif_kaydet(self):
        try:
            dosya=self.metin2.get()
            icerik=self.metin.get(1.0,END)
            if len(dosya)>0  :
                if len(icerik)>10:
                    for i in dosya:
                        if i=="ç" or i=="Ç":
                            dosya=dosya.replace(i,"c")
                        elif i=="ş" or i =="Ş":
                            dosya=dosya.replace(i,"s")
                        elif i=="ü" or i=="Ü":
                            dosya=dosya.replace(i,"u")
                        elif i=="ğ" or i=="Ğ":
                            dosya=dosya.replace(i,"g")
                        elif i=="ö" or i =="Ö":
                            dosya=dosya.replace(i,"o")
                        elif i=="ı" or i=="İ":
                            dosya=dosya.replace(i,"i")
                        else:
                            pass
                    dosya=dosya.upper()
                    dosya=dosya.replace(" ","_")
                    dosya1=os.getcwd()+"/Veritabani/Tarifler/"+self.a1+"/"+dosya+".txt"
                    
                    malzemeler_x=self.metin_m.get(1.0,END)
                    print(malzemeler_x)
                    malzemeler_x=malzemeler_x.split(",")
                    malzemeler=[]
                    for x in malzemeler_x:
                        for i in x:
                            if i=="ç" or i=="Ç":
                                x=x.replace(i,"c")                                
                            elif i=="ş" or i =="Ş":
                                x=x.replace(i,"s")                                
                            elif i=="ü" or i=="Ü":
                                x=x.replace(i,"u")                                
                            elif i=="ğ" or i=="Ğ":
                                x=x.replace(i,"g")                                
                            elif i=="ö" or i =="Ö":
                                x=x.replace(i,"o")                                
                            elif i=="ı" or i=="İ":
                                x=x.replace(i,"i")                                
                            else:
                                pass
                        malzemeler.append(x)
                    malzemeler=[x.upper() for x in malzemeler]
                    
                    malzemeler.insert(0,dosya)
                    malzemeler[-1]=malzemeler[-1].replace("\n","")
                    vt=sql.connect("Malzemeler.db")
                    im=vt.cursor()
                    x=21-len(malzemeler)
                    for i in range(x):
                        malzemeler.append(None)
                    im.execute("""INSERT INTO {} VALUES(?, ?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""".format(self.a1.replace(" ","_").capitalize()),
                               malzemeler)
                    vt.commit()
                                    
                
                    icerik=self.metin.get(1.0,END)
                    f = open(dosya1,"x")
                    f.write(icerik)
                    self.metin.delete("1.0","end")
                    self.metin2.delete(0, "end")
                    self.metin_m.delete("1.0","end")
                    messagebox.showinfo("Mutfak","Ürünün başarıyla kaydedildi!")
                    f.close()
                    vt.close()
                else:
                    messagebox.showerror("Hata","Alanları boş bırakmamalısın...")
            else:
                messagebox.showerror("Hata","Alanları boş bırakmamalısın...")
        except FileExistsError:
            messagebox.showerror("Hata","Malesef yazdığın ürün daha önce kaydedilmiş,tariflere bakmayı deneyebilirsin.")
        except AttributeError:
            pass   
    def tarif_goruntule(self):
        try:            
            tarif_g=Toplevel()
            tarif_g.config(background="gray96")
            self.baslik(tarif_g, self.cb2a)
            tarif_g.iconbitmap(self.ikon)
            tarif_g.geometry(
                "%dx%d+%d+%d"%(
                    self.ekranyuks,self.ekrangen,
                    self.xkon,self.ykon))
            tarif_g.resizable(
                width=FALSE, height=FALSE)
            self.resim_ekle(tarif_g,self.ikon,"0.75","0.026",45,45)
            
            L=Label(tarif_g,text=self.cb2a,
                fg="black",bg="gray96",font=("Arial",10,"normal"),relief=GROOVE,bd=3)            
            L.place(relx=0.05,rely=0.04)
            
            L1=Label(tarif_g,text="Malzemeler",
                fg="black",bg="gray96",font=("Arial",8,"italic"))            
            L1.place(relx=0.05,rely=0.135)
            
            L2=Label(tarif_g,text="Tarif",
                fg="black",bg="gray96",font=("Arial",8,"italic"))            
            L2.place(relx=0.05,rely=0.44)
                        

            
            kaydirma2 = Scrollbar(tarif_g)
            kaydirma2.place(relx=0.92,rely=0.5,relwidth=0.08,relheight=0.5)            
            metin=Text(tarif_g,yscrollcommand=kaydirma2.set)
            metin_konum=(os.getcwd()+"\\Veritabani\\Tarifler\\"+self.a+"\\"+self.cb2a.upper().replace(" ", "_")+".txt")
            f=open(metin_konum,"r")
            f=f.read()
            metin.insert(INSERT,f.capitalize())
            metin.configure(state="disabled")
            metin.place(relx="0",rely="0.5",relwidth="0.92",relheight="0.5")
            kaydirma2.config(command=metin.yview)
            
            vt=sql.connect("Malzemeler.db")
            im=vt.cursor()
            urun=self.cb2a.upper().replace(" ", "_")
            
            veriler=im.execute("SELECT * FROM {} WHERE URUN = '{}'".format(self.a.replace(" ","_"),urun))
            veriler=list(veriler.fetchall()[0])[1:-1]
            liste=[]
            for i in veriler:
                if str(i)!="None":
                    liste.append(i.lower())
                    
            malzemeler=",".join(liste)
            kaydirma = Scrollbar(tarif_g)
            kaydirma.place(relx=0.92,rely=0.2,relwidth=0.08,relheight=0.2)            
            metin2=Text(tarif_g,yscrollcommand=kaydirma.set)
            metin2.insert(INSERT,malzemeler)
            metin2.configure(state="disabled")
            metin2.place(relx="0",rely="0.2",relwidth="0.92",relheight="0.2")
            kaydirma.config(command=metin2.yview)
            vt.close()
            
        except AttributeError:
            tarif_g.destroy()           
    def mutfagimda_ne_var(self):
        vt=sql.connect("Malzemeler.db")
        im=vt.cursor()
        self.anasayfa.destroy()
        self.mnv=Tk()
        self.mnv.geometry("%dx%d+%d+%d"%(350,200,self.xkon,self.ykon))
        self.mnv.config(background="gray96")
        self.mnv.resizable(width=FALSE, height=FALSE)
        self.baslik(self.mnv, "Mutfağımda ne var?")
        self.mnv.iconbitmap(self.ikon)
        self.resim_ekle(self.mnv,self.ikon , "0.893","0.815" ,25, 25)
        L=Label(self.mnv,text="Aşağıya mutfağındaki ürünleri yazıp, türü seçtikten sonra tamama tıklayarak soldaki menüde pişirebileceğin yemekleri görebilirsin.",
                fg="black",bg="gray96",font=("Arial",10,"italic"),wraplength=200,justify=LEFT)
        L.place(relx=0.05,rely=0.055)                    
        self.box_value4=StringVar()
        self.box_value5=StringVar()
        cb=ttk.Combobox(
            self.mnv,
            state="readonly",
            textvariable=self.box_value4)
        cb.set("Ürünler")
        cb.place(
            relx="0.05",rely="0.785",
            relwidth="0.38",relheight="0.1")    
        
        cb2=ttk.Combobox(
            self.mnv,
            state="readonly",
            textvariable=self.box_value5)
        cb2.set("Tür")
        cb2.place(
            relx="0.5",rely="0.785",
            relwidth="0.38",relheight="0.1")
        im.execute("SELECT name FROM sqlite_master WHERE type='table';")
        liste=[]
        for i in im.fetchall():
            for x in i:
                liste.append(x.lower().capitalize().replace("_"," "))
        cb2["values"]=liste
        def text_temizle(event):
            self.metin_mnv.delete("1.0","end")        
        self.metin_mnv=Text()
        self.metin_mnv.insert(END,"Lütfen malzemelerin arasına virgül koy...")
        self.metin_mnv.place(relx="0.05",rely="0.49",relwidth="0.6",relheight="0.2")
        self.metin_mnv.bind("<Button-1>",text_temizle)
        def tamam():
            if self.box_value5.get() !="Tür":
                deger=self.box_value5.get()
            girdi=self.metin_mnv.get(1.0,END).upper()
            girdi=girdi.split(",")
            
            girdi[-1]=girdi[-1].replace("\n","")
            if deger=="Ana yemek":
                veriler=im.execute("SELECT * FROM ANA_YEMEK;".format(deger))
            elif deger=="Corba":
                veriler=im.execute("SELECT * FROM CORBA;".format(deger))
            elif deger=="Tatli":
                veriler=im.execute("SELECT * FROM TATLI;".format(deger))
            rows = im.fetchall()
            yemekler=[]
            for i in rows:
                res = all(elem in i for elem in girdi)
                if res:
                    malzemeler=([s for s in i if s != None])
                    yemek_ismi=(i[0]).lower().capitalize().replace("_"," ")
                    yemekler.append(yemek_ismi)
            cb["values"]=yemekler
            
            
            
        self.buton(self.mnv, "Ana menu", self.ana_menu_butonu3, 0.7, 0.19, 0.2, 0.1, "black", "gray96", SUNKEN, 0, "lightblue", "gray96")
        self.buton(self.mnv, "Tamam", tamam, 0.7, 0.59, 0.2, 0.1, "black", "gray96", SUNKEN, 0, "lightblue", "gray96")
        
    def bugun_ne_pisirsem(self):
        try:
            x=os.listdir(os.getcwd()+"/Veritabani/Tarifler")
            y=[]
            for i in x:
                    x=os.listdir(os.getcwd()+"/Veritabani/Tarifler/"+i)
                    x=random.choice(x).lower().capitalize()[:-4]
                    y.append(x)
            self.anasayfa.destroy()
            self.bnp=Tk()
            self.bnp.geometry("%dx%d+%d+%d"%(250,200,self.xkon,self.ykon))
            self.bnp.config(background="gray96")
            self.bnp.resizable(width=FALSE, height=FALSE)
            self.resim_ekle(self.bnp,self.ikon , "0.85","0.815" ,25, 25)
            self.bnp.iconbitmap(self.ikon) 
            self.baslik(self.bnp, "Bugun ne pisirsem?")
            y1=y[0]
            y2=y[1]
            y3=y[2]
            c=Canvas(self.bnp, width=40, height=1,bg="gray96",highlightthickness=0)
            c.place(relx=0.105,rely=0.36)
            c.create_line(0,0,150,0,fill="black",width=2)
        
            c1=Canvas(self.bnp, width=75, height=1,bg="gray96",highlightthickness=0)                
            c1.place(relx=0.57,rely=0.36)
            c1.create_line(0,0,150,0,fill="black",width=2)
        
            c2=Canvas(self.bnp, width=30, height=1,bg="gray96",highlightthickness=0)                
            c2.place(relx=0.105,rely=0.61)
            c2.create_line(0,0,150,0,fill="black",width=2)
        
            self.etiket(self.bnp,"İşte bugün pişirebileceğin yemekler:",0.085,0.10,"black","gray96","Aerial",10,"italic")
            self.etiket(self.bnp, "Çorba", 0.10, 0.25, "black", "gray96", "Aerial", 10,"italic")
            self.etiket(self.bnp, "Ana Yemek", 0.57, 0.25, "black", "gray96", "Aerial", 10,"italic")
            self.etiket(self.bnp, "Tatlı", 0.10, 0.50, "black", "gray96", "Aerial", 10,"italic")
        
            self.etiket(self.bnp, y2, 0.10, 0.37, "black", "gray96", "Aerial", 10,"normal")
            self.etiket(self.bnp, y1, 0.57, 0.37, "black", "gray96", "Aerial", 10,"normal")
            self.etiket(self.bnp, y3, 0.10, 0.62, "black", "gray96", "Aerial", 10,"normal")
            self.buton(
                self.bnp, "Ana menu", self.ana_menu_butonu2,
                0.57, 0.815, 0.25, 0.1,
                "black", "gray96", FLAT, 0, "lightblue", "gray96")
        except IndexError:
            messagebox.showerror("Hata","Henüz yeteri kadar tarif yok...")       
Mutfak()

mainloop()