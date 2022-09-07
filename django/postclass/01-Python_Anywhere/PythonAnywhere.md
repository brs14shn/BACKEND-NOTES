
## PYTHON ANYWHERE

Python anywherede django dosyasını deploy etmek için aşağıda belirtilen aşamaları yapıyoruz.

1-Python anywhere sayfasından hesap oluşturma işlemlerini yapıyoruz.Bir adet uygulama oluşturmamıza izin veriyor.Ücretsiz sürüm üzerinden devam ediyoruz.

2-Localde yaptığımız projeyi github push işlemini yapıyoruz.

3-Python anywhere > dashboard sayfasından console $bash açıyoruz.

![](https://cdn-images-1.medium.com/max/1600/1%2AR33UyBBExRijmTvjIsnJZA.png)

4- $bash sayfasından sırasıyla,

```py
git clone (github project name)
cd projename
python -m venv env # enviroment ortamı oluşturuyoruz.
source env/bin/activate # MAC/linux env aktif hale getiriyoruz.
pip install -r requirements.txt 
# projemizdeki yüklediğimiz kurulumları install ediyoruz.
echo SECRET_KEY=secretkeyiniz > .env 
# env dosyası oluşturup içerisinde SECRET_KEY tanımlıyoruz.Localdeki ile aynı olmak zorunda değildir.
python manage.py migrate 
#migrate db ile ilişki kuruyoruz
```
![](https://cdn-images-1.medium.com/max/1600/1%2AaHGYfXJmwql46L3-5MHV3g.png)

5- Python anywhere>web sekmesinden **Add a new web app** tıklayarak açılan pencereden *manual>ptyhon (son sürüm) seçilir.

6-$bash üzerinden;

```py
pwd # komut ile dosya yolu bulunur.
```
7- Dosya yolu ;python anywhere >web sayfasının
 - Source code
 - Working directory
 - Virtual env bölümlerine yapıştırılır.
![](https://cdn-images-1.medium.com/max/1600/1%2ApWeVJMgYo34_OBBtBcfVNA.png)
![](https://cdn-images-1.medium.com/max/1600/1%2AeOEa98ro5Z6hGacbLfMGEg.png)
 - WSGİ configurasyon kısmına tıklanarak;
 ```py
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

## assuming your django settings file is at '/home/baris29/mysite/mysite/settings.py'
## and your manage.py is is at '/home/baris29/mysite/manage.py'
path = '/home/baris29/crud-student_register' # pwd dosya yolu
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = '<projectname>.settings'

## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
 ```
![](https://cdn-images-1.medium.com/max/1600/1%2AKAhgx6m0RMfbhVuhCuJZeA.png)
 
 8- Web sayfasından yeşil alana tıklıyoruz ve configuration for sonrasında bulunan linkten projeyi yayımlıyoruz.

 9- Bu aşama "Invalid HTTP_HOST header: 'xxxxx.pythonanywhere.com'. You may need to add 'fatihg.pythonanywhere.com' to ALLOWED_HOSTS" hatası alanlar;  

```py
#! Invalid HTTP_HOST header: 'xxxxx.pythonanywhere.com'. You may need to add 'fatihg.pythonanywhere.com' to ALLOWED_HOSTS.
DEBUG="True"
ALLOWED_HOSTS = ['*']
```

![](https://cdn-images-1.medium.com/max/1600/1%2Ao_GnRfxP7Ci-pcH6eYG7Qw.png)

```py
rm -rf *
 # komutu ile yapılan işlemleri sıfırlayarak yeniden aynı komutları denemeleri gerekmektedir.
```