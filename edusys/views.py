from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from edusys.models import Student,Course,Report,Teacher
from django.views.decorators.cache import cache_page


#登录页面
@cache_page(60*2)          #页面缓存2分钟
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        if username != "" and password != "":
            stuResult = Student.objects.filter(Sno=username,Spassword=password)
            teaResult = Teacher.objects.filter(Tno=username,Tpassword=password)
            if(len(stuResult)>0):                           #判断是否为学生账号
                request.session['username'] = username
                student=Student.objects.get(Sno=username)
                name=student.Sname
                request.session['name'] = name
                return HttpResponseRedirect("/mysystem/index_stu")
            elif(len(teaResult)>0):                         #判断是否为教师账号
                request.session['username'] = username
                teacher=Teacher.objects.get(Tno=username)
                name=teacher.Tname
                request.session['name'] = name
                return HttpResponseRedirect("/mysystem/index_tea")
            else:
                return render_to_response('login.html',{'message':"用户名或密码错误"})
        else:
            return render_to_response('login.html',{'message':"用户名和密码不能为空"})
    else:
        return render(request,'login.html')

#学生首页
def index_stu(request):
    username = request.session['username']
    stu_name = request.session['name']
    return render_to_response('index_stu.html',locals())

#教师首页
def index_tea(request):
    username = request.session['username']
    tea_name = request.session['name']
    return render_to_response('index_tea.html',locals())

#必修课选课界面
def required_courses(request):
    #获取用户名和姓名
    username = request.session['username']
    stu_name = request.session['name']
    courses = Course.objects.filter(Cnature="必修课");         #从数据库获取必修课程
    if request.method == 'POST':
        select_courses = request.POST.getlist('course')       #得到学生的选课列表
        if len(select_courses)>0:
            for select_course in select_courses:
                course = Course.objects.get(Cno=select_course)
                student = Student.objects.get(Sno=username)
                teacher = course.teacher
                reportResult = Report.objects.filter(student=student,teacher=teacher,course=course)
                if(len(reportResult)>0):            #判断你的课表中是否存在该课程
                    isExist = True
                    isSuccess = False
                    exist_course = course.Cname
                    break
                elif course.Exist_Stu == course.Limit_Stu:
                    isFull = True
                    full_course = course.Cname
                    break
                else:                      #将选课记录写入数据库
                    isSuccess = True
                    course.Exist_Stu = course.Exist_Stu + 1
                    report = Report(student=student,teacher=teacher,course=course)
                    report.save()
                    course.save()
            return render_to_response("required_courses.html",locals())
        else:
            return render_to_response("required_courses.html",locals())
    else:
        return render_to_response("required_courses.html",locals())

#限选课选课界面
def diselectives_courses(request):
    username = request.session['username']
    stu_name = request.session['name']
    courses = Course.objects.filter(Cnature="限选课");
    if request.method == 'POST':
        select_courses = request.POST.getlist('course')
        if len(select_courses)>0:
            for select_course in select_courses:
                course = Course.objects.get(Cno=select_course)
                student = Student.objects.get(Sno=username)
                teacher = course.teacher
                reportResult = Report.objects.filter(student=student,teacher=teacher,course=course)
                if(len(reportResult)>0):
                    isExist = True
                    isSuccess = False
                    exist_course = course.Cname
                    break
                elif course.Exist_Stu == course.Limit_Stu:
                    isFull = True
                    full_course = course.Cname
                    break
                else:
                    isSuccess = True
                    course.Exist_Stu = course.Exist_Stu + 1
                    report = Report(student=student,teacher=teacher,course=course)
                    report.save()
                    course.save()
            return render_to_response("diselectives_courses.html",locals())
        else:
            return render_to_response("diselectives_courses.html",locals())
    else:
        return render_to_response("diselectives_courses.html",locals())

#公选课选课界面
def free_optional_courses(request):
    username = request.session['username']
    stu_name = request.session['name']
    courses = Course.objects.filter(Cnature="公选课");
    if request.method == 'POST':
        select_courses = request.POST.getlist('course')
        if len(select_courses)>0:
            for select_course in select_courses:
                course = Course.objects.get(Cno=select_course)
                student = Student.objects.get(Sno=username)
                teacher = course.teacher
                reportResult = Report.objects.filter(student=student,teacher=teacher,course=course)
                if(len(reportResult)>0):
                    isExist = True
                    isSuccess = False
                    exist_course = course.Cname
                    break
                elif course.Exist_Stu == course.Limit_Stu:
                    isFull = True
                    full_course = course.Cname
                    break
                else:
                    isSuccess = True
                    course.Exist_Stu = course.Exist_Stu + 1
                    report = Report(student=student,teacher=teacher,course=course)
                    report.save()
                    course.save()
            return render_to_response("free_optional_courses.html",locals())
        else:
            return render_to_response("free_optional_courses.html",locals())
    else:
        return render_to_response("free_optional_courses.html",locals())

#体育课选课界面
def physical_education(request):
    #获取用户名和姓名
    username = request.session['username']
    stu_name = request.session['name']
    courses = Course.objects.filter(Cnature="体育课");         #从数据库获取体育课
    if request.method == 'POST':
        select_course = request.POST.get('course')       #得到学生的选课列表
        if select_course != None:
            course = Course.objects.get(Cno=select_course)
            student = Student.objects.get(Sno=username)
            teacher = course.teacher
            reportResult = Report.objects.filter(student=student,course__Cnature="体育课")
            if(len(reportResult)>0):            #判断你的课表中是否存在该课程
                isExist = True
                isSuccess = False
                exist_course = "体育课"
            elif course.Exist_Stu == course.Limit_Stu:
                isFull = True
                full_course = course.Cname
            else:                      #将选课记录写入数据库
                isSuccess = True
                course.Exist_Stu = course.Exist_Stu + 1
                report = Report(student=student,teacher=teacher,course=course)
                report.save()
                course.save()
            return render_to_response("physical_education.html",locals())
        else:
            return render_to_response("physical_education.html",locals())
    else:
        return render_to_response("physical_education.html",locals())

