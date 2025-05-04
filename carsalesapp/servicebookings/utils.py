
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# ────────────────────────────────────────────────────────────────────────────────────────────────
# Function to get cleaned data from form
# ────────────────────────────────────────────────────────────────────────────────────────────────
#

def get_POST(request, field, default=''):
    return request.POST.get(field, default).strip()


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Function to send notification on booking status update
# ────────────────────────────────────────────────────────────────────────────────────────────────
#
def msg_booking_status(booking):
    # import pdb; pdb.set_trace()
    user_email = booking.created_by.email
    if user_email:
        email_subject = 'Booking Status Updated'
        email_sender = 'noreply.developer00@gmail.com'
        email_recipient = [user_email]

        html_content = render_to_string("notifications/booking-status.html", {
            'status': booking.status,
            'username': booking.created_by.username,
        })
        email_body = strip_tags(html_content)

        email = EmailMultiAlternatives(
            email_subject,
            email_body,
            email_sender,
            email_recipient
        )
        email.attach_alternative(html_content, "text/html")
        # email.send(fail_silently=False)
    else:
        print(f"User {booking.created_by.username} has no email. Cannot send booking confirmation.")


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Function to send email on service status update
# ────────────────────────────────────────────────────────────────────────────────────────────────
#
def msg_service_status(booking):
    user_email = booking.user.email
    if user_email:
        email_subject   = 'Service Status Updated'
        email_sender    = 'noreply.developer00@gmail.com'
        email_recipient = [user_email]

        html_content = render_to_string("notifications/booking-status.html", {
            'status'  : booking.status,
            'username': booking.user.username,
        })
        email_body = strip_tags(html_content)

        email = EmailMultiAlternatives(
            email_subject,
            email_body,
            email_sender,
            email_recipient
        )
        email.attach_alternative(html_content, "text/html")
        email.send(fail_silently=False)
    else:
        print(f"User {booking.user.username} has no email. Cannot send booking confirmation.")


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Function to send email on service status update | Staff
# ────────────────────────────────────────────────────────────────────────────────────────────────
#
def notify_staff_if_needed(record):
    if hasattr(record, 'assigned_to') and record.assigned_to:
        staff_email = record.assigned_to.email
        if staff_email:
            email_subject = 'Assigned Booking Updated'
            email_sender = 'noreply.developer00@gmail.com'
            email_recipient = [staff_email]

            html_content = render_to_string("notifications/staff-notification.html", {
                'status': record.status,
                'username': record.assigned_to.username,
            })
            email_body = strip_tags(html_content)

            email = EmailMultiAlternatives(
                email_subject,
                email_body,
                email_sender,
                [staff_email]
            )
            email.attach_alternative(html_content, "text/html")
            email.send(fail_silently=False)