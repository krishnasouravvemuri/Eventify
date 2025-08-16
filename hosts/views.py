from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import HostEventForm
from django.shortcuts import get_object_or_404
from .models import EventDetails


def hosts_home(request):
    return render(request, 'hosts_home.html')

def host_event(request):
    if request.method == "POST":
        form = HostEventForm(request.POST, request.FILES)
        
        if form.is_valid():
                EventDetails.objects.create(
                    user=request.user,
                    name=form.cleaned_data['name'],
                    place=form.cleaned_data['place'],
                    date=form.cleaned_data['date'],
                    time=form.cleaned_data['time'],
                    seats=form.cleaned_data['seats'],
                    banner=form.cleaned_data['banner']
                )
                messages.success(request, "Event Created Successfully!")
                form = HostEventForm()  
        else:
            messages.error(request, form.errors)
            form = HostEventForm()  
    else:
        form = HostEventForm()

    return render(request, "host_event.html", {"form": form})

def edit_event(request, event_id):
    event = get_object_or_404(EventDetails, id=event_id)

    if request.method == "POST":
        # Only update fields that have been filled
        updated = False

        new_name = request.POST.get("new_name")
        if new_name:
            event.name = new_name
            updated = True

        new_place = request.POST.get("new_place")
        if new_place:
            event.place = new_place
            updated = True

        new_date = request.POST.get("new_date")
        if new_date:
            event.date = new_date
            updated = True

        new_time = request.POST.get("new_time")
        if new_time:
            event.time = new_time
            updated = True

        new_seats = request.POST.get("new_seats")
        if new_seats:
            event.seats = new_seats
            updated = True

        new_banner = request.FILES.get("new_banner")
        if new_banner:
            event.banner = new_banner
            updated = True

        if updated:
            event.save()
            messages.success(request, "Event updated successfully!")
        else:
            messages.info(request, "No changes were made.")

        return redirect("edit_event", event_id=event.id)

    return render(request, "edit_event.html", {"event": event})

def delete_event(request, event_id):
    event = get_object_or_404(EventDetails, id=event_id)

    if request.method == "POST":
        event.delete()
        messages.success(request, "Event deleted successfully!")
        return redirect("hosts_home")

    return render(request, "view_event.html", {"event": event})

def view_event(request):
    events = EventDetails.objects.filter(user = request.user).order_by('-id')
    for event in events:
        event.remaining_seats = max(0, event.seats - event.registrations.count())
    return render(request, "view_event.html" , {'events': events})
