from django.db import models

class Produit(models.Model):
    nom = models.CharField("اسم المنتج", max_length=100)
    quantite = models.PositiveIntegerField("الكمية في المخزون", default=0)
    prix_achat = models.DecimalField("سعر الشراء (دينار)", max_digits=10, decimal_places=2)
    prix_vente = models.DecimalField("سعر البيع (دينار)", max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom


class Achat(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField("الكمية المشتراة")
    date_achat = models.DateField("تاريخ الشراء", auto_now_add=True)

    def save(self, *args, **kwargs):
        self.produit.quantite += self.quantite
        self.produit.save()
        super().save(*args, **kwargs)


class Vente(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField("الكمية المباعة")
    date_vente = models.DateField("تاريخ البيع", auto_now_add=True)

    def total(self):
        return self.quantite * self.produit.prix_vente

    def save(self, *args, **kwargs):
        if self.quantite <= self.produit.quantite:
            self.produit.quantite -= self.quantite
            self.produit.save()
            super().save(*args, **kwargs)
        else:
            raise ValueError("❌ الكمية غير متوفرة في المخزون!")


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'قيد الانتظار'),
        ('confirmed', 'مؤكد'),
        ('cancelled', 'ملغي'),
        ('completed', 'مكتمل'),
    ]
    
    nom = models.CharField("الاسم", max_length=100)
    email = models.EmailField("البريد الإلكتروني", max_length=254, blank=True, null=True)
    wilaya = models.CharField("الولاية", max_length=100)
    ville = models.CharField("المدينة", max_length=100)
    telephone = models.CharField("رقم الهاتف", max_length=20)
    status = models.CharField("الحالة", max_length=20, choices=STATUS_CHOICES, default='pending')
    date_commande = models.DateTimeField("تاريخ الطلب", auto_now_add=True)
    notes = models.TextField("ملاحظات", blank=True, null=True)

    def __str__(self):
        return f"طلب {self.nom} - {self.date_commande.strftime('%Y-%m-%d')}"

    def total(self):
        return sum(item.total() for item in self.orderitem_set.all())

    def save(self, *args, **kwargs):
        # Check if status changed to cancelled
        if self.pk:  # Existing order
            old_order = Order.objects.get(pk=self.pk)
            if old_order.status != 'cancelled' and self.status == 'cancelled':
                # Restore stock for all items
                for item in self.orderitem_set.all():
                    item.produit.quantite += item.quantite
                    item.produit.save()
        super().save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField("الكمية")
    prix = models.DecimalField("السعر", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produit.nom} - {self.quantite}"

    def total(self):
        return self.quantite * self.prix

    def save(self, *args, **kwargs):
        # Only decrement stock when creating a new order item
        if not self.pk:  # New instance
            if self.quantite <= self.produit.quantite:
                self.produit.quantite -= self.quantite
                self.produit.save()
                super().save(*args, **kwargs)
            else:
                raise ValueError(f"❌ الكمية المطلوبة من {self.produit.nom} غير متوفرة!")
        else:
            super().save(*args, **kwargs)
