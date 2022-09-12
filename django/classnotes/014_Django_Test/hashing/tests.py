from django.test import TestCase
from selenium import webdriver

from .forms import HashForm
import hashlib
from .models import Hash

#browser = webdriver.Chrome()



#browser.get('http://localhost:8000')

# class FunctionalTestCase(TestCase):
    
#     def setUp(self):
#         self.browser = webdriver.Chrome() #! Chrome ayağa kaldırdık
        
    
#     def tearDown(self): 
#         self.browser.quit() #! Ayağa kaldırdığım uygulamaları kapatır(Tümünü kapat)


#     def test_there_is_homepage(self):
#         self.browser.get('http://localhost:8000')
#         self.assertIn('Enter hash here',self.browser.page_source) 
#         #! Enter hash here yazısı, browserda mevcut mu?
#         #! quit komutundan dolayı işlemi test edip kapattı 
#         #! Specifik bir test çalıştırmak istiyorsak ```python manage.py test hashing.test.py.FunctionalTestCase.test_there_is_homepage```
#         #? Method test* ile başlamalı!!!
    
#     def test_hash_of_hello(self):
#          self.browser.get('http://localhost:8000')
#          text = self.browser.find_element_by_id("id_text") 
#          #! İnspect ile textarea nın id sine baktık id=id_text
#          text.send_keys("hello")
#          #! Text area ya hello yazısını gönderdik
#          self.browser.find_element_by_name("submit").click()
#          self.assertInHTML('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', self.browser.page_source)
#          #! İki arguman alır ilki vermesini istediğimiz çıktı,

#          #* ASSERT IN AND ASSERTHTML DİFFERENCE
#          #! assertIn(member, container, msg=None) member in container
#          #! Examples:   self.assertIn(1, [1, 2, 3]) ==> OK

#*=============================UnitTest==============================

class UnitTestCase(TestCase): #* Browserla işimiz kalmadı onun yerine client 

     def test_home_homepage_template(self):
        response = self.client.get('/') 
        self.assertTemplateUsed(response, 'hashing/home.html') 

        #! Daha ayrıntılı çıktı almak istiyorsak python manage.py test -v 2
   
     def test_hash_form(self):
        form = HashForm(data={'text': 'hello'})
        self.assertTrue(form.is_valid())

     def test_hash_func_works(self): 
        text_hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
        self.assertEqual('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', text_hash)
    
     def test_hash_object(self):
       
        hash = Hash()
        hash.text = 'hello'
        hash.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
        hash.save()
        pulled_hash = Hash.objects.get(hash='2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        self.assertEqual(hash.text,pulled_hash.text)
        
     def  test_viewing_hash(self):
        hash = Hash()
        hash.text = 'hello'
        hash.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
        hash.save()
        response = self.client.get('/hash/2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        self.assertContains(response,'hello')


