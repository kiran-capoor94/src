from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.conf import settings
from django.core.mail import send_mail

from .forms import ContactForm
from blogs.models import Blog


def home_page(request):
    # print(request.session.get("first_name", "Unknown"))
    # request.session['first_name']
    contact_form = ContactForm(request.POST or None)
    confirm_message = None
    posts = Blog.objects.published().order_by('-timestamp')[0:3]
    context = {
        "title": "Rejuva Aesthetica | Home",
        # "content":" Welcome to the homepage.",
        "form": contact_form,
        "blog": posts,

    }
    if contact_form.is_valid():
        # print(contact_form.cleaned_data)
        # Adding contact form functionality
        full_name = contact_form.cleaned_data['full_name']
        content = contact_form.cleaned_data['content']
        subject = 'Sent from RejuvaAesthetica.com'
        message = '%s %s' % (content, full_name)
        emailFrom = contact_form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True,)
        confirm_message = "Thanks for the message. We will get right back to you."

        if request.is_ajax():
            return JsonResponse({"message": confirm_message})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')
    # if request.user.is_authenticated():
    #     context["premium_content"] = "YEAHHHHHH"
    return render(request, "index.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    confirm_message = None
    context = {
        "title": "Rejuva Aesthetica | Contact",
        "form": contact_form,
        "message": confirm_message,
    }

    if contact_form.is_valid():
        # print(contact_form.cleaned_data)
        # Adding contact form functionality
        full_name = contact_form.cleaned_data['full_name']
        content = contact_form.cleaned_data['content']
        subject = 'Sent from RejuvaAesthetica.com'
        message = '%s %s' % (content, full_name)
        emailFrom = contact_form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True,)
        confirm_message = "Thanks for the message. We will get right back to you."

        if request.is_ajax():
            return JsonResponse({"message": confirm_message})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')

    return render(request, 'contact/view.html', context)


def about_page(request):
    context = {
        "title": "Rejuva Aesthetica | About Page",
    }
    return render(request, "about.html", context)


class PrivacyPolicyView(TemplateView):
    template_name = 'privacy-policy.html'


class TnCView(TemplateView):
    template_name = 'tnc.html'


class HairTreatmentsView(TemplateView):
    template_name = 'services/hair-treatment.html'


class FaceTreatmentsView(TemplateView):
    template_name = 'services/face-treatment.html'


class BodyTreatmentsView(TemplateView):
    template_name = 'services/body-treatment.html'


class SkinTreatmentsView(TemplateView):
    template_name = 'services/skin-treatment.html'


class CosmeticTreatmentsView(TemplateView):
    template_name = 'services/cosmetic-treatment.html'


class BreastTreatmentsView(TemplateView):
    template_name = 'services/breast-treatment.html'


class LaserTreatmentsView(TemplateView):
    template_name = 'services/laser.html'
