from django.shortcuts import render
from django.views.generic import TemplateView
from .models import User, HMCMember, Gallery, Achievement, QuickLinks


def index(request):
    student_designations = [
        'General Secretary',
        'Welfare Secretary',
        'Mess Convener',
        'Cultural Secretary',
        'Literary Secretary',
        'Technical Secretary',
        'Sports Secretary',
        'Maintenance Secretary',
    ]
    other_designations = [
        'Warden',
        'Associate Warden',
        'Caretaker'
    ]

    hmc = HMCMember.objects.all()
    hmc_list = []
    warden_list = []
    for designation in other_designations:
        other_members = hmc.filter(designation=designation)
        for other_member in other_members:
            warden_list.append(other_member)
    for designation in student_designations:
        hmc_members = hmc.filter(designation=designation)
        for hmc_member in hmc_members:
            hmc_list.append(hmc_member)

    hmc_rows = []
    for i in range(0, len(hmc_list), 3):
        hmc_rows.append(hmc_list[i:i + 3])

    achievements = Achievement.objects.all()
    gallery = Gallery.objects.all()
    quick_links = QuickLinks.objects.all()

    return render(request, 'umIndex.html', {'warden_list': warden_list,
                                            'hmc': hmc_rows,
                                            'achievements': achievements,
                                            'gallery': gallery,
                                            'quick_links': quick_links})
