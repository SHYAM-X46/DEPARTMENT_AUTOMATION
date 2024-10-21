import datetime
import random

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect

from DeptautoApp.models import Login
from DeptautoApp.models import *

def homepagedefault(request):
    return render(request,'index.html')

#ADMIN PAGE

def adminhomepg(request):
    request.session['head'] = ""
    return render(request,'admin/adminindex.html')


def login_get(request):
    return render(request,'admin/login.html')

def login_post(request):
    usn=request.POST['us']
    psw=request.POST['ps']
    alog=Login.objects.filter(username=usn,password=psw)
    if alog.exists():
        logid=alog[0].id
        request.session['loginid']=logid
        print(logid)
        request.session['head']=""
        if alog[0].usertype=='admin':
            return redirect('/adminhomepg')
        # if alog[0].usertype=='teacher':
        #     return redirect('/teacherhome')
        if alog[0].usertype=='student':
            return redirect('/studhomepg')
        if alog[0].usertype=='hod':

            qry=Hod.objects.get(TEACHERS__LOGIN=logid)
            dpid=qry.DEPARTMENT.id
            request.session['departmentid']=dpid
            return redirect('/hod_home')
        else:
            return HttpResponse("<script>alert('invalid user');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('invalid user');window.location='/'</script>")




def admin_addteacher(request):
    request.session['head']="Add Teacher"
    teach=Teachers.objects.all()
    dep=Department.objects.all()
    return render(request,'admin/addteacher.html',{'teee':teach,'deep':dep})

def admin_addteacher_post(request):
    tname=request.POST['Teachername']
    thouse=request.POST['housename']
    tplace=request.POST['place']
    tpost=request.POST['post']
    tpin=request.POST['pin']
    tstate=request.POST['State']
    tdistrict=request.POST['District']
    tpass=request.POST['teacherspassword']
    tgender=request.POST['gender']
    tphn=request.POST['teacherphonenumber']
    tmail=request.POST['teachersemail']
    tpf=request.FILES['tpfp']
    fs=FileSystemStorage()
    dt=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs.save(r"D:\DepartmntAutomatn\DeptautoApp\static\images\\" + dt + '.jpg',tpf)
    path = '/static/images/' +dt + '.jpg'
    deptname=request.POST['deptname']
    obj1=Login()
    obj1.username=tmail
    obj1.password=tpass
    obj1.usertype='teacher'
    obj1.save()

    obj=Teachers()
    obj.name=tname
    obj.phone_no=tphn
    obj.email=tmail
    obj.house_name=thouse
    obj.place=tplace
    obj.pin=tpin
    obj.post=tpost
    obj.district=tdistrict
    obj.state=tstate
    obj.gender=tgender
    obj.profile_pic=path
    obj.password=tpass
    obj.LOGIN=obj1
    obj.DEPARTMENT_id=deptname
    obj.save()
    return HttpResponse("<script>alert('added');window.location='/admin_addteacher#abc'</script>")


def admin_batch_add(request):
    request.session['head'] = "Add Batch"
    dep=Department.objects.all()
    return render(request,'admin/batchadd.html',{'saa':dep })

def admin_batch_add_post(request):
    batchname=request.POST['Batchname']
    depa=request.POST['depsa']
    obj=Batches()
    obj.batch_name=batchname
    obj.DEPARTMENT_id=depa
    obj.save()
    return HttpResponse("<script>alert('updated');window.location='/admin_batch_add#abc'</script>")



def admin_batchlistview(request):
    request.session['head'] = "Batch View"
    stupro = Students.objects.all()
    dep = Department.objects.all()
    batc = Batches.objects.all()
    crs = Course.objects.all()
    return render(request, 'admin/batchlistview.html', {'sugu': stupro, 'saa': dep, 'abc': batc, 'sula': crs})

def admin_batchlistview_post(request):
    depp = Department.objects.all()
    batcp = Batches.objects.all()
    batc=request.POST['batchh']
    crsp = Course.objects.all()
    #dep=request.POST['depsa']2
    crs = request.POST['cour']
    res=Students.objects.filter(BATCH_id=batc, COURSE_id=crs)
    return render(request, 'admin/batchlistview.html', {'saa': depp, 'abc': batcp,'sugu':res, 'sula': crsp})



def admin_courseedit(request,id):
    cor=Course.objects.get(id=id)
    return render(request,'admin/courseedit.html',{'cdf':cor})

def admin_courseedit_post(request,id):
    course_name=request.POST['Coursename']
    Course.objects.filter(id=id).update(course=course_name)
    return HttpResponse("<script>alert('updated');window.location='/admin_courselistview/"+id+"#abc'</script>")

def admin_courselistview(request,id):
    cname=Course.objects.filter(DEPARTMENT_id=id)
    return render(request,'admin/courselistview.html',{'abc':cname})

def admin_courseadd(request,id):
    return render(request,'admin/courseadd.html',{'id':id})

