from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class CSRFExemptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        # we write super.dispatch to get a default despatch call
        # this is in python 2.7 i.e. this super method
        return super(CSRFExemptMixin, self).dispatch(*args, **kwargs)

        # in python >3.0 
        # super().dispatch(*args, **kwargs)