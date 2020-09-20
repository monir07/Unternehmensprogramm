from django.shortcuts import render
from main_store.models import Indent, MrrIssue, MaterialList

# Create your views here.


def costing(request):  # This is costing Home page view.
    context = {

    }
    return render(request, "costing/costing.html", context)


def indent_box(request):
    count = 0
    count_mrr = 0
    indent_list = Indent.objects.all()
    for indent in indent_list:
        if not indent.viewed:
            count += 1

    mrr_list = MrrIssue.objects.all()
    for mrr in mrr_list:
        if not mrr.viewed:
            count_mrr += 1
    context = {
        'indent_list': indent_list,
        'count_indent': count,
        'count_mrr': count_mrr
    }
    return render(request, "costing/mail_box_costing.html", context)


def mrr_box(request):
    count_mrr = 0
    count = 0
    mrr_list = MrrIssue.objects.all()
    for mrr in mrr_list:
        if not mrr.viewed:
            count_mrr += 1

    indent_list = Indent.objects.all()
    for indent in indent_list:
        if not indent.viewed:
            count += 1
    context = {
        'mrr_list': mrr_list,
        'count_mrr': count_mrr,
        'count_indent': count,
    }
    return render(request, "costing/mail_box_costing.html", context)


def mrr_show(request, mrr_no):
    target_mrr_no = mrr_no
    target_mrr = MrrIssue.objects.get(mrr_no=target_mrr_no)
    target_mrr.viewed = True
    target_mrr.save()
    target_material_list = MaterialList.objects.filter(mrr_no=target_mrr_no)
    context = {
        'target_mrr': target_mrr,
        'target_material_list': target_material_list,
    }
    return render(request, "main_store/mrr_show.html", context)