def admin_courseadd_post(request,id):
    course_name=request.POST['Coursename']
    obj=Course()
    obj.course=course_name
    obj.DEPARTMENT_id = id
    obj.save()
    return HttpResponse("<script>alert('added');window.location='/admin_courseadd/"+id+"#abc'</script>")


def admin_deptadd(request):
    request.session['head'] = "Add Department"
    return render(request,'admin/deptadd.html')

def admin_deptadd_post(request):
    deptname=request.POST['Depname']
    obj=Department()
    obj.depname=deptname
    obj.save()
    return HttpResponse("<script>alert('added');window.location='/admin_deptadd#abc'</script>")

def admin_deptedit(request,id):
    dpt=Department.objects.get(id=id)
    return render(request,'admin/deptedit.html',{'abc':dpt})

def admin_deptedit_post(request,id):
    deptname=request.POST['Depname']
    Department.objects.filter(id=id).update(depname=deptname)
    return HttpResponse("<script>alert('updated');window.location='/admin_deptlistview#abc'</script>")

def admin_deptlistview(request):
    request.session['head'] = "Department View "
    dep=Department.objects.all()
    return render(request,'admin/deptlistview.html',{'UNNI':dep})

def admin_sethod(request):
    request.session['head']="Set HOD"
    teach = Teachers.objects.all()
    dep = Department.objects.all()
    return render(request,'admin/sethod.html',{'tee':teach,'deep':dep})

def admin_sethod_post(request):
    deptname=request.POST['deptname']
    hodsname=request.POST['hodsname']
    # obj1=Login()
    # obj1.username=teachername
    # obj1.usertype='hod'
    # obj1.password=ps
    # obj1.save()


    obj=Hod()
    obj.TEACHERS_id=hodsname
    obj.DEPARTMENT_id=deptname
    obj.save()
    Login.objects.filter(id=obj.TEACHERS.LOGIN_id).update(usertype='hod')
    return HttpResponse("<script>alert('HOD added');window.location='/admin_sethod'</script>")

def admin_subjectadd(request):
    request.session['head']="Add Subject"
    crs=Course.objects.all()
    return  render(request,'admin/subjectadd.html',{'annu':crs})

def admin_subjectadd_post(request):
    subjectname=request.POST['subject']
    course=request.POST['coursename']
    sem=request.POST['semester']
    obj=Subjects()
    obj.semester=sem
    obj.subject_name=subjectname
    obj.COURSE_id=course
    obj.save()
    return HttpResponse("<script>alert('added');window.location='/admin_subjectadd#abc'</script>")

def add_ajax_course(request,eid):
    qry=Subjects.objects.filter(COURSE=eid)
    return render(request,'admin/ajaxcourse.html',{"data":qry})

def ajaxa_course(request,eid):
    print("eee",eid)
    qry=Course.objects.filter(DEPARTMENT=eid)
    return render(request,'admin/ajax_course.html',{"data":qry})

def ajax_deptmnt_crse(request,eid):
    obj=Batches.objects.get(id=eid).DEPARTMENT.id
    cr=Course.objects.get(DEPARTMENT=obj).id
    ss=Subjects.objects.filter(COURSE__id=cr)
    arr=[]
    for i in ss:
        if i.DEPARTMENT not  in arr:
            arr.append(i.DEPARTMENT.id)
    return render(request,'admin/ajax_deparment_subject.html',{"data":arr})

#def admin_subjectallocation(request):
    #return render(request,'admin/subjectallocation.html')

#def admin_subjectallocation_post(request):
    #allocated_subjects=request.POST['subjects']
    #deptname=request.POST['deptname']
    #obj=Course_allocated_subjects()
    #obj.COURSE=deptname
    #obj.SUBJECTS=allocated_subjects
    #obj.save()

def admin_subjectlistview(request,id):
    sub=Subjects.objects.filter(COURSE_id=id)
    return render(request,'admin/subjectlistview.html',{'sibu':sub})

def admin_teacherslistview(request):
    request.session['head']="Teachers list view"
    tea=Teachers.objects.all()
    return render(request,'admin/teacherslistview.html',{'somu':tea})

def admin_hodlistview(request):
    request.session['head']="HOD list view"
    tea=Hod.objects.filter(TEACHERS__LOGIN__usertype='hod')
    return render(request,'admin/hodlistview.html',{'somu':tea})

def admin_A_studentprofileview(request):
    stupro=Students.objects.all()
    dep=Department.objects.all()
    batc=Batches.objects.all()
    crs=Course.objects.all()
    return render(request, 'admin/A_studentprofileview.html',{'sugu':stupro,'saa': dep, 'abc': batc, 'sula': crs})

