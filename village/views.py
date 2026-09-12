from django.shortcuts import render
from django.conf import settings
from .models import Subscription, Contributor

def subscribe(request):
    leaders = Contributor.objects.order_by('-points')[:5]
    subs = Subscription.objects.filter(paid=True)
    total = sum([s.amount for s in subs]) if subs else 0
    total_usd = sum([s.usd_amount for s in subs]) if subs else 0

    if request.method == "POST":
        email = request.POST.get('email')
        ref = request.POST.get('paystack_ref', '')
        if email:
            sub, created = Subscription.objects.get_or_create(
                email=email,
                defaults={'amount': 2000, 'usd_amount': 2.0, 'paid': True, 'paystack_ref': ref}
            )
            if not created:
                sub.paid = True
                sub.paystack_ref = ref
                sub.save()
        return render(request, 'village/subscribe_success.html', {'email': email, 'ref': ref})

    return render(request, 'village/subscribe.html', {
        'leaders': leaders,
        'total': total,
        'total_usd': total_usd,
        'sub_count': subs.count(),
        'paystack_key': getattr(settings, 'PAYSTACK_PUBLIC_KEY', 'pk_test_xxx')
    })

def subscribe_success(request):
    email = request.GET.get('email', '')
    ref = request.GET.get('ref', '')
    return render(request, 'village/subscribe_success.html', {'email': email, 'ref': ref})

def leaderboard(request):
    contributors = Contributor.objects.order_by('-points')
    return render(request, 'village/leaderboard.html', {'contributors': contributors})