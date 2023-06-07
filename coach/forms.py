from django.forms import ModelForm
from django import forms
from .models import task, session


class SessionUpdate(forms.ModelForm):


    #timing= forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    estimation = forms.IntegerField(widget=forms.NumberInput(attrs={ "class": "form-control" , "min":"0", "max":"90" }))
    timing = forms.DateField(required=True, widget=forms.widgets.DateInput(attrs={'type': 'datetime-local', "id": "timePicker", "class": "form-control", "format": "dd-mm-yyyy",}))

    timing.widget.attrs["required"] = "required"

    sessions = forms.ModelMultipleChoiceField(
        queryset=session.objects.all(),
        widget=forms.SelectMultiple(attrs={"id": "exampleFormControlSelect2", "multiple class": "form-control"})
    )



    class Meta:
        model = session
        fields = ['name', 'detail', 'timing', 'estimation', 'sessions']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control w-100', 'type': 'text'}),
            'detail': forms.EmailInput(attrs={'class': 'form-control w-100', 'type': 'text'}),
            'timing': forms.DateInput(attrs={'class': 'form-control '}),


        }





class ExerciseForm(forms.ModelForm):

    REST_CHOICES = (
        (1, '15 seconds'),
        (2, '30 seconds'),
        (3, '1 minute'),
        (4, '1 minute 30 sec'),
        (5, '2 minutes')
    )

    SET_CHOICES = (
        (1, 'ONE'),
        (2, 'TWO'),
        (3, 'THREE'),
        (4, 'FOUR'),
        (5, 'FIVE')
    )


    description = forms.CharField(widget=forms.Textarea(attrs={ "class": "form-control", "rows":"4", "col":"10" , "place-holder":"Description" }))
    set = forms.ChoiceField(label='Set', widget=forms.Select(attrs={ "class": "form-control"}), choices=SET_CHOICES)
    rest_time = forms.ChoiceField(label='Rest Time', widget=forms.Select(attrs={"class": "form-control"}), choices=REST_CHOICES)


    class Meta:
        model = task
        fields = [ 'description', 'set', 'rest_time']




class SessionForm(forms.ModelForm):
    class Meta:
        model = session
        fields = ['name', 'detail']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control w-100', 'type': 'text'}),
            'detail': forms.TextInput(attrs={'class': 'form-control w-100', 'type': 'text'}),
        }