def admin_A_studentprofileview_post(request):
    depp = Department.objects.all()
    batcp = Batches.objects.all()
    crsp = Course.objects.all()
    batc=request.POST['batchh']
    crs=request.POST['crss']
    # dep=request.POST['depsa']
    res=Students.objects.filter(COURSE_id=crs,BATCH_id=batc)
    return render(request, 'admin/A_studentprofileview.html', {'saa': depp, 'abc': batcp, 'sula': crsp,'sugu':res})

def admin_A_studentfeedback(request):
    request.session['head'] = "Student Feedback"
    stufeed=Feedbacks.objects.all()
    return render(request,'admin/A_studentfeedback.html',{'hello':stufeed})

def admin_depdelet(request,id):
    Department.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/admin_deptlistview'</script>")

def admin_coursedlt(request,id):
    Course.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/admin_deptlistview'</script>")

def admin_batchedit(request,id):
    bat=Batches.objects.get(id=id)
    dep=Department.objects.all()
    return render(request, 'admin/batchedit.html', {'saghv': bat,'sgh':dep})

def admin_batchedit_post(request, id):
    batch_name = request.POST['Batchname']
    dep=request.POST['depsa']
    Batches.objects.filter(id=id).update(batch_name=batch_name,DEPARTMENT_id=dep)
    return HttpResponse("<script>alert('updated');window.location='/admin_batchlistview#abc'</script>")

def admin_batchdelet(request,id):
    Batches.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/admin_batchlistview#abc'</script>")



def admin_subjectedit(request,id):
    sub=Subjects.objects.get(id=id)
    cor=Course.objects.all()
    return render(request, 'admin/subjectedit.html', {'saghv': sub,'annu':cor})

def admin_subjectedit_post(request, id):
    subject_name = request.POST['subjectname']
    cor=request.POST['coursename']
    sem=request.POST['semester']
    Subjects.objects.filter(id=id).update(subject_name=subject_name,COURSE_id=cor,semester=sem)
    return HttpResponse("<script>alert('updated');window.location='/admin_deptlistview#abc'</script>")

def admin_subjectdelet(request,id,cid):
    Subjects.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/admin_courselistview/"+cid+"#abc'</script>")

def admin_teacherdlt(request,id):
    Teachers.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/admin_teacherslistview#abc'</script>")


#teacher

def teacherhome(request):
    return render(request,'teacher/teacherhome.html')

def teacher_allocatedsubjectsandstudentview(request):
    return render(request,'teacher/allocatedsubjectsandstudentview.html')

def teacher_materials(request):
    return render(request, 'teacher/../templates/meterials.html')

def teacher_materials_post(request):
    department = request.POST['Dep']
    sem = request.POST['_sem_']
    course = request.POST['_course_']
    obj=Materials()
    obj.DEPARTMENT=department
    obj.COURSE=course
    obj.sem_type_materials=sem
    obj.save()

def teacher_parentmanagement(request):
    return render(request,'teacher/parentmanagement.html')

def teacher_parentmanagement_post(request):
    studentname = request.POST['studentsname']
    guardianname = request.POST['guardianname']
    gphone = request.POST['gphoneno']
    obj=Parent()
    obj.STUDENTS=studentname
    obj.guardianname=guardianname
    obj.gphone=gphone
    obj.save()

def teacher_semestermark(request):
    return render(request,'teacher/semestermark.html')

def teacher_studentadd(request):
    return render(request,'teacher/studentadd.html')

def teacher_studentadd_post(request):
    studentfname=request.POST['studentfname']
    studentsname=request.POST['studentsname']
    studentfathersname=request.POST['studentfathersname']
    studentmothersname=request.POST['studentmothersname']
    housename=request.POST['housename']
    place=request.POST['place']
    posno=request.POST['post']
    pin=request.POST['pin']
    state=request.POST['state']
    district=request.POST['district']
    password=request.POST['password']
    gender=request.POST['gender']
    studentphonenumber=request.POST['studentphonenumber']
    studentsmail=request.POST['studentsmail']
    stpfp=request.POST['stpfp']
    obj=Students()
    obj.first_name=studentfname
    obj.studentsname=studentsname
    obj.studentfathersname=studentfathersname
    obj.studentmothersname=studentmothersname
    obj.housename=housename
    obj.place=place
    obj.post=posno
    obj.pin=pin
    obj.state=state
    obj.district=district
    obj.password=password
    obj.gender=gender
    obj.studentphonenumber=studentphonenumber
    obj.studentsmail=studentsmail
    obj.stpfp=stpfp
    obj.save()

def teacher_subject_mark(request):
    return render(request,'teacher/subject_mark.html')

def teacher_subject_mark_post(request):
    subjects=request.POST['subjects']
    mark=request.POST['mark']
    obj=Marks()
    obj.SUBJECT_ASSIGNED_TEACHERS=subjects
    obj.marks=mark
    obj.save()

def teacher_materialsname(request):
    return render(request,'teacher/materials_add.html')

