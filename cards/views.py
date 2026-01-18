from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import CardForm
from .models import Card


@login_required(login_url='accounts:login')
def profile(request):
    try:
        card = Card.objects.get(user=request.user)
    except Card.DoesNotExist:
        return redirect('cards:add_profile')
    return render(request, 'cards/profile.html', {'card': card})


@login_required(login_url='accounts:login')
def add_profile(request):
    # Prevent multiple cards
    if Card.objects.filter(user=request.user).exists():
        return redirect('cards:profile')

    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card.save()
            return redirect('cards:profile')
    else:
        form = CardForm()

    return render(request, 'cards/add_profile.html', {'form': form})


@login_required(login_url='accounts:login')
def edit_card(request, uid):
    card = get_object_or_404(Card, uid=uid, user=request.user)

    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES, instance=card)
        if form.is_valid():
            form.save()
            return redirect('cards:profile')
    else:
        form = CardForm(instance=card)

    return render(request, 'cards/edit_profile.html', {'form': form, 'card': card})


def public_profile(request, uid):
    """Public profile view - accessed when NFC card is tapped"""
    card = get_object_or_404(Card, uid=uid)
    return render(request, 'cards/public_profile.html', {'card': card})


def public_download_vcf(request, uid):
    """Download VCF for public profile"""
    card = get_object_or_404(Card, uid=uid)

    vcf_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{card.name}
TEL:{card.phone_number}
EMAIL:{card.email}
ADR:;;{card.address};;;
END:VCARD"""

    response = HttpResponse(vcf_content, content_type='text/vcard')
    response['Content-Disposition'] = f'attachment; filename="{card.name}.vcf"'
    return response


@login_required(login_url='accounts:login')
def download_vcf(request):
    card = get_object_or_404(Card, user=request.user)

    vcf_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{card.name}
TEL:{card.phone_number}
EMAIL:{card.email}
ADR:;;{card.address};;;
END:VCARD"""

    response = HttpResponse(vcf_content, content_type='text/vcard')
    response['Content-Disposition'] = f'attachment; filename="{card.name}.vcf"'
    return response
