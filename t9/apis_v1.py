from django.forms import model_to_dict

from .models import Poetry
from django.http import JsonResponse, QueryDict
from django.views.generic import View

SUCCESS = 1

DATA = {
    'code': SUCCESS,
    'msg': 'ok',
    'data': ""
}

class PoetryAPI(View):

    def get(self, request):
        # 处理get请求
        p_id = request.GET.get("p_id")
        data = Poetry.objects.get(pk=p_id)
        DATA['data'] = model_to_dict(data)
        return JsonResponse(DATA)

    def post(self, req):
        params = req.POST
        p_title = params.get("title")
        p_author = params.get("author")
        p_content = params.get("content")
        # 创建数据
        p = Poetry.objects.create(
            title=p_title,
            author=p_author,
            content=p_content
        )
        DATA['data'] = p.id
        return JsonResponse(DATA)

    def delete(self, req):
        params = QueryDict(req.body)
        p_id = params.get("p_id")
        print(p_id)
        Poetry.objects.get(pk=p_id).delete()
        DATA['data'] = p_id
        DATA['msg'] = "删除了id是{p_id}的数据".format(p_id=p_id)
        return JsonResponse(DATA)