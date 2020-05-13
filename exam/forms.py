from django import forms
from django.forms.widgets import RadioSelect, Textarea


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_choices_list()]
        self.fields["choices"] = forms.ChoiceField(choices=choice_list,
                                                   widget=RadioSelect)
