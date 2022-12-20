from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField(default=1)
    about = models.TextField(blank=True, null=True)
    register_date=models.DateTimeField(auto_now_add=True)  #auto_now_add=True: it will be added automatically when the object is created
    last_update_date=models.DateTimeField(auto_now=True) #auto_now=True: it will be added automatically when the object is updated
    is_active = models.BooleanField(default=True)
    
    
    def get_register_date(self):
        return self.register_date.strftime("%d/%m/%Y")
    
    def get_last_update_date(self):
        return self.last_update_date.strftime("%d/%m/%Y")
    
    def student_year_status(self):
        "Returns the student's year status."
        import datetime
        if self.register_date < datetime.date(2019, 1, 1):
            return "Senior"
        elif self.register_date < datetime.date(2020, 1, 1):
            return "Junior"
        else:
            return "Freshman"

    def __str__(self):
        return f"{self.number} - {self.first_name}"
    class Meta:
        ordering = ["number"]
        verbose_name_plural = "student_list"
    
