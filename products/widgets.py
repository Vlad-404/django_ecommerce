from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as lazy


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = lazy('Remove')
    initial_text = lazy('Current Image')
    input_text = lazy('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
