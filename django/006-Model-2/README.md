## Django Model-2

Kurulum yaptığımız ve githuba push ettiğimiz django dosyasında gitignoredan dolayı pip freeze içindeki install edilen package gitmez.Bunun için aynı packageleri clone işleminden sonra sırasıyla;

```
python -m venv env # 1.adım
source env/Scripts/Activate (windows) # 2.adım
source env/bin/activate (MacOs) # 2.adım
pip install -r requirements.txt # 3.adım

```
 komutu ile tekrar yüklemiş oluruz.

## İNSTALL COMMANDS

```diff
- CREATING VIRTUAL ENVIRONMENT
# windows
py -m venv env
# windows other option
python -m venv env
# linux / Mac OS
python3 -m venv env

+ ACTIVATING ENVIRONMENT
# windows
.\env\Scripts\activate
# linux / Mac OS
source env/bin/activate

+ PACKAGE INSTALLATION
# if pip does not work try pip3 in linux/Mac OS
pip install django

! CREATING PROJECT
django-admin startproject main .
 #*main** >>project name; #**subfolder** >>hangi klasörünün altına yüklensin
 python manage.py runserver # Django sayfası 🚀

! CREATING APPS
 python3 manage.py startapp <appname> #=django-admin startapp  <appname>

 # ADMİN PANEL ACTIVATING
 python manage.py createsuperuser

 # Models update
 python manage.py makemigrations


 # Models update and database executed
 python manage.py migrate

 # SHELL ENVİROMENT
 python manage.py shell
 Çalışacak class shell ortamına çağrılır:
 from fscohort.models import Student

 # SHELL COMMANDS
 save()
 <classname>.objects.create() # created and save
 <classname>.objects.alls() # all log
 <classname>.objects.get() # single query
 <classname>.objects.filter() #multiple query
 <classname>.objects.filter("firstname__startswitch="K") #multiple query
  <classname>.objects.exclude() #


 shell çıkmak için ** exit() ** komutu çalıştırılır.

 # modelle resim eklemek istiyorsak
  1- İnstall python -m pip install Pillow 
  2- main >> settings.py >> MEDİA_URL="upload_to verilen ismi ekle"
  3- main >>urls.py file içerisine 👇
  # View Static/Media Files:
    from django.conf import settings
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) komut eklenir.
```

**NOT!!!**
Migrate yapmadan önce app leri <span style="color: pink"> main>settings.py>installed apps </span> main>settings.py>installed apps yoluna eklemeyi unutmak migrate haber veririz

blank = Form da boş bırakmaya izin ver/Verme
null = DB de null kaydet/kaydetme

 auto_now : her bir güncellemede en son tarihi alıyor
 auto_now_add : create ederken alıyor sadece

 - ORM nedir?

 Veritabanı ile ilgili yapılan işlemlerde yazılımcı doğrudan sql sorguları yazmak durumundadır. ORM ile kod içerisine yazılan sql satırları ortadan kalkmıştır. Veritabanımız içerisinde yer alan tablolar bir sınıf (class), kolondaki alanlarımızın her biri değişken (property) olarak tanımlanmakta, veritabanındaki kayıtlara da ait olduğu sınıfta bir obje olarak erişebilmekte ve kullanabilmekteyiz.
- ORM kullanmanın avantajları:
  - Nesne tabanlı programlama standartlarına uygun olarak kod yazma imkanı verir.
  - Minimum SQL bilgisi ile veritabanı işlemleri yapmak imkanı tanır.
  - Veritabanı platformu bağımlılığı yoktur. Oracle kullanıyorken MSSQL geçişini sorunsuzca gerçekleştirebiliriz.
  - Kod yazma süresini kısaltır.
  - Kod okunabilirliğini arttırır.

ORM (Object Relational Mapping) ile ilgili açıklayıcı bir yazı 
[ORM NEDİR??](https://bsseylcin.medium.com/orm-object-relational-mapping-nedi%CC%87r-be5cbaf543b3)

#https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups

```diff
- text in red
+ text in green
! text in orange
# text in gray
```
