from website.models import contact
def context_processor(request):
    data = {}
    data['contact'] = contact.objects.all()
    return data