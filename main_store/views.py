from itertools import count
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
# Create your views here.
from main_store.models import ProductStore, ProductIssue, ProductCodeName, MaterialList, BinCardInfo, MaterialQuality, \
    MrrIssue, QualityItemList, JobNumber, Indent, IndentMaterials
from main_store.form import ProductIssueForm, ProductStoreForm, MaterialListForm, MrrIssueForm, MaterialQualityForm, \
    QualityItemListForm, IndentForm, IndentMaterialsForm
from datetime import date, datetime
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@login_required(login_url='login')
def home_store(request):
    user_name = "প্রধান ভাণ্ডার"
    context = {
        'user_name': user_name,

    }
    return render(request, "home/main_store.html", context)


@login_required(login_url='login')
def mrr_compose(request):
    submitted = False
    submitted1 = False
    target_item_query = None
    if request.method == 'POST':
        if '_save' in request.POST:
            mrr_no = request.POST.get('mrr_no')
            form = MaterialListForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                submitted = True
                print("Data Save material list!")
                target_item_query = MaterialList.objects.filter(Q(mrr_no=mrr_no))
            else:
                print('form not valid!')
    if request.method == 'POST':
        if '_save1' in request.POST:
            form = MrrIssueForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                submitted1 = True
                print("Data Save in MRR Form.")
            else:
                print('form not valid!')

    context = {
        'target_item_query': target_item_query,
        'submitted': submitted,
        'submitted1': submitted1,
    }
    return render(request, "main_store/mrr_form.html", context)


def mrr_no_receive(request):
    if request.method == 'POST':
        if '_search' in request.POST:
            target_mrr_no = request.POST.get('mrr_no_search')
            print(target_mrr_no)
            return redirect('mrr_show', mrr_no=target_mrr_no)

    context = {

    }
    return render(request, "main_store/mrr_search_form.html", context)


def mrr_show(request, mrr_no):
    target_mrr_no = mrr_no
    target_mrr = MrrIssue.objects.get(mrr_no=target_mrr_no)
    target_material_list = MaterialList.objects.filter(mrr_no=target_mrr_no)
    context = {
        'target_mrr': target_mrr,
        'target_material_list': target_material_list,
    }
    return render(request, "main_store/mrr_show.html", context)


# search using ajax start
def post_ajax(request):
    search = False
    if request.method == "POST":
        search_text = request.POST['search_text']
        search = True
    else:
        search_text = ''
    search_res = ProductStore.objects.filter(code=search_text)
    context = {
        'search_res': search_res,
        'search': search
    }
    return render(request, "main_store/mrr_form.html", context)  # need output as render for csrf token show!


# render_to_reponse did not show csrf token, need jquery min version not slim version. slim verson not working.


def ajax_search(request):
    search = False
    if request.is_ajax():
        search_text = request.POST['search_text']
        search = True
    else:
        search_text = ''
    search_res = ProductCodeName.objects.get(code=search_text)
    print(search_res)

    context = {
        'search_res': search_res,
        'search': search,
    }
    return render(request, 'main_store/ajax_search.html', context)


# search using ajax end here...........


def job_number(request):  # Job Number & name show in dropdown list.
    all_job = JobNumber.objects.all()
    job_nam = ''
    for job in all_job:  # Add job Number after job name in job name row.
        if job.job_type == "Repair":
            job_no = job.job_no
            job_nam = job.job_name + " " + job_no
            job.job_name = job_nam
            job.save()
    print(job_nam)
    context = {
        'all_job': all_job
    }
    return render(request, "main_store/indent_form.html", context)


