from django.contrib import admin
from .models import manhour_senderName, manhour_receiverName, manhour_shiftName, manhour_jobTypeName, \
    manhour_jobOfficerName, manhour_supvrName, manhour_jobNoName, New_manhour, New_attendance, JobType_name, \
    ManpowerType_name


# New Iden admin display setting
class New_manhourModelAdmin(admin.ModelAdmin):
    list_display = ('ref', 'manhour_date', 'get_manhour_sender', 'get_manhour_receiver', 'get_manhour_jobType',
                    'get_manhour_jobNo', 'get_manhour_jobOfficer', 'get_manhour_supvr', 'get_manhour_shift',
                    'manhour_fitter', 'manhour_fitter_Other', 'manhour_welder', 'manhour_welder_Other',
                    'manhour_gasCutter', 'manhour_gasCutter_Other', 'manhour_grinder', 'manhour_grinder_Other',
                    'manhour_machineMan', 'manhour_cNc')

class Manhour_senderNameAdmin(admin.ModelAdmin):
    list_display = ('name',)

class Manhour_receiverNameAdmin(admin.ModelAdmin):
    list_display = ('name',)

class Manhour_shiftNameAdmin(admin.ModelAdmin):
    list_display = ('name',)

class Manhour_jobTypeNameAdmin(admin.ModelAdmin):
    list_display = ('name',)

class manhour_jobNoNameAdmin(admin.ModelAdmin):
    list_display = ('name',)

class Manhour_jobOfficerNameAdmin(admin.ModelAdmin):
    list_display = ('name',)

class Manhour_supvrNameNameAdmin(admin.ModelAdmin):
    list_display = ('name',)

# New Attendance Admin Model
class New_attendanceAdmin(admin.ModelAdmin):
    list_display = ('ref', 'attendance_date', 'get_attendance_sender', 'get_attendance_receiver', 'get_manpower_type', 'get_job_type',
                  'manpower_attendance', 'manpower_absence')

class JobType_NameAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ManpowerType_NameAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(New_manhour, New_manhourModelAdmin)
admin.site.register(manhour_senderName, Manhour_senderNameAdmin)
admin.site.register(manhour_receiverName, Manhour_receiverNameAdmin)
admin.site.register(manhour_shiftName, Manhour_shiftNameAdmin)
admin.site.register(manhour_jobTypeName, Manhour_jobTypeNameAdmin)
admin.site.register(manhour_jobOfficerName, Manhour_jobOfficerNameAdmin)
admin.site.register(manhour_jobNoName, manhour_jobNoNameAdmin)
admin.site.register(manhour_supvrName, Manhour_supvrNameNameAdmin)
# New Attendance model register
admin.site.register(New_attendance, New_attendanceAdmin)
admin.site.register(JobType_name, JobType_NameAdmin)
admin.site.register(ManpowerType_name, ManpowerType_NameAdmin)
