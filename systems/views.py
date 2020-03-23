from django.http import HttpResponse
from systems.models import Info


def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    # 每条表记录都是是一个dict对象，
    # key 是字段名，value 是 字段值
    qs = Info.objects.values()

    # 定义返回字符串
    retStr = ''
    for sys_info in qs:
        for name, value in sys_info.items():
            retStr += f'{name} : {value} | '

        # <br> 表示换行
        retStr += '<br>'

    return HttpResponse(retStr)
