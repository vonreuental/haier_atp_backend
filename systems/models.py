from django.db import models


class Info(models.Model):
    # 系统编号
    system_id = models.CharField(max_length=5, primary_key=True)

    # 系统名称
    system_name = models.CharField(max_length=128)

    # 系统简称
    system_abbr = models.CharField(max_length=64, null=True)

    # 系统分类
    system_type = models.CharField(max_length=32, null=True)

    # 所属小微
    ascription = models.CharField(max_length=32, null=True)

    # 上线时间
    online_time = models.CharField(max_length=10, null=True)

    # 访问地址
    url_address = models.CharField(max_length=128, null=True)

    # 账号信息
    account = models.CharField(max_length=64, null=True)

    # 管理端地址
    admin_address = models.CharField(max_length=128, null=True)

    # 管理端账号信息
    admin_account = models.CharField(max_length=64, null=True)


class EmployeeInfo(models.Model):
    # 员工ID
    employee_id = models.CharField(max_length=5, primary_key=True)

    # 员工姓名
    employee_name = models.CharField(max_length=10)

    # 所属小微ID
    department_id = models.CharField(max_length=3)

    # 所属小微名称
    department_name = models.CharField(max_length=32)


class DepartmentInfo(models.Model):
    # 所属小微ID
    department_id = models.CharField(max_length=3, primary_key=True)

    # 所属小微名称
    department_name = models.CharField(max_length=32)

    # 小微主ID
    director_id = models.CharField(max_length=5)

    # 小微主姓名
    director_name = models.CharField(max_length=10)
