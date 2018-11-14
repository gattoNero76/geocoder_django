from django.shortcuts import render
from requests import request

from geo_app.models import Address

import io, pandas
from geopy.geocoders import Nominatim
from datetime import datetime, date

import csv

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    return render(request, 'index.html')

def success(request):
    global file

    if request.method == 'POST':
        file = request.FILES['file']
        table_data = file.read().decode('latin-1')
        our_date = date.today()
        for line in table_data:
            new_file = open(str(our_date)+'file.csv', 'a', newline='')
            new_file.write(line)
        new_file.close()

        data = csv.reader(open(str(our_date)+'file.csv'))
        nom = Nominatim()
        r_time = datetime.today()
        for row in data:
            if row[0] !='Address':
                adr = Address()
                adr.address = row[0]

                location = nom.geocode(row[0])
                adr.iteration = r_time
                adr.coordinates = location
                adr.latitude = location.latitude
                adr.longitude = location.longitude
                # adr.longitude = adr.coordinates.apply(lambda x: x.longitude if x!=None else None)
                adr.save()

        addresses = Address.objects.filter(iteration = r_time)
        return render(request, 'success.html', {'address_records': addresses})

    else:
        return render(request, 'index.html', text="Something went wrong")
