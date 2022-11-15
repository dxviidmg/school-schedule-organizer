from .models import Schedule
from django import forms


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        exclude = ['_class']

#	def clean(self):
#		cleaned_data = super(ScheduleForm, self).clean()
#		checkin_time = cleaned_data.get("checkin_time")
#		checkout_time = cleaned_data.get("checkout_time")

#        if checkin_time

#		if email != confirm_email:
#			raise forms.ValidationError({'email': ["Emails no coinciden"]})

#		try:
#			User.objects.get(email=email)#.exclude(pk=self.instance.pk)
#			raise forms.ValidationError({'email': ["Email ya regristrado"]})
#		except User.DoesNotExist:
#			pass