from django import forms
from .models import Student, Address, ImageModel

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'  # جميع الحقول في النموذج

class StudentForm(forms.ModelForm):
    # تغيير إلى ModelChoiceField بدلاً من ModelMultipleChoiceField في حال كان لكل طالب عنوان واحد فقط
    addresses = forms.ModelMultipleChoiceField(
        queryset=Address.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # استخدام Select لتحديد عنوان واحد
    )
    
    class Meta:
        model = Student
       # fields = ['name', 'age', 'address']  # التأكد من أن الحقل هو address وليس addresses'
        fields =  ['name', 'age', 'addresses']

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'  # تأكد من أن هذه القيمة ليست بين علامات اقتباس إضافية