def teacher_materialsname_post(request):
    Material_name1=request.POST['Subject_name1']
    Material_name2=request.POST['Subject_name2']
    Material_name3=request.POST['Subject_name3']
    Material_name4=request.POST['Subject_name4']
    Material_name5=request.POST['Subject_name5']
    Material_name6=request.POST['Subject_name6']


def teacher_teacherviewandedit(request):
    return render(request,'teacher/teacherviewandedit.html')

def teacher_teacherviewandedit_post(request):
    Teachername=request.POST['Teachername']
    Address=request.POST['Address']
    phonenumber=request.POST['phonenumber']
    email=request.POST['email']
    image=request.POST['image']
    obj=Teachers()
    obj.Teachername=Teachername
    obj.Address=Address
    obj.phonenumber=phonenumber
    obj.email=email
    obj.image=image
    obj.save()

def teacher_viewfeedback(request):
    return render(request,'teacher/viewfeedback.html')

# hod

def hod_subject_allocation(request,id):
    batch=Batches.objects.all()
    subs=Subjects.objects.filter(COURSE_id=id)
    # teach=Teachers.objects.get(DEPARTMENT__id=id)
    teach=Teachers.objects.all()
    return render(request,'hod/subjectallocationtoteacher.html',{'batch':batch,'subs':subs,'teach':teach,"id":id})

def hod_subject_allocation_post(request,id):
    batch=request.POST['batchs']
    sem=request.POST['sem']
    sub=request.POST['sub']
    teacher=request.POST['teacher']
    obj=Subject_assigned_teachers()
    obj.BATCH_id=batch
    obj.SUBJECTS_id=sub
    # obj.SUBJECTS_id.semester=sem
    obj.TEACHERS_id=teacher
    obj.COURSE_id=id
    obj.save()
    return HttpResponse("<script>alert('added');window.location='/hod_home'</script>")

def hod_allocateclasstutor(request):
    crs = Course.objects.all()
    teach = Teachers.objects.all()
    batch = Batches.objects.all()
    return render(request, 'hod/allocateclasstutor.html',{'a':crs,'b':teach,'c':batch})

def hod_allocateclasstutor_post(request):
    crs=request.POST['course']
    teach=request.POST['coursetutor']
    batch=request.POST['batchs']
    obj=Allocateclasstutor()
    obj.TEACHERS_id=teach
    obj.BATCH_id=batch
    obj.COURSE_id=crs
    obj.save()
    return HttpResponse("<script>alert('Class tutor added!');window.location='/hod_allocateclasstutor#abc'</script>")
#
# def hod_allocateclasstutor_post(request):
#     batchname = request.POST['batchs']
#     addtutor = request.POST['coursetutor']
#     course=request.POST['course']
#     obj=Allocateclasstutor()
#     obj.BATCH=batchname
#     obj.COURSE=
#     obj.TEACHERS=addtutor
#     obj.save()


def hod_courseanddepartmentview(request):
    hod=Hod.objects.get(TEACHERS__LOGIN__id=request.session['loginid'])
    # hoddep=Hod.objects.filter(DEPARTMENT=)
    crs=Course.objects.filter(DEPARTMENT=hod.DEPARTMENT)
    return render(request, 'hod/courseanddepartmentview.html',{'damu':crs})

def hod_home(request):
    return render(request, 'hod/hodhome.html')


# def hod_subjectallocationteacher(request):
#     return render(request, 'hod/subjectallocationtoteacher.html')
#
#
# def hod_subjectallocationteacher_post(request):
#     subjectallocatedteacher = request.POST['subjectallocatedteacher']

def hod_teacherslistview(request):
    # print(request.session['loginid'])
    #
    data = Teachers.objects.filter(Q(~Q(LOGIN=request.session['loginid']),DEPARTMENT_id=request.session['departmentid']))

    return render(request, 'hod/teacherslistview.html',{'data':data})

def hod_subjectlistview(request):
    sub=Subjects.objects.all()
    return render(request, 'hod/subjectlistview.html',{'subb':sub})

def hod_hodstudentprofileview(request):
    # hd = Hod.objects.get(TEACHERS__LOGIN=request.session['loginid'])
    res = Students.objects.filter(COURSE__DEPARTMENT__id=request.session['departmentid'])
    # dep=Department.objects.all()
    batc=Batches.objects.all()
    crs=Course.objects.all()
    return render(request, 'hod/hodstudentprofileview.html',{'sugu':res, 'abc': batc, 'sula': crs})

def hod_hodstudentprofileview_post(request):
    depp = Department.objects.all()
    batcp = Batches.objects.all()
    crsp = Course.objects.all()
    batc=request.POST['batchh']
    crs=request.POST['crss']
    dep=request.POST['depsa']
    res=Students.objects.filter(COURSE_id=crs,BATCH_id=batc)
    return render(request, 'hod/hodstudentprofileview.html', {'saa': depp, 'abc': batcp, 'sula': crsp,'sugu':res})

