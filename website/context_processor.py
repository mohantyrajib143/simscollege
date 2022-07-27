from website.models import sims
def context_processor(request):
    data = {}
    data['sims'] = sims.objects.filter(id=1)[:1]
    return data