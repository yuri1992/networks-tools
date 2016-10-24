from django.views.generic import FormView


class FormViewWithRequest(FormView):
    def get_form_kwargs(self):
        kwargs = super(FormViewWithRequest, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