def hod_hodstudentfeedback(request):
    request.session['head'] = "Student Feedback"
    stufeed=Feedbacks.objects.all()
    return render(request,'hod/hodstudentfeedback.html',{'hello':stufeed})





# def hod_teacherslistviewedit_post(requst):

# student
def student_Studentaddfeed(request):
    request.session['head'] = "Add Feedback"
    return render(request, 'student/Studentaddfeed.html')


def student_Studentaddfeed_post(request):
    sid=Students.objects.get(LOGIN=request.session['loginid'])
    studentfeedback = request.POST['studentfeedback']
    d = datetime.datetime.now().strftime("%Y/%m/%d")
    obj = Feedbacks()
    obj.STUDENTS_id=sid.id
    obj.feedback = studentfeedback
    obj.date = d
    obj.save()
    return HttpResponse("<script>alert('Feedback added!');window.location='/studhomepg#abc'</script>")


def student_Studentfeededitdlt(request):
    return render(request, 'student/Studentfeededitdlt.html')


def Student_Studentmaterials(request):
    return render(request, 'student/Studentmaterials.html')


def student_studentparentview(request):
    return render(request, 'student/studentparentview.html')


def student_studentprofileview(request):
    stud=Students.objects.get(LOGIN=request.session['loginid'])
    request.session['head'] = "Student Profile"
    return render(request, 'student/studentprofileview.html',{'stu':stud})


def student_Studentrcd(request):
    return render(request, 'student/Studentrcd.html')

def studhomepg(request):
    return render(request,'student/studenthome.html')

def student_studentfeedback(request):
    request.session['head'] = "Student Feedback"
    stufeed=Feedbacks.objects.filter(STUDENTS__LOGIN=request.session['loginid'])
    return render(request,'student/viewfeedback.html',{'hello':stufeed})

def student_studentfeedbackdlt(request,id):
    Feedbacks.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted');window.location='/studhomepg#abc'</script>")

def student_viewmark(request):
    stud=Marks.objects.filter(STUDENTS__LOGIN=request.session['loginid'])
    request.session['head'] = "Student Mark"
    print(stud)
    return render(request,'student/viewmark.html',{'data':stud})

def student_viewmark_post(request):
    se=request.POST['semester']
    stud = Marks.objects.filter(STUDENTS__LOGIN__id=request.session['loginid'], SUBJECTS__semester=se)
    return render(request, 'student/viewmark.html', {'data': stud})

def student_viewmaterial(request):
    material=Materials.objects.all()
    request.session['head'] = "Study Materials"
    return render(request, 'student/studentmeterials.html', {'data': material})

def student_viewmaterial_post(request):
    se=request.POST['semester']
    material=Materials.objects.filter(SUBJECTS__semester=se)
    return render(request,'student/studentmeterials.html',{'data':material})

#android

def andlogin(request):
    usr=request.POST['u']
    psd=request.POST['p']
    obj=Login.objects.filter(username=usr,password=psd)
    if obj.exists():
        return JsonResponse({"status":"ok","type":obj[0].usertype,"lid":obj[0].id})
    else:
        return JsonResponse({"status": "no"})


def andprofile(request):
    return JsonResponse({"status":"ok"})


def and_add_student(request):
    lid=request.POST['lid']
    stf = Teachers.objects.get(LOGIN=lid)
    btc = Allocateclasstutor.objects.filter(TEACHERS=stf.id).order_by('-id')[0]
    Fnm=request.POST['Fnm']
    Snm=request.POST['Snm']
    phn=request.POST['phn']
    email=request.POST['email']
    gende=request.POST['gender']
    reg=request.POST['reg']
    dad=request.POST['dad']
    mom=request.POST['mom']
    house=request.POST['house']
    plc=request.POST['plc']
    pin=request.POST['pin']
    post=request.POST['post']
    dis=request.POST['dis']
    state=request.POST['state']
    adhar=request.POST['adhar']
    identifi=request.POST['identifi']
    club=request.POST['club']
    blood=request.POST['blood']
    lic=request.POST['lic']
    about=request.POST['about']
    pic=request.FILES['pic']
    fs=FileSystemStorage()
    dt=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs.save(r"D:\DepartmntAutomatn\DeptautoApp\static\images\\" + dt + '.jpg',pic)
    path = '/static/images/' +dt + '.jpg'
    log = Login()
    log.username = email
    log.password = reg
    log.usertype = 'student'
    log.save()

    obj = Students()
    obj.COURSE = Course.objects.get(id=btc.COURSE.id)
    obj.BATCH = Batches.objects.get(id=btc.BATCH.id)
    obj.first_name=Fnm
    obj.second_name=Snm
    obj.phone_no=phn
    obj.gender=gende
    obj.email=email
    obj.father_name=dad
    obj.mother_name=mom
    obj.house_name=house
    obj.place=plc
    obj.pin=pin
    obj.post=post
    obj.district=dis
    obj.state=state
    obj.aadhar_no=adhar
    obj.identification_mark=identifi
    obj.joined_clubs=club
    obj.blood_group=blood
    obj.licence_no=lic
    obj.profile_pic=path
    obj.about=about
    obj.reg_no=reg
    obj.LOGIN=log
    obj.save()



    return JsonResponse({"status":"ok"})

