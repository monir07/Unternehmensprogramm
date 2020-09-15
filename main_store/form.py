from django import forms
from .models import ProductIssue, ProductStore, ProductCodeName, MrrIssue, MaterialList, MaterialQuality, \
    QualityItemList, JobNumber


class ProductStoreForm(forms.ModelForm):
    class Meta:
        model = ProductStore
        fields = ['item_code', 'item_name', 'item_quantity', 'item_unit', 'ref_no', 'buy_onDate', 'buy_underJob',
                  'item_user', 'item_location', 'expire_date', 'min_balance',  'item_picture', 'recorder', 'ref_no',
                  'remarks', 'item_under_group']


class ProductIssueForm(forms.ModelForm):
    class Meta:
        model = ProductIssue
        fields = ['sr_no', 'date', 'job_no', 'received_shop', 'item_code', 'item_name', 'item_unit', 'qty_befr_issue',
                  'issuer_name', 'item_quantity', 'loan_job_no', 'qty_after_issue', 'remarks']


class ProductCodeNameForm(forms.ModelForm):
    class Meta:
        model = ProductCodeName
        fields = ['code', 'name', 'item_unit', 'location', 'min_balance', 'item_picture']


class MrrIssueForm(forms.ModelForm):
    class Meta:
        model = MrrIssue
        fields = ['sender', 'receiver', 'mrr_no', 'mrr_date', 'po_no', 'po_date', 'po_qty', 'supplier_name', 'supplier_addrs',
                  'challan_no', 'challan_date', 'how_delivary', 'transport_form_no', 'where_delivery', 'delivery_date',
                  'quality_shop', 'quality_date', 'quality_form_no', 'bin_card_writer', 'written_date', 'oic_store',
                  'oic_sign', 'qc_name', 'java_no', 'java_date', 'ledgerer', 'leadger_date']


class MaterialListForm(forms.ModelForm):
    class Meta:
        model = MaterialList
        fields = ['material_des', 'material_location', 'material_part_no', 'store_code', 'material_qty', 'material_unit',
                  'mrr_no']


class MaterialQualityForm(forms.ModelForm):
    class Meta:
        model = MaterialQuality
        fields = ['send_to', 'quality_no', 'quality_date', 'po_no', 'po_date', 'memo_no', 'memo_date', 'sign_oic_store',
                  'responsible_oic', 'responsible_oic_date', 'oic_store_sign', 'oic_store_date', 'dgm_sign', 'dgm_date',
                  'gm_sign', 'gm_date']


class QualityItemListForm(forms.ModelForm):
    class Meta:
        model = QualityItemList
        fields = ['material_des', 'store_code', 'material_unit', 'material_qty', 'quality_no']


class JobNumberForm(forms.ModelForm):
    class Meta:
        model = JobNumber
        fields = ['job_no', 'job_name', 'job_type']
