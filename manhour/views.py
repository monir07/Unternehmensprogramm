from itertools import count

from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
# Create your views here.
from manhour.form import New_manhour_form, New_attendance_form
from manhour.models import New_manhour, New_attendance
from datetime import date
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def Compose_manhour(request):
    submitted = False
    post = None
    prev = None
    form = None
    # shop_name = user_shop
    template_name = "manhour/manhour_ps.html"
    if request.method == 'POST':
        if '_save' in request.POST:
            form = New_manhour_form(request.POST, request.FILES)
            if form.is_valid():
                post = form.save()
                submitted = True
                template_name = "manhour/manhour_ps.html"
                print("Send is OK")
            else:
                print("Form is not valid")
        elif '_preview' in request.POST:
            # don't send data
            prev = New_manhour_form(request.POST, request.FILES)
            if prev.is_valid():
                post = prev.save()
                template_name = "manhour/manhour_ps.html"
                print("Preview is OK")
                print(post.id)
                draft_id = post.id
                return redirect('preview', new_preview_id=draft_id)

            else:
                print("Form is not valid")
    else:
        form = New_manhour_form()
    context = {
        'form': form,
        'post': post,
        'prev': prev,
        'submitted': submitted,
        # 'user_shop': shop_name
    }
    return render(request, template_name, context)


@login_required(login_url='login')
def Manhour_details(request):
    total_list = []
    other_list = []
    gnd_list = []
    count = 0
    iden_list1 = New_manhour.objects.get(id='10')  # Search by current date of every job
    iden_list = New_manhour.objects.filter(manhour_date__date=date.today()) # Search by current date of every job
    # sum of total worker start here
    for hourList in iden_list:
        total = int(hourList.manhour_fitter) + int(hourList.manhour_gasCutter) + int(hourList.manhour_welder) + \
                int(hourList.manhour_machineMan) + int(hourList.manhour_cNc)+int(hourList.manhour_grinder)
        total_list.append(total)
        total_other = int(hourList.manhour_fitter_Other) + int(hourList.manhour_gasCutter_Other) + \
                      int(hourList.manhour_welder_Other) + int(hourList.manhour_grinder_Other)
        other_list.append(total_other)
    for tList, oList in zip(total_list,other_list):
        gnd_total = tList + oList
        gnd_list.append(gnd_total)

    mylist = zip(iden_list, total_list, other_list, gnd_list)

    context = {
        "iden_list": iden_list1,
        "mylist": mylist,
        "count": count,
    }
    if request.method == "POST":  # This Portion f or Search in same page.
        search_text = request.POST.get('srs', False)  # Here get() parameter come from input type name="" attribute.
        print(search_text)
        if search_text:
            search_res = New_manhour.objects.filter((Q(iden_date__icontains=search_text) |
                                                     Q(job_no__icontains=search_text) |
                                                     Q(sender_shop__name__icontains=search_text)) &
                                                    Q(receiver_shop__name=shopName))
            if search_res:
                context = {
                    "search_res": search_res,
                    "iden_list": iden_list,
                    # "shop_name": shopName,
                    "count": count,
                }
                return render(request, "iden/mailbox.html", context)
            else:
                messages.error(request, 'no result found')
        # else:
        #     return HttpResponseRedirect('/plater_shop/')
    return render(request, "manhour/manhour_ps_Show.html", context)


@login_required(login_url='login')
def Compose_attendance(request):
    submitted = False
    post = None
    prev = None
    form = None
    # shop_name = user_shop
    template_name = "manhour/manpower.html"
    if request.method == 'POST':
        if '_save' in request.POST:
            form = New_attendance_form(request.POST, request.FILES)
            if form.is_valid():
                post = form.save()
                submitted = True
                template_name = "manhour/manpower.html"
                print("Send is OK")
            else:
                print("Form is not valid")
        elif '_preview' in request.POST:
            # don't send data
            prev = New_manhour_form(request.POST, request.FILES)
            if prev.is_valid():
                post = prev.save()
                template_name = "manhour/manpower.html"
                print("Preview is OK")
                print(post.id)
                draft_id = post.id
                return redirect('preview', new_preview_id=draft_id)

            else:
                print("Form is not valid")
    else:
        form = New_manhour_form()
    context = {
        'form': form,
        'post': post,
        'prev': prev,
        'submitted': submitted,
        # 'user_shop': shop_name
    }
    return render(request, template_name, context)


@login_required(login_url='login')
def Attendance_manpower(request):

    total_p = []
    total_a = []
    sl = []
    g_total_p = 0
    g_total_a = 0
    grand_total = 0
    count = 0
    attend_list1 = New_attendance.objects.get(id='5')  # Search by current date of every job
    attend_list = New_attendance.objects.filter(attendance_date__date=date.today()) # Search by current date of every job
    # sum of total worker start here
    for attend in attend_list:
        total_p.append(int(attend.manpower_attendance) + int(attend.manpower_absence))
        total_a.append(int(attend.manpower_absence))
        g_total_p += int(attend.manpower_attendance)  # grand total present
        g_total_a += int(attend.manpower_absence)  # grand total absent
        grand_total = g_total_p + g_total_a  # grand total manpower
        count += 1
        sl.append(count)
    mylist = zip(attend_list, total_p, total_a, sl)
    context = {
        "attend_list1": attend_list1,  # header display sender name and reciever name.
        "mylist": mylist,  # attendance information list.
        "g_total_p": g_total_p,
        "g_total_a": g_total_a,
        "grand_total": grand_total,
        "sl": sl,
    }
    if request.method == "POST":  # This Portion f or Search in same page.
        search_text = request.POST.get('srs', False)  # Here get() parameter come from input type name="" attribute.
        print(search_text)
        if search_text:
            search_res = New_manhour.objects.filter((Q(iden_date__icontains=search_text) |
                                                     Q(job_no__icontains=search_text) |
                                                     Q(sender_shop__name__icontains=search_text)) &
                                                    Q(receiver_shop__name=shopName))
            if search_res:
                context = {
                    "search_res": search_res,
                    "iden_list": iden_list,
                    # "shop_name": shopName,
                    "count": count,
                }
                return render(request, "iden/mailbox.html", context)
            else:
                messages.error(request, 'no result found')
        # else:
        #     return HttpResponseRedirect('/plater_shop/')
    return render(request, "manhour/attendManhour_ps_Show.html", context)


def Attendance_show(request):
    context = {

    }
    return render(request, "manhour/attendManhour_ps_Show.html", context)