def andviewallocatedsubject(request):
    return JsonResponse({"status":"ok"})

def and_view_student(request):
    lid = request.POST['lid']
    stf = Teachers.objects.get(LOGIN=lid)
    btc = Allocateclasstutor.objects.get(TEACHERS=stf.id)
    res = Students.objects.filter(BATCH=btc.BATCH.id, COURSE=btc.COURSE.id)
    li = []
    for i in res:
        li.append({
            'name': i.first_name+i.second_name,
            'email': i.email,
            'reg_no': i.reg_no,
            'father_name': i.father_name,
            'mother_name': i.mother_name,
            'id': i.id,
            'img':i.profile_pic,
        })
    return JsonResponse({"status":"ok", 'data': li})


def and_viewstudent2(request):
    lid = request.POST['lid']
    stf = Teachers.objects.get(LOGIN=lid)
    btc = Allocateclasstutor.objects.get(TEACHERS=stf.id)
    res = Students.objects.filter(BATCH=btc.BATCH.id, COURSE=btc.COURSE.id)
    li = []
    for i in res:
        li.append({
            'name': i.first_name+i.second_name,
            'email': i.email,
            'reg_no': i.reg_no,
            'father_name': i.father_name,
            'mother_name': i.mother_name,
            'id': i.id,
            'img':i.profile_pic,
        })
    return JsonResponse({"status":"ok", 'data': li})

def andviewstudentaddmark(request):
    return JsonResponse({"status":"ok"})

def andview_profile(request):
    lid = request.POST['lid']
    stf = Teachers.objects.get(LOGIN=lid)
    return JsonResponse({"status":"ok", 'name': stf.name,'Phone_no':stf.phone_no,'Email':stf.email,'House_name':stf.house_name,'Place':stf.place,'Pin':stf.pin,'Post':stf.post,
                         'District':stf.district,'State':stf.state,"image":stf.profile_pic, "gender": stf.gender})


def andupdate_profile(request):
    try:
        lid=request.POST['lid']
        name=request.POST['upd1']
        phn=request.POST['upd2']
        email=request.POST['upd3']
        print(phn,email,lid)
        house=request.POST['upd4']
        place=request.POST['upd5']
        pin=request.POST['upd6']
        post=request.POST['upd7']
        dis=request.POST['upd8']
        state=request.POST['upd9']
        gender=request.POST['gender']
        pic = request.FILES['pic']
        fs = FileSystemStorage()
        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs.save(r"D:\DepartmntAutomatn\DeptautoApp\static\images\\" + dt + '.jpg', pic)
        path = '/static/images/' + dt + '.jpg'
        Teachers.objects.filter(LOGIN=lid).update(name=name,phone_no=phn,email=email,house_name=house,
                                                        place=place,pin=pin,post=post,district=dis,state=state,profile_pic=path,gender=gender)
        return JsonResponse({"status": "ok"})

    except Exception as e:
        lid = request.POST['lid']
        name = request.POST['upd1']
        phn = request.POST['upd2']
        email = request.POST['upd3']
        house = request.POST['upd4']
        place = request.POST['upd5']
        pin = request.POST['upd6']
        post = request.POST['upd7']
        dis = request.POST['upd8']
        state = request.POST['upd9']
        Teachers.objects.filter(LOGIN=lid).update(name=name,phone_no=phn,email=email,
                                                        house_name=house,place=place, pin=pin, post=post, district=dis, state=state)
        return JsonResponse({"status": "ok"})

def andview_studentprofile(request):
    sid = request.POST['sid']
    stf =  Students.objects.get(id=sid)
    return JsonResponse({"status":"ok", 'firstname': stf.first_name,'secondname':stf.second_name,'phnno':stf.phone_no,'registerno':stf.reg_no,'email':stf.email,'fathername':stf.father_name,'mothername':stf.mother_name,
                         'housename':stf.house_name,'place':stf.place,"pin":stf.pin,"post":stf.post,"district":stf.district,"state":stf.state,"aadhaarno":stf.aadhar_no,"identimark":stf.identification_mark,
                         "bloodgrp":stf.blood_group,"licno":stf.licence_no,"abt":stf.about,"gender":stf.gender,'image':stf.profile_pic,"joinedclub":stf.joined_clubs})