@login_required(login_url='login')
def product_issue(request):
    form = None
    popup = False
    submitted = False
    p_job = ''
    before_issue = ''
    balance_low = ''
    all_job = JobNumber.objects.all()
    if request.method == 'POST':
        if '_save' in request.POST:
            p_code = request.POST.get('item_code')
            p_job = request.POST.get('job_no')
            p_quantity = request.POST.get('item_quantity')
            form = ProductIssueForm(request.POST, request.FILES)
            target_item_query = BinCardInfo.objects.filter(Q(item_code=p_code))
            print(target_item_query)
            if target_item_query:
                if form.is_valid():
                    instance = form.save(commit=False)
                    for target_item in target_item_query:
                        before_issue = target_item.balance
                        print(target_item.balance)
                        if float(before_issue) > 0 and float(before_issue) >= float(p_quantity):
                            target_item.balance = float(target_item.balance) - float(p_quantity)
                            target_item.save()
                            after_issue = target_item.balance
                            instance.qty_befr_issue = before_issue
                            instance.qty_after_issue = after_issue
                            instance.save()
                            submitted = True
                            print("Issue & deduction OK")
                        else:
                            balance_low = "This Product Not Available or product available but less than your" \
                                          " requirement"

                else:
                    print("Form is not Valid")

            else:
                popup = True
                print("Product not found")
    context = {
        'form': form,
        'submitted': submitted,
        'popup': popup,
        'p_job': p_job,
        'balance_low': balance_low,
        'before_issue': before_issue,
        'all_job': all_job
    }
    return render(request, "main_store/product_issue_form.html", context)


@login_required(login_url='login')
def product_store(request):
    submitted = False
    error_msg = ""
    p_code = ""
    if request.method == 'POST':
        if '_save' in request.POST:
            p_code = request.POST.get('item_code')
            target_item_p_store = ProductStore.objects.filter(Q(item_code=p_code))
            # code.
            if target_item_p_store:
                error_msg = "This Product Code Already Exits. Try new code!"
            else:
                form = ProductStoreForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    submitted = True
                    print("Save is OK")
                    # This code below for product save  to  product name and code table.
                    form2 = ProductCodeName()
                    try:
                        target_item_p_name = ProductCodeName.objects.get(
                            Q(code=p_code))  # Item Target in Product name &
                        if target_item_p_name:
                            target_item_p_name.location = request.POST.get('item_location')
                            target_item_p_name.min_balance = request.POST.get('min_balance')
                            target_item_p_name.item_picture = request.FILES.get('item_picture')
                            target_item_p_name.save()
                    except ObjectDoesNotExist:
                        form2.code = request.POST.get('item_code')
                        form2.name = request.POST.get('item_name')
                        form2.item_unit = request.POST.get('item_unit')
                        form2.location = request.POST.get('item_location')
                        form2.min_balance = request.POST.get('min_balance')
                        form2.item_picture = request.FILES.get('item_picture')
                        form2.item_under_group = request.POST.get('item_group')
                        form2.save()
                        print("Product Name and code save.")
                        # Bin Card table data inserted here...
                    bincard_form = BinCardInfo()
                    bincard_form.ref_no = request.POST.get('ref_no')
                    bincard_form.item_code = request.POST.get('item_code')
                    bincard_form.item_name = request.POST.get('item_name')
                    buy_date = request.POST.get('buy_onDate')
                    if buy_date:
                        bincard_form.date = buy_date
                    bincard_form.job_no = request.POST.get('buy_underJob')
                    bincard_form.entry_qty = request.POST.get('item_quantity')
                    # bincard_form.issued_qty  = request.POST.get('buy_onDate')
                    bincard_form.receiver = request.POST.get('item_user')
                    bincard_form.balance = request.POST.get('item_quantity')
                    bincard_form.min_balance = request.POST.get('min_balance')
                    bincard_form.item_unit = request.POST.get('item_unit')
                    bincard_form.save()
                    print("Bin Card Save!")
                else:
                    print("Form is not Valid")
    context = {
        'submitted': submitted,
        'error_msg': error_msg,
        'p_code': p_code

    }
    return render(request, "main_store/product_store_form.html", context)


