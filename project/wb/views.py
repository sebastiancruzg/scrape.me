from django.shortcuts import render
from django.http import HttpResponse
from .scrape.amazon_wb.scrape import scrape
from .scrape.models.csv.store_record_csv import store_records
from .models import Resource
from .forms import ScrapeForm

# Create your views here.
def main_page(request):
    return render(request, 'index.html', {'resources': Resource.objects.all()})

def scrape_handler(request):
    if not request.method == 'POST':
        return HttpResponse('Method not allowed', content_type='application/json', status=405)
    form = ScrapeForm(request.POST)
    if not form.is_valid():
        return HttpResponse('Invalid form', content_type='application/json', status=400)

    search_query = form.cleaned_data['search_query'].strip()
    resource_tag = form.cleaned_data['resource_tag']
    url = Resource.objects.get(tag=resource_tag).url

    csv_file = scrape(url, search_query, store_records)

    # Create the HTTP response for downloading the CSV
    response = HttpResponse(csv_file, content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{search_query.replace(" ", "_")}.csv"'

    # Close the in-memory file if not needed anymore
    csv_file.close()

    return response
