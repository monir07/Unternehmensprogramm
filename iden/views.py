from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from iden.form import New_iden_form, Preview_iden_form
from iden.models import new_iden, Iden_preview

# Create your views here.

# Login and logout View Start Here....................................


shop_list = ["জাহাজ নির্মাণ শাখা", "যান্ত্রিক বাহির শাখা", "যান্ত্রিক ভিতর শাখা", "নঙ্গর শাখা", "জি এম প্রোডাকশন",
             "প্রধান ভাণ্ডার","বিদ্যুৎ শাখা","পুরকৌশল শাখা", "রেডিও ইলেক্ট্রিক্যাল শাখা", "কার্প্রেন্ট্রি শপ", "রক্ষণাবেক্ষণ শাখা", "নকশা শাখা",
             "পরিকল্পনা শাখা", "আইটি শাখা", "প্রশাসন শাখা", "বাণিজ্যিক শাখা লোকাল", "বাণিজ্যিক শাখা ফরেন",
             "হিউম্যান রিসোর্স শাখা", "অর্থ শাখা", "মূল্য নির্ধারন শাখা"]
shop_list1 = ["Plater_shop","Outdoor","Indoor","Docking","gm_production","main_store", "Electrical"]


@login_required(login_url='login')
def starter_view(request, user_name):
    if user_name == "জাহাজ নির্মাণ শাখা":
        return redirect('plater-shop')

    if user_name == "main_store1":
        return redirect('main_store')
    context = {
        "user_name": user_name,
    }
    return render(request,"iden/home.html", context)


@login_required(login_url='login')
def plater_shop(request):
    user_name = "জাহাজ নির্মাণ শাখা"
    context = {
        'user_name': user_name,

    }
    return render(request,'home/plater_shop.html', context)


def project_list(request):
    user_name = "জাহাজ নির্মাণ শাখা"
    context = {
        'user_name': user_name,

    }
    return render(request,'home/project.html', context)


def project_detail(request):
    user_name = "জাহাজ নির্মাণ শাখা"
    context = {
        'user_name': user_name,

    }
    return render(request,'main_store/project-details_store.html', context)


def services(request):
    user_name = "জাহাজ নির্মাণ শাখা"
    context = {
        'user_name': user_name,

    }
    return render(request,'home/service.html', context)


def contact(request):
    user_name = "জাহাজ নির্মাণ শাখা"
    context = {
        'user_name': user_name,

    }
    return render(request,'home/contact.html', context)


@login_required(login_url='login')
def Compose_iden(request, user_shop):
    submitted = False
    post = None
    prev = None
    form = None
    shop_name = user_shop
    template_name = "iden/compose_idn.html"
    if request.method == 'POST':
        if '_save' in request.POST:
            form = New_iden_form(request.POST, request.FILES)
            if form.is_valid():
                post = form.save()
                submitted = True
                template_name = "iden/compose_idn.html"
                print("Send is OK")
            else:
                print("Form is not valid")
        elif '_preview' in request.POST:
                # don't send data
                prev = Preview_iden_form(request.POST, request.FILES)
                if prev.is_valid():
                    post = prev.save()
                    template_name = "iden/compose_idn.html"
                    print("Preview is OK")
                    print(post.id)
                    draft_id = post.id
                    return redirect('preview', new_preview_id=draft_id)

                else:
                    print("Form is not valid")
    else:
        form = New_iden_form()
    context = {
        'form': form,
        'post': post,
        'prev': prev,
        'submitted': submitted,
        'user_shop': shop_name
    }
    return render(request,template_name, context)

@login_required(login_url='login')
def preview_view(request, new_preview_id):
    iden = Iden_preview.objects.get(id=new_preview_id)
    iden.viewed = True
    iden.save()
    context = {
        "form": iden,
    }
    return render(request, 'iden/iden_pdf.html', context)