@login_required(login_url='login')
def existing_product_store(request):
    submitted = False
    error_msg = ""
    p_code = ""
    p_job_no = ""
    p_min_balance = ''
    if request.method == 'POST':
        if '_save' in request.POST:
            p_code = request.POST.get('item_code')
            p_job_no = request.POST.get('buy_underJob')
            p_code_error = ProductStore.objects.filter(Q(item_code=p_code))  # Q(buy_underJob=p_job_no)
            if not p_code_error:
                error_msg = ": This Product Code is not registered. Try with registered Product Code or " \
                            "Registration by new entry."
            else:
                # these request come from template.
                form = ProductStore()
                form.item_code = p_code
                form.item_name = request.POST.get('item_name')
                form.item_quantity = request.POST.get('item_quantity')
                form.item_unit = request.POST.get('item_unit')
                form.ref_no = request.POST.get('ref_no')
                form.buy_onDate = request.POST.get('buy_onDate')
                form.buy_underJob = p_job_no
                form.item_user = request.POST.get('item_user')
                exp_date = request.POST.get('expire_date')
                if exp_date:
                    form.expire_date = exp_date
                form.recorder = request.POST.get('recorder')

                # request come from name & code table.
                auto_input = ProductCodeName.objects.get(Q(code=p_code))
                form.item_location = auto_input.location
                p_min_balance = auto_input.min_balance
                form.min_balance = p_min_balance
                form.item_picture = auto_input.item_picture
                form.save()
                print("Existing Form Save!")

                update_product = BinCardInfo.objects.filter(Q(item_code=p_code))  #
                if update_product:
                    # Bin Card table data update here...
                    bincard_balance = request.POST.get('item_quantity')
                    bincard_date = request.POST.get('buy_onDate')
                    bincard_ref_no = request.POST.get('ref_no')
                    received_shop = request.POST.get('item_user')
                    target_item_query = BinCardInfo.objects.filter(Q(item_code=p_code))
                    if target_item_query:
                        for target_item in target_item_query:
                            target_item.balance = float(target_item.balance) + float(bincard_balance)
                            target_item.date = bincard_date
                            target_item.ref_no = bincard_ref_no
                            target_item.entry_qty = bincard_balance
                            target_item.save()
                            submitted = True
                        print("Bin Card Updated!")
                else:
                    # Bin Card table data inserted here ...
                    bincard_form = BinCardInfo()
                    bincard_form.ref_no = request.POST.get('ref_no')
                    bincard_form.item_code = p_code
                    bincard_form.item_name = request.POST.get('item_name')
                    bincard_form.date = request.POST.get('buy_onDate')
                    bincard_form.job_no = p_job_no
                    bincard_form.entry_qty = request.POST.get('item_quantity')
                    # bincard_form.issued_qty  = request.POST.get('buy_onDate')
                    bincard_form.receiver = request.POST.get('item_user')
                    bincard_form.balance = request.POST.get('item_quantity')
                    bincard_form.min_balance = p_min_balance
                    bincard_form.item_unit = request.POST.get('item_unit')
                    bincard_form.save()
                    print("Bin Card Save!")
    context = {
        'submitted': submitted,
        'error_msg': error_msg,
        'p_code': p_code,
        'p_job_no': p_job_no

    }
    return render(request, "main_store/Existing_product_store_form.html", context)


def bin_card_state(request):
    search_item_query = None
    total = 0
    if request.method == 'POST':
        if '_search' in request.POST:
            p_code = request.POST.get('search')
            search_item_query = ProductStore.objects.filter(Q(item_code=p_code) | Q(item_name__icontains=p_code) |
                                                            Q(item_quantity=p_code) | Q(item_location=p_code) |
                                                            Q(buy_underJob=p_code))
            for search_item in search_item_query:
                total = total + int(search_item.item_quantity)

    context = {
        'search_item_query': search_item_query,
        'total': total,

    }
    return render(request, "main_store/bin_card_state.html", context)


def issuer_state(request):
    search_query_set = None
    total_issue = 0
    item_unit = ''
    if request.method == 'POST':
        if '_search' in request.POST:
            p_code = request.POST.get('search')
            search_query_set = ProductIssue.objects.filter(Q(sr_no=p_code) | Q(job_no=p_code) |
                                                           Q(received_shop=p_code) | Q(item_code=p_code) |
                                                           Q(item_name__icontains=p_code) | Q(item_quantity=p_code))

            for item_wise in search_query_set:
                total_issue = float(total_issue) + float(item_wise.item_quantity)
                item_unit = item_wise.item_unit  
    context = {
        'search_query_set': search_query_set,
        'total_issue': total_issue,
        'item_unit': item_unit

    }
    return render(request, "main_store/bin_card_issuer.html", context)


