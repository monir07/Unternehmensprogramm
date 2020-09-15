from django import forms
from .models import New_manhour,New_attendance

class New_manhour_form(forms.ModelForm):
    class Meta:
        model = New_manhour
        fields = ['ref', 'manhour_date', 'manhour_sender', 'manhour_receiver', 'manhour_jobType', 'manhour_jobNo',
                  'manhour_jobOfficer', 'manhour_supvr', 'manhour_shift', 'manhour_fitter', 'manhour_fitter_Other',
                  'manhour_welder', 'manhour_welder_Other', 'manhour_gasCutter', 'manhour_gasCutter_Other',
                  'manhour_grinder','manhour_grinder_Other', 'manhour_machineMan', 'manhour_cNc']

class New_attendance_form(forms.ModelForm):
    class Meta:
        model = New_attendance
        fields = ['ref', 'attendance_date', 'attendance_sender', 'attendance_receiver', 'manpower_type', 'job_type',
                  'manpower_attendance', 'manpower_absence']