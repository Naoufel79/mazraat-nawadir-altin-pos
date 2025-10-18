from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from Siliana.models import Produit


class Command(BaseCommand):
    help = 'Setup initial data for the application'

    def handle(self, *args, **kwargs):
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('✓ Created superuser (username: admin, password: admin123)'))
        else:
            self.stdout.write(self.style.WARNING('⚠ Superuser already exists'))

        # Sample products to add
        products = [
            {'nom': 'زيدي', 'quantite': 50, 'prix_achat': 0.800, 'prix_vente': 1.000},
            {'nom': 'بيثر', 'quantite': 30, 'prix_achat': 1.200, 'prix_vente': 1.500},
            {'nom': 'براون تكي', 'quantite': 40, 'prix_achat': 1.500, 'prix_vente': 2.000},
            {'nom': 'اسباني اسود', 'quantite': 25, 'prix_achat': 2.000, 'prix_vente': 2.500},
        ]

        for product_data in products:
            product, created = Produit.objects.get_or_create(
                nom=product_data['nom'],
                defaults={
                    'quantite': product_data['quantite'],
                    'prix_achat': product_data['prix_achat'],
                    'prix_vente': product_data['prix_vente']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Added product: {product.nom}'))
            else:
                self.stdout.write(self.style.WARNING(f'⚠ Product already exists: {product.nom}'))

        self.stdout.write(self.style.SUCCESS('\n✅ Setup completed successfully!'))
        self.stdout.write(self.style.SUCCESS('You can now login with username: admin, password: admin123'))
