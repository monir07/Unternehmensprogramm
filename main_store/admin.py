from django.contrib import admin
from main_store.models import ProductStore, ProductIssue, ProductCodeName, MrrIssue, MaterialList, BinCardInfo, \
    MaterialQuality, QualitySign,  QualitySignDgm, QualitySignStore, QualitySignShop, SignOicStore, DemoNameCode, \
    QualityItemList, JobNumber, DemoJobNumber, Indent, IndentMaterials
import csv
from django.http import HttpResponse


class ProductStoreAdmin(admin.ModelAdmin):
    list_display = ('item_code', 'item_name', 'ref_no', 'item_quantity', 'item_unit', 'item_location', 'buy_underJob',
                    'buy_onDate', 'expire_date', 'min_balance', 'item_user',  'item_picture', 'recorder', 'remarks',
                    'item_under_group')
    search_fields = ('item_code', 'item_name', 'ref_no', 'buy_underJob', 'buy_onDate', 'item_user',  'recorder',
                     'remarks', 'item_under_group')
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response


class ProductIssueAdmin(admin.ModelAdmin):
    list_display = ('sr_no', 'date', 'job_no', 'loan_job_no', 'received_shop', 'item_code', 'item_name', 'item_unit',
                    'qty_befr_issue', 'item_quantity', 'qty_after_issue', 'issuer_name', 'remarks')
    search_fields = ('sr_no', 'date', 'job_no', 'received_shop', 'item_code', 'item_name', 'issuer_name', 'remarks')

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response


class ProductCodeNameAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'item_unit', 'location', 'min_balance', 'item_picture', 'item_under_group')
    search_fields = ('code', 'name', 'item_unit', 'item_under_group')
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response


class MrrIssueAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'mrr_no', 'mrr_date', 'po_no', 'po_date', 'po_qty', 'supplier_name',
                    'supplier_addrs', 'challan_no', 'challan_date', 'how_delivary', 'transport_form_no',
                    'where_delivery', 'delivery_date', 'quality_shop', 'quality_date', 'quality_form_no',
                    'bin_card_writer', 'written_date', 'oic_store', 'oic_sign', 'qc_name', 'java_no', 'java_date',
                    'ledgerer', 'leadger_date')


class MaterialListAdmin(admin.ModelAdmin):
    list_display = ('material_des', 'material_location', 'material_part_no', 'store_code', 'material_qty',
                    'material_unit', 'mrr_no')


class BinCardInfoAdmin(admin.ModelAdmin):
    list_display = ('item_code', 'item_name', 'ref_no', 'date', 'job_no', 'receiver', 'entry_qty', 'issued_qty',
                    'balance', 'min_balance', 'item_unit')
    search_fields = ('item_code', 'item_name', 'ref_no', 'date', 'job_no', 'receiver')


class MaterialQualityAdmin(admin.ModelAdmin):
    list_display = ('send_to', 'quality_no', 'quality_date', 'po_no', 'po_date', 'memo_no', 'memo_date',
                    'get_oic_sign_oic_store', 'get_oic_responsible_oic', 'responsible_oic_date', 'get_oic_store_sign',
                    'oic_store_date', 'get_dgm_sign', 'dgm_date', 'get_gm_sign', 'gm_date')


class QualitySignAdmin(admin.ModelAdmin):
    list_display = ('image_tag',)


class QualitySignDgmAdmin(admin.ModelAdmin):
    list_display = ('image_tag',)


class QualitySignStoreAdmin(admin.ModelAdmin):
    list_display = ('image_tag',)


class QualitySignShopAdmin(admin.ModelAdmin):
    list_display = ('image_tag',)


class SignOicStoreAdmin(admin.ModelAdmin):
    list_display = ('image_tag',)


class DemoCodeNameAdmin(admin.ModelAdmin):
    list_display = ('p_code', 'p_name', 'p_unit', 'item_under_group')


class DemoJobNumberAdmin(admin.ModelAdmin):
    list_display = ('job_no', 'job_name', 'job_type')


class QualityItemListAdmin(admin.ModelAdmin):
    list_display = ('material_des', 'store_code', 'material_qty', 'material_unit', 'quality_no')


class JobNumberAdmin(admin.ModelAdmin):
    list_display = ('job_no', 'job_name', 'job_type')
    search_fields = ('job_no', 'job_type')
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response


class IndentAdmin(admin.ModelAdmin):
    list_display = ('sender_shop', 'receiver_shop', 'indent_date', 'job_no', 'priority', 'indent_no', 'indent_officer',
                  'sign_indent_offcr', 'oic_store', 'sign_oic_store')
    search_fields = ('indent_no', 'indent_date', 'job_no')


class IndentMaterialsAdmin(admin.ModelAdmin):
    list_display = ('item_description', 'item_code', 'item_requirement', 'item_unit', 'current_balance', 'prev_buy',
                    'expect_time')
    search_fields = ('item_code', 'item_description')


# Register your models here.
admin.site.register(ProductStore, ProductStoreAdmin)
admin.site.register(ProductIssue, ProductIssueAdmin)
admin.site.register(ProductCodeName, ProductCodeNameAdmin)
admin.site.register(MrrIssue, MrrIssueAdmin)
admin.site.register(MaterialList, MaterialListAdmin)
admin.site.register(BinCardInfo, BinCardInfoAdmin)

# Material Quality Registration here.
admin.site.register(MaterialQuality, MaterialQualityAdmin)
admin.site.register(QualitySign, QualitySignAdmin)
admin.site.register(QualitySignDgm, QualitySignDgmAdmin)
admin.site.register(QualitySignStore, QualitySignStoreAdmin)
admin.site.register(QualitySignShop, QualitySignShopAdmin)
admin.site.register(SignOicStore, SignOicStoreAdmin)

# Material Quality Item List Registration here.
admin.site.register(QualityItemList, QualityItemListAdmin)

# Job Number Registration here.
admin.site.register(JobNumber, JobNumberAdmin)
admin.site.register(DemoJobNumber, DemoJobNumberAdmin)

# Demo Code and Name Registration Here.....
admin.site.register(DemoNameCode, DemoCodeNameAdmin)

# Indent and indent materials Registration here........
admin.site.register(Indent, IndentAdmin)
admin.site.register(IndentMaterials, IndentMaterialsAdmin)