def andupdate_studentprofile(request):
    try:
        sid = request.POST['sid']
        fname=request.POST['upd1']
        sname=request.POST['upd2']
        phn=request.POST['upd3']
        regno=request.POST['upd4']
        email=request.POST['upd5']
        father=request.POST['upd6']
        mother=request.POST['upd7']
        house=request.POST['upd8']
        place=request.POST['upd9']
        pin=request.POST['upd10']
        post=request.POST['upd11']
        dist=request.POST['upd12']
        state=request.POST['upd13']
        aadhaar=request.POST['upd14']
        iden=request.POST['upd15']
        club=request.POST['upd16']
        blood=request.POST['upd17']
        licno=request.POST['upd18']
        abt=request.POST['upd19']
        # gender=request.POST['upd20']
        gender = request.POST['gender']
        pic = request.FILES['pic']
        fs = FileSystemStorage()
        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs.save(r"D:\DepartmntAutomatn\DeptautoApp\static\images\\" + dt + '.jpg', pic)
        path = '/static/images/' + dt + '.jpg'
        Students.objects.filter(id=sid).update(first_name=fname,second_name=sname,phone_no=phn,reg_no=regno,
                                            email=email,father_name=father,mother_name=mother,house_name=house,place=place,pin=pin,
                                            post=post,district=dist,state=state,aadhar_no=aadhaar,identification_mark=iden,joined_clubs=club,
                                            blood_group=blood,licence_no=licno,about=abt,gender=gender,profile_pic=path)
        return JsonResponse({"status": "ok"})

    except Exception as e:
        sid = request.POST['sid']
        fname = request.POST['upd1']
        sname = request.POST['upd2']
        phn = request.POST['upd3']
        regno = request.POST['upd4']
        email = request.POST['upd5']
        father = request.POST['upd6']
        mother = request.POST['upd7']
        house = request.POST['upd8']
        place = request.POST['upd9']
        pin = request.POST['upd10']
        post = request.POST['upd11']
        dist = request.POST['upd12']
        state = request.POST['upd13']
        aadhaar = request.POST['upd14']
        iden = request.POST['upd15']
        club = request.POST['upd16']
        blood = request.POST['upd17']
        licno = request.POST['upd18']
        abt = request.POST['upd19']
        gender = request.POST['gender']
        # gender = request.POST['upd20']
        Students.objects.filter(id=sid).update(first_name=fname, second_name=sname, phone_no=phn, reg_no=regno,
                                            email=email, father_name=father, mother_name=mother, house_name=house,
                                            place=place, pin=pin,
                                            post=post, district=dist, state=state, aadhar_no=aadhaar,
                                            identification_mark=iden, joined_clubs=club, blood_group=blood,
                                            licence_no=licno, about=abt, gender=gender)
        return JsonResponse({"status": "ok"})


def and_delete_student(request):
    id = request.POST['id']
    Students.objects.get(id=id).delete()
    return JsonResponse({"status":"ok"})

def and_view_student_addmark(request):
    lid = request.POST['lid']
    # id = Teachers.objects.get(LOGIN=lid)
    res = Students.objects.filter(COURSE__DEPARTMENT_id=id)

    li = []
    for i in res:
        li.append({
            'name': i.first_name,
            'reg_no': i.reg_no,
            'id': i.id,
            'img':i.profile_pic,
        })
    return JsonResponse({"status":"ok", 'data': li})



# def and_view_staff_batch_view(request):
#     lid = request.POST['lid']
#     stf = Subject_assigned_teachers.objects.filter(TEACHERS__LOGIN=lid)
#
#     arr = []
#     for i in stf:
#         if i.BATCH.id not in arr:
#             arr.append(i.BATCH.id)
#     res = []
#     for i in arr:
#         res.append({"id": i,
#                     "batch": Batches.objects.get(id=i).batch_name})
#     return JsonResponse({"status": "ok", "data": res})
#
# def and_view_staff_course_view(request):
#     lid=request.POST['lid']
#     bid=request.POST['bid']
#     stf=Subject_assigned_teachers.objects.filter(TEACHERS__LOGIN=lid,BATCH=bid)
#
#     arr = []
#     for i in stf:
#         if i.COURSE.id not in arr:
#             arr.append(i.COURSE.id)
#     res = []
#     for i in arr:
#         res.append({"id": i,
#                     "course": Course.objects.get(id=i).course})
#     return JsonResponse({"status": "ok", "data": res})
#
#
# def and_view_staff_sem_view(request):
#     lid = request.POST['lid']
#     bid = request.POST['bid']
#     stf = Subject_assigned_teachers.objects.filter(TEACHERS__LOGIN=lid, BATCH=bid)
#
#     arr = []
#     for i in stf:
#         arr.append({"id": i.id,
#                     "course": i.SUBJECTS.semester})
#
#
# def and_view_staff_subject_view(request):
#     lid = request.POST['lid']
#     bid = request.POST['bid']
#     stf = Subject_assigned_teachers.objects.filter(TEACHERS__LOGIN=lid, BATCH=bid)
#
#     arr = []
#     for i in stf:
#         arr.append({"id": i.id,
#                     "course": i.SUBJECTS.semester})


