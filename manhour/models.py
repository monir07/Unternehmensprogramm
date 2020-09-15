from django.db import models

# Create your models here.

class manhour_senderName(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class manhour_receiverName(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
class manhour_shiftName(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class manhour_jobTypeName(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class manhour_jobOfficerName(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class manhour_supvrName(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class manhour_jobNoName(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class New_manhour(models.Model):
    ref = models.CharField(max_length=100, blank=True, null= True)
    manhour_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    manhour_sender = models.ManyToManyField(manhour_senderName)
    manhour_receiver = models.ManyToManyField(manhour_receiverName)
    manhour_jobType = models.ManyToManyField(manhour_jobTypeName)
    manhour_jobNo = models.ManyToManyField(manhour_jobNoName)
    manhour_jobOfficer = models.ManyToManyField(manhour_jobOfficerName)
    manhour_supvr = models.ManyToManyField(manhour_supvrName)
    manhour_shift = models.ManyToManyField(manhour_shiftName)
    manhour_fitter = models.CharField(max_length=100, blank=True, null=True)
    manhour_fitter_Other = models.CharField(max_length=100, blank=True, null=True)
    manhour_welder = models.CharField(max_length=100, blank=True, null=True)
    manhour_welder_Other = models.CharField(max_length=100, blank=True, null=True)
    manhour_gasCutter = models.CharField(max_length=100, blank=True, null=True)
    manhour_gasCutter_Other = models.CharField(max_length=100, blank=True, null=True)
    manhour_grinder = models.CharField(max_length=100, blank=True, null=True)
    manhour_grinder_Other = models.CharField(max_length=100, blank=True, null=True)
    manhour_machineMan = models.CharField(max_length=100, blank=True, null=True)
    manhour_cNc = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.manhour_date

    # for single option select.
    def get_manhour_sender(self):
        return "\n".join([p.name for p in self.manhour_sender.all()])

    # For Multiple option select.
    def get_manhour_receiver(self):
        list1 = []
        for p in self.manhour_receiver.all():
            list1.append(p)
        return list1
    # For Single Option Select.
    def get_manhour_jobType(self):
        return "\n".join([p.name for p in self.manhour_jobType.all()])

    def get_manhour_jobNo(self):
        return "\n".join([p.name for p in self.manhour_jobNo.all()])

    def get_manhour_jobOfficer(self):
        return "\n".join([p.name for p in self.manhour_jobOfficer.all()])

    def get_manhour_supvr(self):
        return "\n".join([p.name for p in self.manhour_supvr.all()])

    def get_manhour_shift(self):
        return "\n".join([p.name for p in self.manhour_shift.all()])

class JobType_name(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class ManpowerType_name(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class New_attendance(models.Model):
    ref = models.CharField(max_length=100, blank=True, null=True)
    attendance_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    attendance_sender = models.ManyToManyField(manhour_senderName)
    attendance_receiver = models.ManyToManyField(manhour_receiverName)
    manpower_type = models.ManyToManyField(ManpowerType_name)
    job_type = models.ManyToManyField(JobType_name)
    manpower_attendance = models.CharField(max_length=100, blank=True, null=True)
    manpower_absence = models.CharField(max_length=100, blank=True, null=True)


    def __unicode__(self):
        return self.attendance_date

        # for single option select.
    def get_attendance_sender(self):
        return "\n".join([p.name for p in self.attendance_sender.all()])

        # For Multiple option select.
    def get_attendance_receiver(self):
        list1 = []
        for p in self.attendance_receiver.all():
            list1.append(p)
        return list1

    def get_manpower_type(self):
        return "\n".join([p.name for p in self.manpower_type.all()])

    def get_job_type(self):
        return "\n".join([p.name for p in self.job_type.all()])
