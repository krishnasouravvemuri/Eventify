from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import HostEventForm
from .models import EventDetails


def hosts_home(request):
    return render(request, 'hosts_home.html')


def host_event(request):

    if request.method == "POST":
        form = HostEventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)  # Don't save yet
            event.user = request.user        # Assign current user
            event.save()                     # Saves and uploads banner to S3
            messages.success(request, "Event Created Successfully!")
            return redirect('hosts_home')
        else:
            messages.error(request, form.errors)
    else:
        form = HostEventForm()

    return render(request, "host_event.html", {"form": form})


def edit_event(request, event_id):

    event = get_object_or_404(EventDetails, id=event_id)

    if request.method == "POST":
        # Bind form to instance but allow partial updates
        form = HostEventForm(request.POST, request.FILES, instance=event)
        
        if form.is_valid():
            # Only save fields that were actually modified
            for field in form.changed_data:
                setattr(event, field, form.cleaned_data[field])
            
            event.save()  # Saves changes and uploads new banner to S3 if provided
            messages.success(request, "Event updated successfully!")
            return redirect("edit_event", event_id=event.id)
        else:
            messages.error(request, form.errors)
    else:
        form = HostEventForm(instance=event)

    return render(request, "edit_event.html", {"form": form, "event": event})


def delete_event(request, event_id):

    event = get_object_or_404(EventDetails, id=event_id)
    if request.method == "POST":
        event.delete()
        messages.success(request, "Event deleted successfully!")
        return redirect("hosts_home")
    return render(request, "view_event.html", {"event": event})


def view_event(request):

    events = EventDetails.objects.filter(user=request.user).order_by('-id')
    for event in events:
        # Check if registrations relation exists
        if hasattr(event, 'registrations'):
            event.remaining_seats = max(0, event.seats - event.registrations.count())
        else:
            event.remaining_seats = event.seats
    return render(request, "view_event.html", {'events': events})
