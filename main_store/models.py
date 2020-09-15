from django.db import models

# Create your models here.


class ProductStore(models.Model):
    item_code = models.CharField(max_length=100, blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True, null=True)
    item_quantity = models.CharField(max_length=100, blank=True, null=True)
    item_location = models.CharField(max_length=100, blank=True, null=True)
    buy_underJob = models.CharField(max_length=100, blank=True, null=True)
    buy_onDate = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    expire_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    min_balance = models.CharField(max_length=100, blank=True, null=True)
    item_unit = models.CharField(max_length=100, blank=True, null=True)
    item_user = models.CharField(max_length=100, blank=True, null=True)
    item_picture = models.ImageField(upload_to='images/store/product/', blank=True, null=True)
    recorder = models.CharField(max_length=100, blank=True, null=True)
    ref_no = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    item_under_group = models.CharField(max_length=100, blank=True, null=True)


class ProductIssue(models.Model):
    sr_no = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    job_no = models.CharField(max_length=100, blank=True, null=True)
    received_shop = models.CharField(max_length=100, blank=True, null=True)
    item_code = models.CharField(max_length=100, blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True, null=True)
    item_unit = models.CharField(max_length=100, blank=True, null=True)
    issuer_name = models.CharField(max_length=100, blank=True, null=True)  # need migrations
    qty_befr_issue = models.CharField(max_length=100, blank=True, null=True)
    item_quantity = models.CharField(max_length=100, blank=True, null=True)
    qty_after_issue = models.CharField(max_length=100, blank=True, null=True)
    loan_job_no = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)


# Product Searching by code or name
class ProductCodeName(models.Model):  # need migration to alter table data
    code = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    item_unit = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    min_balance = models.CharField(max_length=100, blank=True, null=True)
    item_picture = models.ImageField(upload_to='images/store/name_and_c/', blank=True, null=True)
    item_under_group = models.CharField(max_length=100, blank=True, null=True)


#  All Job Number Database:
class JobNumber(models.Model):  # need migration to alter table data
    job_no = models.CharField(max_length=100, blank=True, null=True)
    job_name = models.CharField(max_length=100, blank=True, null=True)
    job_type = models.CharField(max_length=100, blank=True, null=True)


class DemoJobNumber(models.Model):  # need migration to alter table data
    job_no = models.CharField(max_length=100, blank=True, null=True)
    job_name = models.CharField(max_length=100, blank=True, null=True)
    job_type = models.CharField(max_length=100, blank=True, null=True)


# MRR Input Database.
class MrrIssue(models.Model):
    sender = models.CharField(max_length=100, blank=True, null=True)
    receiver = models.CharField(max_length=100, blank=True, null=True)
    mrr_no = models.CharField(max_length=100, blank=True, null=True)
    mrr_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    po_no = models.CharField(max_length=100, blank=True, null=True)
    po_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    po_qty = models.CharField(max_length=100, blank=True, null=True)
    supplier_name = models.CharField(max_length=100, blank=True, null=True)
    supplier_addrs = models.CharField(max_length=100, blank=True, null=True)
    challan_no = models.CharField(max_length=100, blank=True, null=True)
    challan_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    how_delivary = models.CharField(max_length=100, blank=True, null=True)
    transport_form_no = models.CharField(max_length=100, blank=True, null=True)
    where_delivery = models.CharField(max_length=100, blank=True, null=True)
    delivery_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    quality_shop = models.CharField(max_length=100, blank=True, null=True)
    quality_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    quality_form_no = models.CharField(max_length=100, blank=True, null=True)
    bin_card_writer = models.CharField(max_length=100, blank=True, null=True)
    written_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    oic_store = models.CharField(max_length=100, blank=True, null=True)
    oic_sign = models.ImageField(upload_to='images/main_store/',blank=True, null=True)

    qc_name = models.CharField(max_length=100, blank=True, null=True)
    java_no = models.CharField(max_length=100, blank=True, null=True)
    java_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    ledgerer = models.CharField(max_length=100, blank=True, null=True)
    leadger_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)


# MRR Material List database
class MaterialList(models.Model):
    material_des = models.CharField(max_length=100, blank=True, null=True)
    material_location = models.CharField(max_length=100, blank=True, null=True)
    material_part_no = models.CharField(max_length=100, blank=True, null=True)
    store_code = models.CharField(max_length=100, blank=True, null=True)
    material_qty = models.CharField(max_length=100, blank=True, null=True)
    material_unit = models.CharField(max_length=100, blank=True, null=True)
    mrr_no = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.mrr_no


# Bin Card information Database;
class BinCardInfo(models.Model):
    item_code = models.CharField(max_length=100, blank=True, null=True)
    item_name = models.CharField(max_length=100, blank=True, null=True)
    ref_no = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    job_no = models.CharField(max_length=100, blank=True, null=True)
    item_unit = models.CharField(max_length=100, blank=True, null=True)
    receiver = models.CharField(max_length=100, blank=True, null=True)
    entry_qty = models.CharField(max_length=100, blank=True, null=True)
    issued_qty = models.CharField(max_length=100, blank=True, null=True)
    balance = models.CharField(max_length=100, blank=True, null=True)
    min_balance = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.ref_no


# Material Quality Database Start Here........

