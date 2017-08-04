from django.db import models

class Student(models.Model):
    Sno = models.CharField(u'学号',max_length=20,primary_key=True)
    Sname = models.CharField(u'姓名',max_length=20)
    Spassword = models.CharField(u'密码',max_length=15)
    Semail = models.EmailField(u'电子邮箱')
    Ssex = models.CharField(u'性别',max_length=2)
    def __str__(self):
        return self.Sname

class Teacher(models.Model):
    Tno = models.CharField(u'工号',max_length=20,primary_key=True)
    Tname = models.CharField(u'姓名',max_length=20)
    Tsex = models.CharField(u'性别',max_length=2)
    Tpassword = models.CharField(u'密码',max_length=15)
    def __str__(self):
        return self.Tname

class Course(models.Model):
    Cno = models.CharField(u'课程号',max_length=10,primary_key=True)
    Cname = models.CharField(u'课程名',max_length=20)
    Cnature = models.CharField(u'课程性质',max_length=20)
    Classhour = models.IntegerField(u'学时')
    Credit = models.FloatField(u'学分')
    teacher = models.ForeignKey('Teacher')
    TimeTable = models.CharField(u'时间',max_length=15)
    Place = models.CharField(u'地点',max_length=20)
    Limit_Stu = models.IntegerField(u'限报人数')
    Exist_Stu = models.IntegerField(u'已报人数')
    def __str__(self):
        return self.Cname

class Report(models.Model):
    Score = models.IntegerField(u'成绩',null=True)
    teacher = models.ForeignKey('Teacher')
    student = models.ForeignKey('Student')
    course = models.ForeignKey('Course')
    def __str__(self):
        return '%s : %s - %s' % (self.student.Sname, self.course.Cname, self.teacher.Tname)