def purchase_state(request):
    search_query_set = None
    total_purchase = 0
    item_unit = ''
    if request.method == 'POST':
        if '_search' in request.POST:
            p_code = request.POST.get('search')
            search_query_set = ProductStore.objects.filter(Q(ref_no=p_code) | Q(buy_underJob=p_code)
                                                           | Q(item_code=p_code) | Q(item_name__icontains=p_code) |
                                                           Q(item_user__icontains=p_code))
            for item_wise in search_query_set:
                total_purchase = float(total_purchase) + float(item_wise.item_quantity)
                item_unit = item_wise.item_unit   
    context = {
        'search_query_set': search_query_set,
        'total_purchase': total_purchase,
        'item_unit': item_unit

    }
    return render(request, "main_store/store_state.html", context)


def product_name_code(request):
    search_query_set = ""
    sl_no = 0
    if request.method == 'POST':
        if '_search' in request.POST:
            p_code = request.POST.get('search')
            group_name = request.POST.get('group_name')
            if p_code and not group_name:
                search_query_set = ProductCodeName.objects.filter(Q(name__icontains=p_code) | Q(code__icontains=p_code)
                                                                  | Q(location__icontains=p_code))
                print("Search")
            elif group_name and not p_code:
                search_query_set = ProductCodeName.objects.filter(Q(item_under_group=group_name))
                print("Group Name")
            elif group_name and p_code:
                search_query_set = ProductCodeName.objects.filter((Q(name__icontains=p_code) | Q(code__icontains=p_code)
                                                                  | Q(location__icontains=p_code)) &
                                                                  Q(item_under_group=group_name))
                print("Group Name & search")
    context = {
        'search_query_set': search_query_set,

    }
    return render(request, 'main_store/product_code_name.html', context)


def low_balance_state(request):
    min_balance_list = []
    min_balance_filter = []
    search_query_set = BinCardInfo.objects.all()
    for search_query in search_query_set:
        if search_query.min_balance:
            if float(search_query.min_balance) >= float(search_query.balance):
                min_balance_list.append(search_query)
    if request.method == 'POST':
        if '_search' in request.POST:
            search_key = request.POST.get('search')
            search_query_filter = ProductStore.objects.filter(
                Q(item_code=search_key) | Q(item_name__icontains=search_key) |
                Q(job_no__icontains=search_key))
            for search_filter in search_query_filter:
                if search_filter.min_balance and search_filter.item_quantity:
                    if float(search_filter.min_balance) >= float(search_filter.item_quantity):
                        min_balance_filter.append(search_filter)
    context = {
        'min_balance_filter': min_balance_filter,
        'min_balance_list': min_balance_list,

    }
    return render(request, 'main_store/low_balance.html', context)


def expire_date_state(request):
    current_date = date.today()
    p_code = '112211'
    expired_list = []
    expired_list_filter = []
    diff = ''
    search_query_set = ProductStore.objects.all()
    for search_query in search_query_set:
        last_date = search_query.expire_date
        if last_date:
            diff = last_date - current_date
            if diff.days < 60:
                expired_list.append(search_query)
    if request.method == 'POST':
        if '_search' in request.POST:
            search_key = request.POST.get('search')
            search_query_filter = ProductStore.objects.filter(
                Q(item_code=search_key) | Q(item_name__icontains=search_key) |
                Q(buy_underJob=search_key) | Q(item_user__icontains=search_key))
            for search_filter in search_query_filter:
                last_date = search_filter.expire_date
                diff = (last_date - current_date)
                if diff.days < 60:
                    expired_list_filter.append(search_filter)
    print(expired_list)
    context = {
        'expired_list': expired_list,
        'expired_list_filter': expired_list_filter,

    }
    return render(request, 'main_store/expire_date_list.html', context)


# Auto Complete Function for show Product Code from Product CodeName Table.
def autocomplete(request):
    if 'term' in request.GET:
        qs = ProductCodeName.objects.filter(code__icontains=request.GET.get('term'))
        titles = list()
        for product_name in qs:
            titles.append(product_name.code)
        return JsonResponse(titles, safe=False)
    return render(request, 'main_store/Existing_product_store_form.html')


