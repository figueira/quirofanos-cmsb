from django import forms
from django.core.exceptions import ValidationError

class BaseForm(forms.Form):
    ''' Clase base que extiende a la clase django.forms.Form que agrega funcionalidad para remover espacios en blanco al principio y al final de los datos ingresados '''
    def _clean_fields(self):
        ''' Sobreescribe el _clean_fields(), agregando funcionalidad para remover espacios en blanco al principio y al final de los datos ingresados '''
        for name, field in self.fields.items():
            # value_from_datadict() gets the data from the data dictionaries.
            # Each widget type knows how to retrieve its own data, because some
            # widgets split data over several HTML fields.
            value = field.widget.value_from_datadict(self.data, self.files,
                self.add_prefix(name))

            try:
                if isinstance(field, forms.FileField):
                    initial = self.initial.get(name, field.initial)
                    value = field.clean(value, initial)
                else:
                    if isinstance(value, basestring):
                        value = field.clean(value.strip())
                    else:
                        value = field.clean(value)
                self.cleaned_data[name] = value
                if hasattr(self, 'clean_%s' % name):
                    value = getattr(self, 'clean_%s' % name)()
                    self.cleaned_data[name] = value
            except ValidationError, e:
                self._errors[name] = self.error_class(e.messages)
                if name in self.cleaned_data:
                    del self.cleaned_data[name]
