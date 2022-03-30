from django import  forms

class NewEntryForm(forms.Form):
    encyc_title=forms.CharField(
        label='Enter title of new Encyclopedia',
        required=True
    )
    encyc_content=forms.CharField( label='Enter details of new course',
                                    widget=forms.Textarea(
                       attrs={'style': 'height: 240px;width:50%'}),
                                    required=True)


class NewEditForm(forms.Form):
    encyc_title = forms.CharField(
        label='Enter title of new Encyclopedia',
        required=True
    )
    encyc_content = forms.CharField(label='Enter details of new course',
                                    widget=forms.Textarea(
                                        attrs={'style': 'height: 240px;width:50%'}),
                                    required=True)
