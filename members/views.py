from django.shortcuts import render , redirect , get_object_or_404
from django.urls import reverse
from django.contrib import messages
from hosts.models import EventDetails
from .models import MemberDetails
import qrcode
import io
import uuid
import base64

def members_home(request):
    events  = EventDetails.objects.all().order_by('-id')
    for event in events:
        event.remaining_seats = event.seats - event.registrations.count()
    return render(request , 'members_home.html' , {'events': events})

def event_register(request, event_id):
    event = get_object_or_404(EventDetails, id=event_id)

    remaining_seats = max(0, event.seats - event.registrations.count())

    if request.method == "POST":
        member_names = request.POST.getlist('member_name')
        total_members = len(member_names)

        if remaining_seats == 0:
            messages.error(request , "Seats over!")
            return redirect(request.path)

        if total_members > remaining_seats:
            messages.error(request, f"Only {remaining_seats} seats are available.")
            return redirect(request.path)

        # Generate a single registration code for this session
        session_code = str(uuid.uuid4()).replace('-', '')[:12].upper()

        for name in member_names:
            if name.strip():
                MemberDetails.objects.create(
                    user=request.user,
                    event=event,
                    member_name=name,
                    no_of_members=total_members,
                    registration_code=session_code
                )

        messages.success(request, "Registration successful!")
        return redirect(request.path)

    return render(request, 'event_register.html', {"event": event , "remaining_seats": remaining_seats})

def show_registrations(request):
    # Get all MemberDetails for the user
    all_members = MemberDetails.objects.filter(user=request.user)

    # Group by registration_code
    grouped_sessions = []
    unique_codes = all_members.values_list('registration_code', flat=True).distinct()

    for code in unique_codes:
        members_in_session = all_members.filter(registration_code=code)
        event = members_in_session.first().event  # All members in session belong to same event
        grouped_sessions.append({
            'registration_code': code,
            'event': event,
            'members': members_in_session,
            'banner': event.banner
        })

    return render(request, 'show_registrations.html', {
        'grouped_sessions': grouped_sessions
    })

def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(MemberDetails, id=ticket_id)
    return render(request, 'ticket_detail.html', {'ticket': ticket})

def show_ticket(request, registration_code):
    # Fetch all members in this registration session
    tickets = MemberDetails.objects.filter(user=request.user, registration_code=registration_code)
    event = tickets.first().event

    member_names = [t.member_name for t in tickets]
    num_members = len(member_names)

    # Prepare QR code data
    qr_data = f"Event: {event.name}\nDate: {event.date} {event.time}\nRegistered Members ({num_members}):\n"
    qr_data += "\n".join(member_names)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=4,
        border=2,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return render(request, 'show_ticket.html', {
        'qr_code': img_str,
        'event': event,
        'member_names': member_names,
        'num_members': num_members
    })