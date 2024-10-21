from django.db import models


class Login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)


class Department(models.Model):
    depname = models.CharField(max_length=100)


class Course(models.Model):
    course = models.CharField(max_length=100)
    DEPARTMENT = models.ForeignKey(Department, on_delete=models.CASCADE)


class Batches(models.Model):
    batch_name = models.CharField(max_length=100)
    DEPARTMENT = models.ForeignKey(Department, on_delete=models.CASCADE)


class Subjects(models.Model):
    subject_name = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    COURSE = models.ForeignKey(Course, on_delete=models.CASCADE)


class Teachers(models.Model):
    name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    house_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    pin = models.IntegerField()
    post = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    profile_pic = models.CharField(max_length=2000)
    password = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE, default=1)
    DEPARTMENT = models.ForeignKey(Department, on_delete=models.CASCADE, default=1)


class Allocateclasstutor(models.Model):
    COURSE = models.ForeignKey(Course, on_delete=models.CASCADE)
    TEACHERS = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    BATCH = models.ForeignKey(Batches, on_delete=models.CASCADE)


class Hod(models.Model):
    TEACHERS = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    DEPARTMENT = models.ForeignKey(Department, on_delete=models.CASCADE)


class Students(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    house_name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    pin = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    aadhar_no = models.CharField(max_length=100)
    identification_mark = models.CharField(max_length=1000)
    joined_clubs = models.CharField(max_length=1000)
    blood_group = models.CharField(max_length=100)
    licence_no = models.CharField(max_length=100)
    profile_pic = models.CharField(max_length=2000)
    about = models.CharField(max_length=1000)
    reg_no = models.CharField(max_length=100)
    COURSE = models.ForeignKey(Course, on_delete=models.CASCADE)
    BATCH = models.ForeignKey(Batches, on_delete=models.CASCADE)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE, default=1)


class Feedbacks(models.Model):
    STUDENTS = models.ForeignKey(Students, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=2000)
    date = models.CharField(max_length=100)


class Subject_assigned_teachers(models.Model):
    SUBJECTS = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    TEACHERS = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    BATCH = models.ForeignKey(Batches, on_delete=models.CASCADE)
    COURSE = models.ForeignKey(Course, on_delete=models.CASCADE)




class Marks(models.Model):
    STUDENTS = models.ForeignKey(Students, on_delete=models.CASCADE)
    SUBJECTS = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    sem = models.CharField(max_length=200)
    internal_marks = models.CharField(max_length=200)


class Attendence(models.Model):
    STUDENTS = models.ForeignKey(Students, on_delete=models.CASCADE)
    sem = models.CharField(max_length=30)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class Materials(models.Model):
    DEPARTMENT = models.ForeignKey(Department, on_delete=models.CASCADE)
    SUBJECTS = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    COURSE = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="")
    date = models.CharField(max_length=100, default="0000-00-00")
    sem_type_materials = models.CharField(max_length=100)