class QualitySign(models.Model):
    sign = models.ImageField(upload_to='images/store/quality_sign/', blank=True, null=True)

    def __str__(self):
        return self.sign.url

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="140px" height="80px" />' % self.sign.url)

    image_tag.short_description = 'Image'


class QualitySignDgm(models.Model):
    sign = models.ImageField(upload_to='images/store/quality_sign/', blank=True, null=True)

    def __str__(self):
        return self.sign.url

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="140px" height="80px" />' % self.sign.url)

    image_tag.short_description = 'Image'


class QualitySignStore(models.Model):
    sign = models.ImageField(upload_to='images/store/quality_sign/', blank=True, null=True)

    def __str__(self):
        return self.sign.url

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="140px" height="80px" />' % self.sign.url)

    image_tag.short_description = 'Image'


class QualitySignShop(models.Model):
    sign = models.ImageField(upload_to='images/store/quality_sign/', blank=True, null=True)

    def __str__(self):
        return self.sign.url

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="140px" height="80px" />' % self.sign.url)

    image_tag.short_description = 'Image'


class SignOicStore(models.Model):
    sign = models.ImageField(upload_to='images/store/quality_sign/', blank=True, null=True)

    def __str__(self):
        return self.sign.url

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="140px" height="80px" />' % self.sign.url)

    image_tag.short_description = 'Image'


class MaterialQuality(models.Model):
    send_to = models.CharField(max_length=100, blank=True, null=True)
    quality_no = models.CharField(max_length=100, blank=True, null=True)
    quality_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    po_no = models.CharField(max_length=100, blank=True, null=True)
    po_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    memo_no = models.CharField(max_length=100, blank=True, null=True)
    memo_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    sign_oic_store = models.ManyToManyField(SignOicStore, blank=True)
    responsible_oic = models.ManyToManyField(QualitySignShop, blank=True)
    responsible_oic_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    oic_store_sign = models.ManyToManyField(QualitySignStore, blank=True)
    oic_store_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    dgm_sign = models.ManyToManyField(QualitySignDgm,blank=True)
    dgm_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    gm_sign = models.ManyToManyField(QualitySign, blank=True)
    gm_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    # def __str__(self):
    #     return self.quality_no

    # Show image at admin site using this function...
    # def oic_store_img(self):
    #     from django.utils.html import mark_safe
    #     return mark_safe('<img src="%s" width="140px" height="80px" />' % self.sign_oic_store.url)
    #
    # oic_store_img.short_description = 'Image'

    def get_gm_sign(self):
        list1 = []
        sign = ''
        for p in self.gm_sign.all():
            list1.append(p)
            for j in list1:
                sign = j
        return sign

    def get_dgm_sign(self):
        list1 = []
        sign = ''
        for p in self.dgm_sign.all():
            list1.append(p)
            for j in list1:
                sign = j
        return sign

    def get_oic_store_sign(self):
        list1 = []
        sign = ''
        for p in self.oic_store_sign.all():
            list1.append(p)
            for j in list1:
                sign = j
        return sign

    def get_oic_responsible_oic(self):
        list1 = []
        sign = ''
        for p in self.responsible_oic.all():
            list1.append(p)
            for j in list1:
                sign = j
        return sign

    def get_oic_sign_oic_store(self):
        list1 = []
        sign = ''
        for p in self.sign_oic_store.all():
            list1.append(p)
            for j in list1:
                sign = j
        return sign
# Material Quality Database End Here........


# Material Quality List database
class QualityItemList(models.Model):
    material_des = models.CharField(max_length=100, blank=True, null=True)
    store_code = models.CharField(max_length=100, blank=True, null=True)
    material_unit = models.CharField(max_length=100, blank=True, null=True)
    material_qty = models.CharField(max_length=100, blank=True, null=True)
    quality_no = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.store_code


class DemoNameCode(models.Model):
    p_code = models.CharField(max_length=100, blank=True, null=True)
    p_name = models.CharField(max_length=100, blank=True, null=True)
    p_unit = models.CharField(max_length=100, blank=True, null=True)
    item_under_group = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.p_name


class Indent(models.Model):
    sender_shop = models.CharField(max_length=100, blank=True, null=True)
    receiver_shop = models.CharField(max_length=100, blank=True, null=True)
    indent_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    job_no = models.CharField(max_length=100, blank=True, null=True)
    priority = models.CharField(max_length=100, blank=True, null=True)
    indent_no = models.CharField(max_length=100, blank=True, null=True)
    indent_officer = models.CharField(max_length=100, blank=True, null=True)
    sign_indent_offcr = models.ImageField(upload_to='images/main_store/',blank=True, null=True)
    oic_store = models.CharField(max_length=100, blank=True, null=True)
    sign_oic_store = models.ImageField(upload_to='images/main_store/',blank=True, null=True)

    def __str__(self):
        return self.indent_no


class IndentMaterials(models.Model):
    item_description = models.CharField(max_length=200, blank=True, null=True)
    item_code = models.CharField(max_length=50, blank=True, null=True)
    item_requirement = models.CharField(max_length=50, blank=True, null=True)
    item_unit = models.CharField(max_length=50, blank=True, null=True)
    current_balance = models.CharField(max_length=50, blank=True, null=True)
    prev_buy = models.CharField(max_length=50, blank=True, null=True)
    expect_time = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.item_code