from django.db import models
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_duratio = models.CharField(max_length=100)
    course_fees = models.IntegerField()
    def __str__(self):
        return self.course_name
class City(models.Model):
    city_name = models.CharField(max_length=150)
    def __str__(self):
        return self.city_name

class Student(models.Model):
    stud_name = models.CharField(max_length=150)
    stud_phno = models.BigIntegerField()
    stud_email = models.CharField(max_length=150)
    paid_fees = models.IntegerField()
    pending_fees = models.IntegerField()
    stud_course = models.ForeignKey(Course, on_delete=models.CASCADE) # id column of Course column will be linked here
    # we have given on_delete=models.CASCADE because if a column is deleted in city table it will check dependency for that id in child table if that
    #perticular id is deleted in parent table it will delete that id related records in child table also
    stud_city  = models.ForeignKey(City, on_delete=models.CASCADE)