def login_vew(request):
    messages = None
    user_name = ""
    n = 0
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=user_name, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                for shop in shop_list1:
                    if shop == user_name:
                        user_name = shop_list[n]
                    n += 1
                return redirect('home', user_name = user_name)

            else:
                messages = "Username OR Password incorrect."
        else:
            messages = "Username OR Password incorrect."
    context = {
        "messages": messages,
    }
    return render(request,"registration/login.html",context)

def logout_view(request):
    logout(request)
    context = {

    }
    return render(request,"registration/logged_out.html",context)


@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change_form.html', {'form': form})
#
# # Compose mail new_iden_view Start Here..................
# @login_required(login_url='login')
# def new_iden_view(request):
#     submitted = False
#     form = New_iden_form(request.POST, request.FILES)
#     if form.is_valid():
#         form.save()
#         submitted = True
#         return render(request, 'iden/index3.html', {'form': form, 'submitted': submitted})
#     else:
#         print("Form is not valid")
#     return render(request, 'iden/index3.html', {'form': form, 'submitted': submitted})
#
# # Iden_pdf view here....................
@login_required(login_url='login')
def iden_pdf_view(request, new_iden_id):
    iden = new_iden.objects.get(id=new_iden_id)
    iden.viewed = True
    iden.save()
    context = {
        "form": iden,
    }
    return render(request, 'iden/iden_pdf.html', context)

@login_required(login_url='login')
def iden_preview(request):
    iden = Iden_preview.objects.get(id=new_iden_id)
    iden.viewed = True
    iden.save()
    context = {
        "form": iden,
    }
    return render(request, 'iden/iden_pdf.html', context)
#
# Shop Wise Iden Show.........................
@login_required(login_url='login')
def iden_MailBox(request,user_shop):
    print(user_shop)
    shopName = user_shop
    count = 0
    iden_list = new_iden.objects.filter(receiver_shop__name=shopName).order_by('-id')
    for iden in iden_list:
        if not iden.viewed:
            count += 1
    context = {
        "iden_list": iden_list,
        "shop_name": shopName,
        "count": count,
    }
    if request.method == "POST":  # This Portion f or Search in same page.
        search_text = request.POST.get('srs', False)  # Here get() parameter come from input type name="" attribute.
        print(search_text)
        if search_text:
            search_res = new_iden.objects.filter((Q(iden_date__icontains=search_text) |
                                                 Q(job_no__icontains=search_text) |
                                                 Q(sender_shop__name__icontains=search_text)) &
                                                 Q(receiver_shop__name=shopName))
            if search_res:
                context = {
                    "search_res": search_res,
                    "iden_list": iden_list,
                    "shop_name": shopName,
                    "count": count,
                }
                return render(request, "iden/mailbox.html", context)
            else:
                messages.error(request, 'no result found')
        # else:
        #     return HttpResponseRedirect('/plater_shop/')
    return render(request, "iden/mailbox.html", context)

@login_required(login_url='login')
def SentMail(request,user_shop):
    shopName = user_shop
    sentlist = new_iden.objects.filter(sender_shop__name=shopName).order_by('-id')
    template = "iden/mailbox.html"
    context = {
        "sentlist": sentlist,
        "shop_name": shopName,
    }
    if request.method == "POST":  # This Portion f or Search in same page.
        search_text = request.POST.get('srs', False)  # Here get() parameter come from input type name="" attribute.
        print(search_text)
        if search_text:
            sent_search = new_iden.objects.filter((Q(iden_date__icontains=search_text) |
                                                 Q(job_no__icontains=search_text) |
                                                 Q(receiver_shop__name__icontains=search_text)) &
                                                 Q(sender_shop__name=shopName))
            if sent_search:
                context = {
                    "sent_search": sent_search,
                    "sentlist": sentlist,
                    "shop_name": shopName,
                }
                return render(request, template, context)
            else:
                messages.error(request, 'no result found')
    return render(request, template, context)


