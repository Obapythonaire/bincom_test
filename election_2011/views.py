# election/views.py
from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from .models import PollingUnit, AnnouncedPuResults,  AnnouncedLgaResults, AnnouncedWardResults,  AnnouncedStateResults, Lga
from .forms import NewPollingUnitForm


def home(request):
    return render(request, 'election_2011/home.html')

# For Ques 1 on displaying individual polling unit results
def polling_unit_results(request, pu_id):
    pu = get_object_or_404(PollingUnit, uniqueid=pu_id)
    results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=pu_id)
    return render(request, 'election_2011/polling_unit.html', {'pu': pu, 'results': results})

def polling_units_list(request):
    polling_units = PollingUnit.objects.all()
    return render(request, 'election_2011/polling_units.html', {'polling_units': polling_units})


# For question 2 on displaying sum results for LGAs

def lga_results(request):
    # Get distinct LGAs from the Lga model
    lgas = Lga.objects.all().values('lga_id', 'lga_name')
    # lgas = Lga.objects.all()
    
    # print(lgas)  # Debugging: Check if LGAs are being fetched
    
    summed_results = None
    selected_lga = None

    if 'lga_id' in request.GET:
        selected_lga = request.GET.get('lga_id')

        # Filter polling units based on selected LGA
        polling_units = PollingUnit.objects.filter(lga_id=selected_lga).values_list('uniqueid', flat=True)

        # Sum up the results for the parties in the selected LGA's polling units
        summed_results = AnnouncedPuResults.objects.filter(
            polling_unit_uniqueid__in=polling_units
        ).values('party_abbreviation').annotate(total_score=Sum('party_score'))

    return render(request, 'election_2011/lga_results.html', {
        'lgas': lgas,
        'summed_results': summed_results,
        'selected_lga': selected_lga
    })


# For question 3 on adding and storing new polling unit result
def new_polling_unit(request):
    if request.method == 'POST':
        form = NewPollingUnitForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'election_2011/new_polling_unit.html', {'form': NewPollingUnitForm(), 'success': True})
    else:
        form = NewPollingUnitForm()
    return render(request, 'election_2011/new_polling_unit.html', {'form': form})


def ward_results(request):
    # Retrieve all ward results
    ward_results = AnnouncedWardResults.objects.all()
    return render(request, 'election_2011/ward_results.html', {'ward_results': ward_results})

def state_results(request):
    # Retrieve all state results
    state_results = AnnouncedStateResults.objects.all()
    return render(request, 'election_2011/state_results.html', {'state_results': state_results})