def and_view_allocated_subjects(request):

    lid = request.POST['lid']

    batches = []
    obj = Subject_assigned_teachers.objects.filter(TEACHERS__LOGIN=lid)
    arr = []
    for i in obj:
        if i.BATCH_id not in arr:
            arr.append(i.BATCH_id)
            batches.append({"id": Batches.objects.get(id=i.BATCH_id).id,
                        "batch": Batches.objects.get(id=i.BATCH_id).batch_name})
    course = []
    arr = []
    for i in obj:
        if i.COURSE_id not in arr:
            arr.append(i.COURSE_id)
            course.append({"id": Course.objects.get(id=i.COURSE_id).id,
                        "course": Course.objects.get(id=i.COURSE_id).course})

    sem = []
    arr = []
    for i in obj:
        if i.SUBJECTS.id not in arr:
            arr.append(i.SUBJECTS.id)
            sem.append({"id": Subjects.objects.get(id=i.SUBJECTS.id).semester,
                           "sem": Subjects.objects.get(id=i.SUBJECTS.id).semester})

    subject = []
    arr = []
    for i in obj:
        if i.SUBJECTS_id not in arr:
            arr.append(i.SUBJECTS_id)
            subject.append({"id": Subjects.objects.get(id=i.SUBJECTS_id).id,
                        "subject": Subjects.objects.get(id=i.SUBJECTS_id).subject_name})
    print(sem)

    return JsonResponse({"status": "ok", "batches": batches, "course":course, "sem":sem, "subject":subject})



def list_students(request):
    batch = request.POST['batch']
    course = request.POST['course']
    sem = request.POST['sem']
    sub = request.POST['sub']

    obj = Students.objects.filter(COURSE=course, BATCH=batch)
    print("sem",sem)

    total_days = []
    q = Attendence.objects.filter(sem=sem)

    for i in q:
        if i.sem not in total_days:
            total_days.append(i.sem)

    arr = []
    print(total_days, "ghjk")

    for i in obj:
        sq = Attendence.objects.filter(STUDENTS=i, sem=sem)
        n = 0
        for j in sq:
            if j.status == "full":
                n+=1
            elif j.status == "half":
                n+=0.5
        if len(total_days) == 0:
            percentage = 0
        else:
            percentage = n/len(total_days)*100

        arr.append({"id": i.id,
                    "regno": i.reg_no,
                    "name": i.first_name+" "+i.second_name,
                    "img": i.profile_pic,
                    "att": percentage})
    print(arr)
    return JsonResponse({"status":"ok", "data": arr})

def andaddmark(request):
    sid = request.POST['sid']
    mark = request.POST['mark']
    sem = request.POST['sem']
    sub = request.POST['sub']
    print(sid, mark, sem, sub)
    obj = Marks.objects.filter(SUBJECTS=sub, STUDENTS=sid, sem=sem)
    if obj.exists():
        obj.update(internal_marks=mark)
        return JsonResponse({"status":"updated"})
    obj = Marks()
    obj.SUBJECTS_id = sub
    obj.STUDENTS_id = sid
    obj.internal_marks = mark
    obj.sem = sem
    obj.save()

    return JsonResponse({"status":"ok"})

def andaddmaterial(request):
    sem = request.POST['sem']
    course = request.POST['course']
    sub = request.POST['sub']
    t = request.POST['t']
    file = request.FILES['file']
    fs = FileSystemStorage()
    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs.save(r"D:\DepartmntAutomatn\DeptautoApp\static\materials\\" + dt + '.pdf', file)
    path = '/static/materials/' + dt + '.pdf'
    RES=Course.objects.get(id=course)
    obj=Materials()
    obj.SUBJECTS_id=sub
    obj.COURSE_id=course
    obj.DEPARTMENT_id=RES.DEPARTMENT.id
    obj.title=t
    obj.date=dt
    obj.sem_type_materials=path
    obj.save()
    return JsonResponse({"status":"ok"})

def andadd_attendance(request):
    studid = request.POST['studid']
    status = request.POST['status']
    sem = request.POST['sem']
    obj = Attendence.objects.filter(STUDENTS_id=studid, date=datetime.datetime.now().strftime("%Y-%m-%d"), sem=sem)
    if obj.exists():
        obj.update(status=status)
    else:
        res = Attendence()
        res.STUDENTS_id=studid
        res.date=datetime.datetime.now().strftime("%Y-%m-%d")
        res.status = status
        res.sem = sem
        res.save()
    return JsonResponse({"status":"ok"})



def load_ajax(request):
    cid=request.POST['cid']
    res=Batches.objects.get(id=cid).DEPARTMENT.id
    dd=Subjects.objects.filter(COURSE__DEPARTMENT__id=res)
    l=[]
    for i in dd:
        l.append(({"id":i.id,"sname":i.subject_name}))
    return JsonResponse({"status":"ok","data":l})