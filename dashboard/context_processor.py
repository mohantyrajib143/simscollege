from website.models import contact
def context_processor(request):
    data = {}
    data['contact'] = contact.objects.all().order_by('-id')[:5]
    return data