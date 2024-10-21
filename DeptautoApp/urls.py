"""DepartmntAutomatn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from DeptautoApp import views

urlpatterns = [
#admin
    path('',views.homepagedefault ),
    path('login_post',views.login_post),
    path('adminhomepg',views.adminhomepg),
    path('admin_addteacher',views.admin_addteacher),
    path('admin_addteacher_post',views.admin_addteacher_post),
    path('admin_batch_add',views.admin_batch_add),
    path('admin_batch_add_post',views.admin_batch_add_post),
    path('admin_batchedit/<id>',views.admin_batchedit),
    path('admin_batchedit_post/<id>',views.admin_batchedit_post),
    path('admin_batchlistview', views.admin_batchlistview),
    path('admin_courseedit/<id>', views.admin_courseedit),
    path('admin_courseedit_post/<id>', views.admin_courseedit_post),
    path('admin_courselistview/<id>', views.admin_courselistview),
    path('admin_courseadd/<id>', views.admin_courseadd),
    path('admin_courseadd_post/<id>', views.admin_courseadd_post),
    path('admin_deptadd', views.admin_deptadd),
    path('admin_deptadd_post', views.admin_deptadd_post),
    path('admin_deptedit/<id>', views.admin_deptedit),
    path('admin_deptedit_post/<id>', views.admin_deptedit_post),
    path('admin_deptlistview', views.admin_deptlistview),
    path('admin_sethod', views.admin_sethod),
    path('admin_sethod_post', views.admin_sethod_post),
    path('admin_subjectadd', views.admin_subjectadd),
    path('admin_subjectadd_post', views.admin_subjectadd_post),
   # path('admin_subjectallocation', views.admin_subjectallocation),
    #path('admin_subjectallocation_post', views.admin_subjectallocation_post),
    path('admin_subjectlistview/<id>', views.admin_subjectlistview),
    path('admin_teacherslistview', views.admin_teacherslistview),
    path('admin_hodlistview', views.admin_hodlistview),
    path('admin_A_studentprofileview_post',views.admin_A_studentprofileview_post),
    path('admin_A_studentprofileview',views.admin_A_studentprofileview),
    path('admin_A_studentfeedback',views.admin_A_studentfeedback),
    path('admin_depdelet/<id>',views.admin_depdelet),
    path('admin_coursedlt/<id>',views.admin_coursedlt),
    path('admin_batchdelet/<id>',views.admin_batchdelet),
    path('admin_subjectedit/<id>', views.admin_subjectedit),
    path('admin_subjectedit_post/<id>', views.admin_subjectedit_post),
    path('admin_subjectdelet/<id>/<cid>', views.admin_subjectdelet),
    path('admin_teacherdlt/<id>', views.admin_teacherdlt),
    path('admin_batchlistview', views.admin_batchlistview),
    path('admin_batchlistview_post', views.admin_batchlistview_post),
    path('add_ajax_course/<eid>',views.add_ajax_course),
    path('ajaxa_course/<eid>',views.ajaxa_course),
    path('ajax_deptmnt_crse/<eid>',views.ajax_deptmnt_crse),
    path('load_ajax/',views.load_ajax),

    #teacher
    path('teacher_allocatedsubjectsandstudentview', views.teacher_allocatedsubjectsandstudentview),
    path('teacher_materials', views.teacher_materials),
    path('teacher_materials_post', views.teacher_materials_post),
    path('teacher_parentmanagement', views.teacher_parentmanagement),
    path('teacher_parentmanagement_post', views.teacher_parentmanagement_post),
    path('teacher_semestermark', views.teacher_semestermark),
    path('teacher_studentadd', views.teacher_studentadd),
    path('teacher_studentadd_post', views.teacher_studentadd_post),
    path('teacher_subject_mark', views.teacher_subject_mark),
    path('teacher_subject_mark_post', views.teacher_subject_mark_post),
    path('teacher_materialsname', views.teacher_materialsname),
    path('teacher_materialsname_post', views.teacher_materialsname_post),
    path('teacher_teacherviewandedit', views.teacher_teacherviewandedit),
    path('teacher_teacherviewandedit_post', views.teacher_teacherviewandedit_post),
    path('teacher_viewfeedback', views.teacher_viewfeedback),
#hod
    path('hod_allocateclasstutor', views.hod_allocateclasstutor),
    path('hod_allocateclasstutor_post', views.hod_allocateclasstutor_post),
    path('hod_courseanddepartmentview', views.hod_courseanddepartmentview),
    path('hod_home', views.hod_home),
    # path('hod_subjectallocationteacher', views.hod_subjectallocationteacher),
    path('hod_subjectlistview', views.hod_subjectlistview),
    path('hod_teacherslistview', views.hod_teacherslistview),
    path('hod_hodstudentprofileview', views.hod_hodstudentprofileview),
    path('hod_hodstudentprofileview_post', views.hod_hodstudentprofileview_post),
    path('hod_hodstudentfeedback', views.hod_hodstudentfeedback),
    path('hod_subject_allocation/<id>', views.hod_subject_allocation),
    path('hod_subject_allocation_post/<id>', views.hod_subject_allocation_post),

    #student
    path('student_Studentaddfeed', views.student_Studentaddfeed),
    path('student_Studentaddfeed_post', views.student_Studentaddfeed_post),
    path('student_Studentfeededitdlt', views.student_Studentfeededitdlt),
    path('Student_Studentmaterials', views.Student_Studentmaterials),
    path('student_studentparentview', views.student_studentparentview),
    path('student_studentprofileview', views.student_studentprofileview),
    path('student_Studentrcd', views.student_Studentrcd),
    path('studhomepg',views.studhomepg),
    path('student_studentfeedback',views.student_studentfeedback),
    path('student_studentfeedbackdlt/<id>', views.student_studentfeedbackdlt),
    path('student_viewmark', views.student_viewmark),
    path('student_viewmark_post', views.student_viewmark_post),
    path('student_viewmaterial', views.student_viewmaterial),
    path('student_viewmaterial_post', views.student_viewmaterial_post),

# teacher

    path('andlogin',views.andlogin),
    path('andprofile',views.andprofile),
    path('andaddmark',views.andaddmark),
    path('andaddmaterial',views.andaddmaterial),
    path('and_add_student',views.and_add_student),
    path('andviewallocatedsubject',views.andviewallocatedsubject),
    path('and_view_student',views.and_view_student),
    path('andviewstudentaddmark',views.andviewstudentaddmark),
    path('andview_profile',views.andview_profile),
    path('andupdate_profile',views.andupdate_profile),
    path('andview_studentprofile',views.andview_studentprofile),
    path('andupdate_studentprofile',views.andupdate_studentprofile),
    path('and_delete_student',views.and_delete_student),
    path('and_view_student_addmark',views.and_view_student_addmark),

    path('and_view_allocated_subjects', views.and_view_allocated_subjects),
    path('list_students', views.list_students),
    path('andaddmark', views.andaddmark),
    path('andaddmaterial', views.andaddmaterial),
    path('andadd_attendance', views.andadd_attendance),


]