#学生修改密码
def resetpsw_stu(request):
    username = request.session['username']
    stu_name = request.session['name']
    if request.method == 'POST':
        username=request.POST['username']
        old_psw=request.POST['old_psw']
        new_psw=request.POST['new_psw']
        new_psw2=request.POST['new_psw2']
        if username != "" and old_psw != "":
            stuResult = Student.objects.filter(Sno=username,Spassword=old_psw)
            if(len(stuResult)>0):
                if new_psw != new_psw2 and new_psw != "" and new_psw2 != "":
                    message = "请输入相同的新密码"
                    return render_to_response('resetpsw_stu.html',locals())
                else:
                    isSuccess = True
                    change_user = Student.objects.get(Sno=username,Spassword=old_psw)
                    change_user.Spassword = new_psw
                    change_user.save()
                    return render_to_response('resetpsw_stu.html',locals())
            else:
                message = "学号或密码错误"
                return render_to_response('resetpsw_stu.html',locals())
        else:
            message = "请输入学号和密码"
            return render_to_response('resetpsw_stu.html',locals())
    else:
        return render_to_response('resetpsw_stu.html',locals())

#教师修改密码
def resetpsw_tea(request):
    username = request.session['username']
    tea_name = request.session['name']
    if request.method == 'POST':
        username=request.POST['username']
        old_psw=request.POST['old_psw']
        new_psw=request.POST['new_psw']
        new_psw2=request.POST['new_psw2']
        if username != "" and old_psw != "":
            stuResult = Teacher.objects.filter(Tno=username,Tpassword=old_psw)
            if(len(stuResult)>0):
                if new_psw != new_psw2 and new_psw != "" and new_psw2 != "":
                    message = "请输入相同的新密码"
                    return render_to_response('resetpsw_tea.html',locals())
                else:
                    isSuccess = True
                    change_user = Teacher.objects.get(Tno=username,Tpassword=old_psw)
                    change_user.Tpassword = new_psw
                    change_user.save()
                    return render_to_response('resetpsw_tea.html',locals())
            else:
                message = "账号或密码错误"
                return render_to_response('resetpsw_tea.html',locals())
        else:
            message = "请输入账号和密码"
            return render_to_response('resetpsw_tea.html',locals())
    else:
        return render_to_response('resetpsw_tea.html',locals())

#学生查询课表（带有删课功能）
def search_courses(request):
    username = request.session['username']
    stu_name = request.session['name']
    reports = Report.objects.filter(student_id=username)
    if request.method == 'POST':
        delete_courses = request.POST.getlist('delete_courses')
        if len(delete_courses)>0:               #判断是否删课
            for delete_course in delete_courses:
                report = Report.objects.get(student_id=username,course_id=delete_course)
                course = Course.objects.get(Cno=delete_course)
                course.Exist_Stu = course.Exist_Stu - 1
                course.save()
                report.delete()
            return render_to_response('search_courses.html',locals())
    else:
        return render_to_response('search_courses.html',locals())

#学生成绩查询
def search_grades(request):
    username = request.session['username']
    stu_name = request.session['name']
    reports = Report.objects.filter(student_id=username)
    return render_to_response('search_grades.html',locals())

#教师授课表查询
def search_teaching(request):
    username = request.session['username']
    tea_name = request.session['name']
    courses = Course.objects.filter(teacher_id=username)
    return render_to_response('search_teaching.html',locals())

#教师成绩录入
def input_grades(request):
    username = request.session['username']
    tea_name = request.session['name']
    tea_courses = Course.objects.filter(teacher_id=username)
    select_course = request.GET.get('course')
    if request.method == 'GET':
        if select_course == "all":
            reports = Report.objects.filter(teacher_id=username)
            selected = True
        else:
            reports = Report.objects.filter(teacher_id=username,course_id=select_course)
            selected = False
    elif request.method == 'POST':
        if select_course == "all":
            reports = Report.objects.filter(teacher_id=username)
            selected = True
        else:
            reports = Report.objects.filter(teacher_id=username,course_id=select_course)
            selected = False
        for change_report in reports:
            report_id = change_report.id
            if request.POST[str(report_id)] == "" or request.POST[str(report_id)] == "None":
                continue
            score = int(request.POST[str(report_id)])
            change_report = Report.objects.get(id=report_id)
            change_report.Score = score
            change_report.save()
            isSuccess = True
        if select_course == "all":
            reports = Report.objects.filter(teacher_id=username)
            selected = True
        else:
            reports = Report.objects.filter(teacher_id=username,course_id=select_course)
            selected = False
    return render_to_response('input_grades.html',locals())

#学生名单查询
def search_students(request):
    username = request.session['username']
    tea_name = request.session['name']
    tea_courses = Course.objects.filter(teacher_id=username)
    select_course = request.POST.get('course')
    if request.method == 'POST':
        if select_course == "all":
            stu_lists = Report.objects.filter(teacher_id=username)
            selected = True
        else:
            stu_lists = Report.objects.filter(teacher_id=username,course_id=select_course)
            selected = False
    else:
        stu_lists = Report.objects.filter(teacher_id=username)
    return render_to_response('search_students.html',locals())

#注销
def loginout(request):
    #将session删除并返回登录界面
    del request.session['username']
    del request.session['name']
    return HttpResponseRedirect("/")


def page_not_found(request):
    return render_to_response('404.html')

def page_error(request):
    return render_to_response('500.html')