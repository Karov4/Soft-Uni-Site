from django.shortcuts import render, redirect

from Soft_Uni_Site.rentals.forms import RentalApplicationForm


def apply_for_rental(request, apartment_id):
    if request.method == 'POST':
        form = RentalApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.applicant = request.user
            application.apartment_id = apartment_id
            application.save()
            return redirect('apartment_detail', apartment_id=apartment_id)
    else:
        form = RentalApplicationForm()
    return render(request, 'apartments/apply.html', {'form': form})