# Auto Complete Function for show Product Job Number from Product Store Table.
def autocomplete_job_no(request):
    if 'term' in request.GET:
        qs = ProductStore.objects.filter(buy_underJob__icontains=request.GET.get('term'))
        job_no = list()
        for product_job in qs:
            job_no.append(product_job.buy_underJob)
        return JsonResponse(job_no, safe=False)
    return render(request, 'main_store/Existing_product_store_form.html')


def material_balance_state(request):
    search_query_set = None
    total = 0
    unit = ''
    if request.method == 'POST':
        if '_search' in request.POST:
            p_code = request.POST.get('search')
            search_query_set = BinCardInfo.objects.filter(Q(ref_no=p_code) | Q(job_no=p_code)
                                                          | Q(item_code=p_code) | Q(item_name__icontains=p_code))
            for search_item in search_query_set:
                total = total + float(search_item.balance)
                unit = search_item.item_unit
    context = {
        'search_query_set': search_query_set,
        'total': total,
        'unit': unit
    }
    return render(request, 'main_store/mat_balance_state.html', context)


def quality_receive(request):
    if request.method == 'POST':
        if '_search' in request.POST:
            target_quality_no = request.POST.get('quality_no_search')
            print(target_quality_no)
            return redirect('material_quality', quality_no=target_quality_no)

    context = {

    }
    return render(request, "main_store/quality_no_search_form.html", context)


def material_quality(request, quality_no):
    quality_no = quality_no
    quality_data = MaterialQuality.objects.get(Q(quality_no=quality_no))
    quality_item = QualityItemList.objects.filter(Q(quality_no=quality_no))
    if quality_data and quality_item:
        context = {
           "quality_data": quality_data,
           "quality_item": quality_item,
        }
        return render(request, 'main_store/quality_form.html', context)
    else:
        error_msg = 'Search Item Not Found'
    context = {

    }
    return render(request, 'main_store/quality_no_search_form.html', context)


def quality_input(request):
    target_item_query = ''
    submitted = ''
    submitted1 = ''
    form1 = MaterialQualityForm()
    if request.method == 'POST':
        if '_save1' in request.POST:
            quality_no = request.POST.get('quality_no')
            form = QualityItemListForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                submitted1 = True
                print("Data Save Quality Item list!")
                target_item_query = QualityItemList.objects.filter(Q(quality_no=quality_no))
            else:
                print('form not valid!')
    if request.method == 'POST':
        if '_save' in request.POST:
            form = MaterialQualityForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                submitted = True
                print("Quality Report Submitted")
            else:
                print("Form Not Valid")
    context = {
        "form1": form1,
        'target_item_query': target_item_query,
        'submitted': submitted,
        'submitted1': submitted1,
    }
    return render(request, 'main_store/quality_form_input.html', context)


def gate_pass(request):
    bincard_form = BinCardInfo()
    return render(request, 'main_store/gate_pass.html')


def sr_form(request):
    bincard_form = BinCardInfo()
    return render(request, 'main_store/sr_form.html')


def project_detail_store(request):
    user_name = "প্রধান ভাণ্ডার"
    context = {
        'user_name': user_name,

    }
    return render(request, 'main_store/project-details_store.html', context)


