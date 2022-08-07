from website.models import sims, about
def context_processor(request):
    data = {}
    data['sims'] = sims.objects.filter(id=1)[:1]
    data['about'] = about.objects.filter(id=1)[:1]
    return data