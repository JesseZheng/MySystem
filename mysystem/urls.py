"""mysystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from edusys import views as edusys_views
from django.conf.urls import handler404, handler500

handler404 = edusys_views.page_not_found
handler500 = edusys_views.page_error

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',edusys_views.login,name="login"),
    url(r'^mysystem/index_stu',edusys_views.index_stu,name="index_stu"),
    url(r'^mysystem/index_tea',edusys_views.index_tea,name="index_tea"),
    url(r'^mysystem/required_courses',edusys_views.required_courses,name="required_courses"),
    url(r'^mysystem/diselectives_courses',edusys_views.diselectives_courses,name="diselectives_courses"),
    url(r'^mysystem/free_optional_courses',edusys_views.free_optional_courses,name="free_optional_courses"),
    url(r'^mysystem/physical_education',edusys_views.physical_education,name="physical_education"),
    url(r'^mysystem/search_courses',edusys_views.search_courses,name="search_courses"),
    url(r'^mysystem/search_grades',edusys_views.search_grades,name="search_grades"),
    url(r'^mysystem/resetpsw_stu',edusys_views.resetpsw_stu,name="resetpsw_stu"),
    url(r'^mysystem/resetpsw_tea',edusys_views.resetpsw_tea,name="resetpsw_tea"),
    url(r'^mysystem/input_grades',edusys_views.input_grades,name="input_grades"),
    url(r'^mysystem/search_students',edusys_views.search_students,name="search_students"),
    url(r'^mysystem/search_teaching',edusys_views.search_teaching,name="search_teaching"),
    url(r'^mysystem/loginout',edusys_views.loginout,name="loginout"),
]