def statement(request):
    total_buy = 0
    total_issue = 0
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        product_name = request.POST.get('item_code')  # receive product code from post method.
        p_job_name = request.POST.get('item_job_no')
        if p_job_name and product_name:
            purchase_info = ProductStore.objects.filter(Q(buy_underJob=p_job_name) & Q(item_code=product_name)
                                                        & Q(buy_onDate__range=[start_date, end_date]))
        elif p_job_name and not product_name:
            purchase_info = ProductStore.objects.filter(Q(buy_underJob=p_job_name) &
                                                        Q(buy_onDate__range=[start_date, end_date]))
        else:
            purchase_info = ProductStore.objects.filter(Q(item_code=product_name) &
                                                        Q(buy_onDate__range=[start_date, end_date]))
        if purchase_info:
            for item_buy in purchase_info:
                total_buy = total_buy + float(item_buy.item_quantity)
        print(purchase_info)
        print(total_buy)
        if p_job_name and product_name:
            issue_info = ProductIssue.objects.filter(Q(job_no=p_job_name) & Q(item_code=product_name) &
                                                     Q(date__range=[start_date, end_date]))
        elif p_job_name and not product_name:
            issue_info = ProductIssue.objects.filter(Q(job_no=p_job_name) &
                                                     Q(date__range=[start_date, end_date]))
        else:
            issue_info = ProductIssue.objects.filter(Q(item_code=product_name) & Q(date__range=[start_date, end_date]))
        if issue_info:
            for item_issue in issue_info:
                total_issue = total_issue + float(item_issue.item_quantity)
        print(issue_info)
        print(total_issue)
        context = {
            'purchase_info': purchase_info,
            'issue_info': issue_info,
            'total_issue': total_issue,
            'total_buy': total_buy,
            'start_date': start_date,
            'end_date': end_date,
        }
        return render(request, 'main_store/statement.html', context)
    context = {

    }
    return render(request, 'main_store/statement.html', context)


# Demo Product Code and Name from xlsc/Excel file.
from main_store.models import DemoNameCode, DemoJobNumber
from django.db.models import Count
import xlrd
import os


def demo_code_input(request):
    module_dir = os.path.dirname(__file__)  # set file location. file located in main_store app folder
    file = os.path.join(module_dir, '01 Hardware_microsoft.xlsx')  # set file location in django
    workbook = xlrd.open_workbook(file)
    print(workbook)
    sheet = workbook.sheet_by_index(0)
    for row in range(sheet.nrows):
        print("--------------------------")
        obj_name_code = DemoNameCode()
        for col in range(sheet.ncols):
            if col == 0:
                print("Name: ", sheet.cell_value(row, col))
                obj_name_code.p_name = sheet.cell_value(row, col)
            elif col == 1:
                print("Code: ", sheet.cell_value(row, col))
                obj_name_code.p_code = sheet.cell_value(row, col)
            elif col == 2:
                print("Unit: ", sheet.cell_value(row, col))
                obj_name_code.p_unit = sheet.cell_value(row, col)
            elif col == 3:
                print("Item _under_group: ", sheet.cell_value(row, col))
                obj_name_code.item_under_group = sheet.cell_value(row, col)
        obj_name_code.save()
    return render(request, 'main_store/demo_code_name.html')


def demo_job_name(request):  # Job Number import from demo Excel file.
    module_dir = os.path.dirname(__file__)  # set file location. file located in main_store app folder
    file = os.path.join(module_dir, '09Job Name.xlsx')  # set file location in django
    workbook = xlrd.open_workbook(file)
    print(workbook)
    sheet = workbook.sheet_by_index(0)
    for row in range(sheet.nrows):
        print("--------------------------")
        obj_job_name = DemoJobNumber()
        for col in range(sheet.ncols):
            if col == 0:
                print("Job No: ", sheet.cell_value(row, col))
                obj_job_name.job_no = sheet.cell_value(row, col)
            elif col == 1:
                print("Job Name: ", sheet.cell_value(row, col))
                obj_job_name.job_name = sheet.cell_value(row, col)
            elif col == 2:
                print("Job Type: ", sheet.cell_value(row, col))
                obj_job_name.job_type = sheet.cell_value(row, col)
        obj_job_name.save()
    return render(request, 'main_store/demo_code_name.html')


def demo_job_name_delete(request):  # Delete all Job Number in demo job name database.
    demo_job_no = DemoJobNumber.objects.all()
    demo_job_no.delete()
    context = {
        # 'demo_name': demo_name,
    }
    return render(request, 'main_store/demo_code_show.html', context)


def job_no_store(request):  # Job Number import from demo job name database.
    job_no_dict = DemoJobNumber.objects.all()
    for job_no in job_no_dict:
        form2 = JobNumber()
        print("--------------------------")
        form2.job_no = job_no.job_no
        print("Job No", job_no.job_no)
        form2.job_name = job_no.job_name
        print("Job Name", job_no.job_name)
        form2.job_type = job_no.job_type
        print("Job Type", job_no.job_type)
        form2.save()
    return render(request, 'main_store/demo_code_name.html')


