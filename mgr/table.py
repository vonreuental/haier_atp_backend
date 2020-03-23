import json

from django.http import JsonResponse
from systems.models import Info
from django.core.paginator import Paginator, EmptyPage


def list_table(request):
    try:
        # 检查url中是否有参数
        sort = eval(request.body.decode()).get('sort')
        system_name = eval(request.body.decode()).get('system_name')
        system_type = eval(request.body.decode()).get('system_type')
        ascription = eval(request.body.decode()).get('ascription')
        # 返回一个 QuerySet 对象 ，包含所有的表记录
        qs = Info.objects.values().order_by(sort)
        # 如果有，添加过滤条件
        if system_name:
            qs = qs.filter(system_name__contains=system_name)
        if system_type:
            qs = qs.filter(system_type=system_type)
        if ascription:
            qs = qs.filter(ascription=ascription)

        # 要获取的第几页
        pagenum = eval(request.body.decode()).get('page')

        # 每页要显示多少条记录
        pagesize = eval(request.body.decode()).get('limit')
        # 使用分页对象，设定每页多少条记录
        pgnt = Paginator(qs, pagesize)

        # 从数据库中读取数据，指定读取其中第几页
        page = pgnt.page(pagenum)

        # 将 QuerySet 对象 转化为 list 类型
        retlist = list(page)

        return JsonResponse({
            'code': 20000,
            'data': {
                'total': len(list(qs)),
                'items': retlist
            }
        })
    except EmptyPage:
        return JsonResponse({'code': 0, 'retlist': [], 'total': 0})
    except:
        return JsonResponse({'code': 2, 'msg': f'未知错误\n'})


def modify_table(request):
    # 从请求消息中 获取修改客户的信息
    data = request.body.decode()
    info = json.loads(data)
    system_id = info['system_id']

    try:
        # 根据 id 从数据库中找到相应的记录
        system_info = Info.objects.get(system_id=system_id)
    except system_info.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为{system_id}的系统不存在'
        }
    if 'system_name' in info:
        system_info.system_name = info['system_name']
    if 'system_abbr' in info:
        system_info.system_abbr = info['system_abbr']
    if 'system_type' in info:
        system_info.system_type = info['system_type']
    if 'ascription' in info:
        system_info.ascription = info['ascription']
    if 'online_time' in info:
        system_info.online_time = info['online_time'][0:10]
    if 'url_address' in info:
        system_info.url_address = info['url_address']
    if 'account' in info:
        system_info.account = info['account']
    if 'admin_address' in info:
        system_info.admin_address = info['admin_address']
    if 'admin_account' in info:
        system_info.admin_account = info['admin_account']

    system_info.save()

    return JsonResponse({
        'code': 20000,
        'data': 'success'
    })


def create_table(request):
    # 从请求消息中 获取修改客户的信息
    data = request.body.decode()
    info = json.loads(data)
    # system_id = info['system_id']

    Info.objects.create(system_id=info['system_id'],
                        system_name=info['system_name'],
                        system_abbr=info['system_abbr'],
                        system_type=info['system_type'],
                        ascription=info['ascription'],
                        online_time=info['online_time'][0:10],
                        url_address=info['url_address'],
                        account=info['account'],
                        admin_address=info['admin_address'],
                        admin_account=info['admin_account'])
    return JsonResponse({
        'code': 20000,
        'data': 'success'
    })


def delete_table(request):
    # 从请求消息中 获取修改客户的信息
    data = request.body.decode()
    info = json.loads(data)
    system_id = info['system_id']

    try:
        # 根据 id 从数据库中找到相应的记录
        system_info = Info.objects.get(system_id=system_id)
    except system_info.DoesNotExist:
        return {
            'code': 1,
            'msg': f'id 为{system_id}的系统不存在'
        }

    # delete 方法就将该记录从数据库中删除了
    system_info.delete()
    return JsonResponse({
        'code': 20000,
        'data': 'success'
    })


Action2Handler = {
    'list_table': list_table,
    'modify_table': modify_table,
}


def dispatcher(request):
    # 将请求参数统一放入request 的 params 属性中，方便后续处理

    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)

    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_customer':
        return list_table(request)
    # elif action == 'add_customer':
    #     return addcustomer(request)
    elif action == 'modify_customer':
        return modify_table(request)
    # elif action == 'del_customer':
    #     return deletecustomer(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


if __name__ == '__main__':
    list_table()
