from myapp.models import MainContactModel


def contact_form_processor(request):
    return {
        'context_processor': MainContactModel.objects.all()
    }
