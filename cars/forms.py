from django import forms
from cars.models import Brand, Car

class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.DecimalField( required=True) 
    photo = forms.ImageField()

    def save(self):
        # criando objeto Carro e preenchendo com dados validos
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )
        car.save() # salva o objeto na tabela Car no BD
        return car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'  # todos os campos
    
    # validar campo "value" sempre começa com "clean_xxxxxx"
    def clean_value(self):
        value = self.cleaned_data.get('value') # pega dado ja limpo 
        if value < 20000:
            self.add_error('value', 'Valor mínimo de carro deve ser maior que R$20.000')
        return value
    # validar ano de fabricação
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year','Infelizmente não trabalhamos com carros fabricados antes de 1975') 
        return factory_year