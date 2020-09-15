from django.contrib import admin
from .models import sender_shopName,receiver_shopName,attention,new_iden

# New Iden admit display setting
class NewIdenModelAdmin(admin.ModelAdmin):
    list_display = ('ref','iden_date','get_senderShop','get_receiverShop','subject','job_no','iden_body','get_attention',
                    'sender_name','sender_designation','sign','attachment')

class SenderShopNameModelAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ReceiverShopModelAdmin(admin.ModelAdmin):
    list_display = ('name',)

class AttentionModelAdmin(admin.ModelAdmin):
    list_display = ('name',)

# END of New Iden Model display setting


# New Iden Model Admin Register Here................
admin.site.register(new_iden,NewIdenModelAdmin)
admin.site.register(sender_shopName,SenderShopNameModelAdmin)
admin.site.register(receiver_shopName,ReceiverShopModelAdmin)
admin.site.register(attention,AttentionModelAdmin)
