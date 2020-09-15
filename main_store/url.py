from django.conf.urls import url
from django.urls import path, include
from main_store.views import *


urlpatterns = [
    path('main_store', home_store, name='main_store'),
    path('compose_mrr', mrr_compose, name='compose_mrr'),
    path('mrr_show/<mrr_no>/', mrr_show, name='mrr_show'),
    path('mrr_no_receive', mrr_no_receive, name='mrr_no_receive'),
    path('indent_box', indent_box, name='indent_box'),
    path('indent_form', indent_form, name='indent_form'),
    path('product_issue', product_issue, name='product_issue'),
    path('product_store', product_store, name='product_store'),
    path('existing_product_store', existing_product_store, name='existing_product_store'),  # product existing update.
    path('bin_card_state', bin_card_state, name='bin_card_state'),
    path('issuer_state', issuer_state, name='issuer_state'),
    path('product_name_code', product_name_code, name='product_name_code'),
    path('min_balance_list', low_balance_state, name='low_balance_state'),
    path('expire_date_list', expire_date_state, name='expire_date_state'),
    path('purchase_state', purchase_state, name='purchase_state'),
    path('material_balance_state', material_balance_state, name='material_balance_state'),
    path('statement', statement, name='statement'),
    path('data_entry_statement', data_entry_statement, name='data_entry_statement'),

    path('job_number', job_number, name='job_number'),

    
    # Demo code and name
    path('demo_code_input', demo_code_input, name='demo_code_input'),
    path('demo_code_show', demo_code_show, name='demo_code_show'),
    # path('duplicate_in_demo_code', duplicate_in_demo_code, name='duplicate_in_demo_code'),  # Find Duplicate in demo
    # code and Name Model.
    # path('duplicate_in_p_name_code', duplicate_in_p_name_code, name='duplicate_in_p_name_code'),  # Find Duplicate in
    # Product Name and Code model.
    path('product_name_store', product_name_store, name='product_name_store'),
    # path('demo_code_delete', demo_code_delete, name='demo_code_delete'),

    # Demo job name
    path('demo_job_name', demo_job_name, name='demo_job_name'),
    # path('demo_job_name_delete', demo_job_name_delete, name='demo_job_name_delete'),
    path('job_no_store', job_no_store, name='job_no_store'),

    path('item_group_name_change', item_group_name_change, name='item_group_name_change'),


    path('quality_receive', quality_receive, name='quality_receive'),
    path('material_quality/<quality_no>/', material_quality, name='material_quality'),
    path('quality_input', quality_input, name='quality_input'),


    path('gate_pass', gate_pass, name='gate_pass'),
    path('sr_form', sr_form, name='sr_form'),
    path('project_detail_store', project_detail_store, name='project_detail_store'),

    path('autocomplete', autocomplete, name='autocomplete'),
    path('autocomplete_job_no', autocomplete_job_no, name='autocomplete_job_no'),



    path('post_ajax', post_ajax, name='post_ajax'),
    path('ajax_search', ajax_search, name='ajax_search'),
]