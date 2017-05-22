# -*- coding: utf-8 -*-
from models import Project
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json, time, re
from django.forms.models import model_to_dict
from django.db.models import Count, Sum
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt


def project(request):
    is_login = request.session.get('ex_user', None)
    # 如果session不存在则返回登陆页面
    if not is_login:
        return redirect('login')
    context = {}
    return render(request, 'project.html', context)


def show_project_in_table(request):
    '''
    :param request:
    :return:
    '''
    if request.method == "GET":
        limit = request.GET.get('limit')  # how many items per page
        offset = request.GET.get('offset')  # how many items in total in the DB
        sort_column = request.GET.get('sort')  # which column need to sort
        order = request.GET.get('order')  # ascending or descending
        search_condition = request.GET.get('search_condition')
        restr = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
        #print restr.findall(search_condition)
        if len(restr.findall(search_condition))>0:  # 判断是否有搜索字
            all_records = Project.objects.filter(master_ip=search_condition)
        elif search_condition:
            all_records = Project.objects.filter(project_name=search_condition)
        else:
            all_records = Project.objects.all()  # must be wirte the line code here

        if sort_column:  # 判断是否有排序需求
            sort_column = sort_column.replace('asset_', '')
            if sort_column in ['id', 'project_name', 'master_ip', 'problem_info', 'dba', 'department',
                               'remark']:  # 如果排序的列表在这些内容里面
                if order == 'desc':  # 如果排序是反向
                    sort_column = '-%s' % (sort_column)
                all_records = Project.objects.all().order_by(sort_column)
        all_records_count = all_records.count()
        if not offset:
            offset = 0
        if not limit:
            limit = 5  # 默认是每页20行的内容，与前端默认行数一致
        pageinator = Paginator(all_records, limit)  # 开始做分页
        page = int(int(offset) / int(limit) + 1)
        response_data = {'total': all_records_count, 'rows': []}
        # 必须带有rows和total这2个key，total表示总页数，rows表示每行的内容
        for asset in pageinator.page(page):
            # 下面这些asset_开头的key，都是我们在前端定义好了的，前后端必须一致，前端才能接受到数据并且请求.
            response_data['rows'].append({
                # "asset_id": '<a href="/asset/asset_list/%d" target="_blank">%d</a>' % (asset.id, asset.id),
                "asset_id": asset.id if Project.id else "",
                "asset_project_name": asset.project_name if Project.project_name else "",
                "asset_master_ip": asset.master_ip if Project.master_ip else "",
                "asset_problem_info": asset.problem_info if Project.problem_info else "",
                "asset_dba": asset.dba if Project.dba else "",
                "asset_department": asset.department if Project.department else "",
                "asset_remark": asset.remark if Project.remark else "",
            })
        return HttpResponse(json.dumps(response_data))  # 需要json处理下数据格式


def ajax_opt_project(request):
    if request.method == "POST":
        # print request.POST["opt_type"]
        if request.POST["opt_type"] == "add":
            project = Project()
            project.project_name = request.POST["project_name"]
            project.master_ip = request.POST["master_ip"]
            # article.problem_info = request.POST["problem_info"]
            project.dba = request.POST["dba"]
            project.department = request.POST["department"]
            project.remark = request.POST["remark"]
            # print request.POST["published"]
            try:
                project.save()
                op_code = 1
            except Exception as e:
                op_code = 2
                print "Article Add Failed..."

        elif request.POST["opt_type"] == "edit":

            project_id = request.POST["id"]
            project = Project.objects.get(id=project_id)
            project.project_name = request.POST["project_name"]
            project.master_ip = request.POST["master_ip"]
            project.dba = request.POST["dba"]
            project.department = request.POST["department"]
            project.remark = request.POST["remark"]
            try:
                project.save()
                op_code = 1
            except Exception as e:
                op_code = 2
                print "Article Edit Failed......", e

        result = {
            "code": op_code,
            "message": "success"
        }
        return HttpResponse(json.dumps(result))  # 最后返会给前端的数据，如果能在前端弹出框中显示我们就成功了


def ajax_del_project(request):
    if request.method == "POST":
        project_id = request.POST["id"]
        project = Project.objects.get(id=project_id)
        try:
            project.delete()
            op_code = 1
        except Exception as e:
            op_code = -1
            print "ajax_del_article failed...", e
        result = {
            "code": op_code,
            "message": "success"
        }
        return HttpResponse(json.dumps(result))
