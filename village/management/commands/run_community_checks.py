from django.core.management.base import BaseCommand
from village.models import Contributor, Contribution, Subscription

class Command(BaseCommand):
    help = '3 Scripts: 1=Auto-Moderation 2=Reward 3=Revenue Split - Pecuniary benefit'

    def handle(self, *args, **kwargs):
        # SCRIPT 1: Auto-Moderation & Quality Check
        self.stdout.write(self.style.WARNING("=== SCRIPT 1: Auto-Moderation ==="))
        pending = Contribution.objects.filter(approved=False)
        if not pending.exists():
            self.stdout.write("No pending contributions")
        for c in pending:
            if len(c.title) < 5 or "spam" in c.title.lower() or "xxx" in c.title.lower():
                self.stdout.write(self.style.ERROR(f"❌ FLAGGED spam: {c.title} - DELETED"))
                c.delete()
            else:
                c.approved = True
                c.points_given = 50 if c.type == 'course' else 30
                c.save()
                c.contributor.points += c.points_given
                c.contributor.naira_earned = c.contributor.points * 5
                c.contributor.save()
                self.stdout.write(self.style.SUCCESS(f"✅ APPROVED {c.title} -> {c.contributor.user.username} +{c.points_given}pts"))

        # SCRIPT 2: Contribution Tracker & Leaderboard
        self.stdout.write(self.style.WARNING("\n=== SCRIPT 2: Leaderboard - Who gets paid ==="))
        leaders = Contributor.objects.order_by('-points')[:10]
        if not leaders.exists():
            self.stdout.write("No contributors yet - Invite ABIAPOLY students!")
        for rank, contrib in enumerate(leaders, 1):
            self.stdout.write(f"{rank}. {contrib.user.username} ({contrib.igbo_name}): {contrib.points}pts = ₦{contrib.naira_earned}")

        # SCRIPT 3: Paywall & Revenue Split
        self.stdout.write(self.style.WARNING("\n=== SCRIPT 3: Revenue Split ==="))
        paid_subs = Subscription.objects.filter(paid=True)
        total = sum([s.amount for s in paid_subs])
        self.stdout.write(f"Total Revenue: ₦{total} from {paid_subs.count()} subscribers")
        if total > 0:
            self.stdout.write(f"CEO 40% = ₦{total*0.4:.0f} (for Starlink/NEPA/Domain)")
            self.stdout.write(f"Contributors 30% = ₦{total*0.3:.0f}")
            self.stdout.write(f"Community 20% = ₦{total*0.2:.0f}")
            self.stdout.write(f"Server/Power 10% = ₦{total*0.1:.0f}")
        else:
            self.stdout.write("No paid subscriptions yet - Add Paystack button!")
            self.stdout.write("Target: 50 subs x ₦2000 = ₦100,000 for CAC + domain + Starlink")