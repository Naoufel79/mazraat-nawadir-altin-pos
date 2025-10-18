from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
from Siliana.models import Produit
from datetime import datetime


class Command(BaseCommand):
    help = 'Send daily product list with quantities to email'

    def handle(self, *args, **kwargs):
        try:
            # Get all products
            produits = Produit.objects.all().order_by('nom')
            
            if not produits.exists():
                self.stdout.write(self.style.WARNING('No products found in database'))
                return
            
            # Build email content
            subject = f'Daily Product List - {datetime.now().strftime("%Y-%m-%d")}'
            
            # Create email body
            message = f"Daily Product List Report\n"
            message += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            message += "=" * 60 + "\n\n"
            message += f"{'Product Name':<40} {'Quantity':>15}\n"
            message += "-" * 60 + "\n"
            
            for produit in produits:
                message += f"{produit.nom:<40} {produit.quantite:>15}\n"
            
            message += "-" * 60 + "\n"
            message += f"\nTotal Products: {produits.count()}\n"
            message += f"Total Quantity: {sum(p.quantite for p in produits)}\n"
            
            # Send email
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['kharroubi.naoufel@gmail.com'],
                fail_silently=False,
            )
            
            self.stdout.write(self.style.SUCCESS(
                f'Successfully sent product list to kharroubi.naoufel@gmail.com'
            ))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error sending email: {str(e)}'))