def demo_code_show(request):
    demo_name = DemoNameCode.objects.all()
    context = {
        'demo_name': demo_name,
    }
    return render(request, 'main_store/demo_code_show.html', context)


# def demo_code_delete(request):
#     demo_name = DemoNameCode.objects.filter(Q(p_code=" "))
#     for name in demo_name:
#         print(name.p_name)
#     context = {
#         'demo_name': demo_name,
#     }
#     return render(request, 'main_store/demo_code_show.html', context)

def duplicate_in_demo_code(request):  # find and delete duplicate item name and code from database.
    dupes = DemoNameCode.objects.values('p_name').annotate(Count('id')).order_by().filter(id__count__gt=1)
    records = DemoNameCode.objects.filter(p_name__in=[item['p_name'] for item in dupes])
    print(records)
    records.delete()
    context = {
        'demo_name': demo_name,
    }
    return render(request, 'main_store/demo_code_show.html', context)


def duplicate_in_p_name_code(request): # find and delete duplicate item name and code from database.
    dupes = ProductCodeName.objects.values('name').annotate(Count('id')).order_by().filter(id__count__gt=1)
    records = ProductCodeName.objects.filter(name__in=[item['name'] for item in dupes])
    print(records)
    records.delete()
    context = {
        # 'demo_name': demo_name,
    }
    return render(request, 'main_store/demo_code_show.html', context)


# Product Name and code store from demo_code_and_name
def product_name_store(request):
    code_name_dict = DemoNameCode.objects.all()
    for code_name in code_name_dict:
        form2 = ProductCodeName()
        print("--------------------------")
        form2.code = code_name.p_code
        print("Code", code_name.p_code)
        form2.name = code_name.p_name
        print("Name", code_name.p_name)
        form2.item_unit = code_name.p_unit
        print("Unit", code_name.p_unit)
        form2.item_under_group = code_name.item_under_group
        print("Group", code_name.item_under_group)
        form2.save()
    return render(request, 'main_store/demo_code_name.html')


def item_group_name_change(request):
    name = "Timber & Stationary"
    group_name = ProductCodeName.objects.filter(Q(item_under_group=name))
    for group in group_name:
        print("--------------------------")
        group.item_under_group = "Timber and Stationary"
        group.save()
        print("Group", group.item_under_group)
    return render(request, 'main_store/demo_code_name.html')


def data_entry_statement(request):
    total_buy = 0
    total_issue = 0
    purchase_info = ''
    issue_info = ''
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        issuer_name = request.POST.get('issuer_name')  # receive product code from post method.
        if issuer_name:
            purchase_info = ProductStore.objects.filter(Q(recorder=issuer_name) & 
                                                        Q(buy_onDate__range=[start_date, end_date]))
    
        if purchase_info:
            for item_buy in purchase_info:
                total_buy = total_buy + float(item_buy.item_quantity)
        print(total_buy)
        if issuer_name:
            issue_info = ProductIssue.objects.filter(Q(issuer_name=issuer_name) &
                                                     Q(date__range=[start_date, end_date]))
        if issue_info:
            for item_issue in issue_info:
                total_issue = total_issue + float(item_issue.item_quantity)
        print(issue_info)
        print(total_issue)
        context = {
            'purchase_info': purchase_info,
            'issue_info': issue_info,
            'total_issue': total_issue,
            'total_buy': total_buy,
            'start_date': start_date,
            'end_date': end_date,
        }
        return render(request, 'main_store/data_entry_statement.html', context)

    context = {

    }
    return render(request, 'main_store/data_entry_statement.html', context)


def indent_form(request):
    submitted = False
    if request.method == 'POST':
        if '_save' in request.POST:
            indent_no = request.POST.get('indent_no')
            form = IndentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                submitted = True
                print("Data Save Indent Form")
            else:
                print('Form not valid!')
    context = {
        'submitted': submitted
    }
    return render(request, "main_store/indent_form.html", context)


def indent_box(request):
    indent_list = Indent.objects.all()
    context = {
        'indent_list': indent_list
    }
    return render(request, "main_store/mailbox_indent.html", context)