from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from company.models import *
import json
# Create your views here.

# def data_page(request):
#     information={
#         'name': 'PRUEBA django to vue',
#         'tipo': 'funcional'
#     }
#     return render(request,'data.html',{'information': information})

def data_page(request):
    information = {
        'dataThings':[
                {
                    'image': "thing-1",
                    'title': "Sign Up",
                    'body': "Sign Up Completes all the work associated with planning and processing",
                },
                {
                    'image': "thing-2",
                    'title': "Worth of Money",
                    'body': "After successful access then book from exclusive deals & pricing",
                },
                {
                    'image': "thing-3",
                    'title': "Exciting Travel",
                    'body': "Start and explore a wide range of exciting travel experience.",
                },
            ],
        'dataExclusiveDeals': [
            {
                'cards': [
                    {
                        'city': "Madrid",
                        'rating': "4.8",
                        'country': "Spain",
                        'old_price': "950",
                        'new_price': "850",
                        'image':"Madrid",
                    },
                    {
                        'city': "Firenze",
                        'rating': "4.5",
                        'country': "Italy",
                        'old_price': "850",
                        'new_price': "750",
                        'image':"Firense",
                    },
                    {
                        'city': "Paris",
                        'rating': "4.4",
                        'country': "France",
                        'old_price': "699",
                        'new_price': "599",
                        'image': "Paris",
                    },
                    {
                        'city': "London",
                        'rating': "4.8",
                        'country': "UK",
                        'old_price': "850",
                        'new_price': "850",
                        'image': "London",
                    },
                ],
            },

            {
                'cards': [
                    {
                        'city': "Paris",
                        'rating': "4.4",
                        'country': "France",
                        'old_price': "699",
                        'new_price': "599",
                        'image': "Paris",
                    },
                    {
                        'city': "Firenze",
                        'rating': "4.5",
                        'country': "Italy",
                        'old_price': "850",
                        'new_price': "750",
                        'image': "Firense",
                    },
                    {
                        'city': "London",
                        'rating': "4.8",
                        'country': "UK",
                        'old_price': "850",
                        'new_price': "850",
                        'image': "London",
                    },
                    {
                        'city': "Madrid",
                        'rating': "4.8",
                        'country': "Spain",
                        'old_price': "950",
                        'new_price': "850",
                        'image': "Madrid",
                    },
                ],
            },
        ],
        'dataGetUpdate': [
            {
                'cards': [
                    {
                        'text': "The Amazing Difference a Year of Travelling .",
                        'date': "July 27, 2021",
                        'image': "amazing-diference-year",
                    },
                    {
                        'text': "The Amazing Difference a Year of Travelling .",
                        'date': "July 27, 2021",
                        'image': "travel-for-enough",
                    },
                    {
                        'text': "The Amazing Difference a Year of Travelling .",
                        'date': "July 27, 2021",
                        'image': "save-money-while",
                    },
                ],
            },

            {
                'cards': [
                    {
                        'text': "The Amazing Difference a Year of Travelling .",
                        'date': "July 27, 2021",
                        'image': "amazing-diference-year",
                    },
                    {
                        'text': "The Amazing Difference a Year of Travelling .",
                        'date': "July 27, 2021",
                        'image': "travel-for-enough",
                    },
                    {
                        'text': "The Amazing Difference a Year of Travelling .",
                        'date': "July 27, 2021",
                        'image': "save-money-while",
                    },
                ],
            },
        ],
        'dataMainBanner': [
            {
                'name': "Location",
                'text': "Where are you doing",
                'options_list': ["op1", "op2", "op3"],
            },
            {
                'name': "'date'",
                'text': "Where are you doing2",
                'options_list': ["op4", "op5", "op6"],
            },
            {
                'name': "Guest",
                'text': "Where are you doing3",
                'options_list': ["op7", "op8", "op9"],
            },
        ],
        'dataVacationPlan': [
            {
                'cards': [
                    {
                        'city': "Rome, Italy",
                        'price': "5.42K",
                        'quantity_days': "10 Days Trip",
                        'rating': "4.8",
                        'image': "osaka",
                    },
                    {
                        'city': "London, UK",
                        'price': "2.42K",
                        'quantity_days': "07 Days Trip",
                        'rating': "4.7",
                        'image': "london2",
                    },
                    {
                        'city': "Osaka,Japan",
                        'price': "5.42K",
                        'quantity_days': "10 Days Trip",
                        'rating': "4.8",
                        'image': "osaka",
                    },
                ],
            },

            {
                'cards': [
                    {
                        'city': "Rome, Italy",
                        'price': "$5.42K",
                        'quantity_days': "10 Days trip",
                        'rating': "4.8",
                        'image': "osaka",
                    },
                    {
                        'city': "London, UK",
                        'price': "$2.42K",
                        'quantity_days': "07 Days trip",
                        'rating': "4.7",
                        'image': "london2",
                    },
                    {
                        'city': "Osaka,Japan",
                        'price': "$5.42K",
                        'quantity_days': "10 Days trip",
                        'rating': "4.8",
                        'image': "osaka",
                    },
                ],
            },
        ]
        }
    return JsonResponse({'djangoToVue': information})

def convert(obj):
    data = [item.__dict__ for item in obj]
    data = [item for item in data if '_state' in item]
    for item in data:
        del item['_state']
    json_data = json.dumps(data)
    return json_data

def data_things(request):
    dataThing = Thing.objects.all()
    dataThing=convert(dataThing)
    return HttpResponse(dataThing,content_type='application/json')

def data_exclusive(request):
    dataExclusive = ExclusiveDeal.objects.all()
    dataExclusive = convert(dataExclusive)

    return HttpResponse(dataExclusive,content_type='application/json')

def data_GetUpdate(request):
    dataGetUpdate = GetUpdate.objects.all()
    dataGetUpdate = convert(dataGetUpdate)
    return HttpResponse(dataGetUpdate,content_type='application/json')

def data_MainBanner(request):
    dataMainBanner = MainBanner.objects.all()
    dataMainBanner = convert(dataMainBanner)
    return HttpResponse(dataMainBanner,content_type='application/json')

def data_VacationPlan(request):
    dataVacationPlan = VacationPlan.objects.all()
    dataVacationPlan = convert(dataVacationPlan)
    return HttpResponse(dataVacationPlan, content_type='application/json')