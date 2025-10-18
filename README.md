# مزرعة نوادر التين - نظام نقطة البيع
# Mazra'at Nawadir Al-Tin - Point of Sale System

نظام إدارة مبيعات ومخزون متكامل لمزرعة نوادر التين مع صفحة طلبات عامة للعملاء.

A complete sales and inventory management system for Nawadir Al-Tin Farm with a public order page for customers.

## 🌟 Features / المميزات

### For Administrators / للإدارة
- 📦 **Product Management** - إدارة المنتجات
- 📊 **Sales Reports** - تقارير المبيعات
- 💰 **Sales Processing** - معالجة المبيعات
- 📋 **Order Management** - إدارة الطلبات
- 📈 **Stock Management** - إدارة المخزون
- 📧 **Daily Email Reports** - تقارير بريد إلكتروني يومية
- 🔄 **Order Status Tracking** - تتبع حالة الطلبات
- 📤 **Excel Export** - تصدير إلى Excel

### For Customers / للعملاء
- 🛒 **Public Order Page** - صفحة طلبات عامة
- ✅ **Real-time Stock Availability** - توفر المخزون في الوقت الفعلي
- 📱 **Mobile Responsive** - متوافق مع الهواتف المحمولة
- 🏪 **Easy Ordering** - طلب سهل

## 🚀 Installation / التثبيت

### Prerequisites / المتطلبات
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps / خطوات الإعداد

1. **Clone the repository / استنساخ المستودع**
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME/Point_De_Vente
```

2. **Create virtual environment / إنشاء بيئة افتراضية**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Mac/Linux
```

3. **Install dependencies / تثبيت المتطلبات**
```bash
pip install django openpyxl
```

4. **Run migrations / تشغيل الترحيلات**
```bash
python manage.py migrate
```

5. **Create superuser / إنشاء مستخدم إداري**
```bash
python manage.py createsuperuser
```

6. **Load initial data (optional) / تحميل البيانات الأولية (اختياري)**
```bash
python manage.py setup_data
```

7. **Run the server / تشغيل الخادم**
```bash
python manage.py runserver
```

8. **Access the application / الوصول إلى التطبيق**
- Admin Panel: http://127.0.0.1:8000/admin/
- Staff Dashboard: http://127.0.0.1:8000/
- Public Order Page: http://127.0.0.1:8000/order/

## 📱 Pages / الصفحات

- **Home** - `/` - لوحة التحكم الرئيسية
- **Products** - `/products/` - قائمة المنتجات وإدارتها
- **New Sale** - `/sale/` - إضافة مبيعات جديدة
- **Orders** - `/orders/` - قائمة الطلبات
- **Sales Report** - `/report/` - تقارير المبيعات
- **Public Order** - `/order/` - صفحة الطلبات العامة

## 🔧 Configuration / الإعدادات

### Logo Setup / إعداد الشعار
1. Save your logo image as `logo.png`
2. Place it in: `Siliana/static/images/logo.png`
3. The logo will automatically appear on all pages

For detailed instructions, see `LOGO_SETUP_INSTRUCTIONS.md`

### Daily Email Reports / تقارير البريد الإلكتروني اليومية
For setting up automatic daily email reports, see `DAILY_EMAIL_SETUP_INSTRUCTIONS.md`

## 🎨 Branding / العلامة التجارية

- **Farm Name:** مزرعة نوادر التين
- **Phone:** ☎ 20.707.272
- **Colors:** Purple gradient (#667eea to #764ba2)

## 📊 Features Details / تفاصيل المميزات

### Order Management / إدارة الطلبات
- ✅ Filter by status (pending, confirmed, completed, cancelled)
- ✅ Filter by wilaya (province)
- ✅ Select all/individual orders
- ✅ Export selected orders to Excel
- ✅ Automatic stock deduction on order placement
- ✅ Stock restoration on order cancellation

### Stock Management / إدارة المخزون
- ✅ Real-time stock updates
- ✅ Automatic stock deduction on sales
- ✅ Low stock alerts
- ✅ Stock addition tracking

## 🛠 Management Commands / أوامر الإدارة

```bash
# Setup initial data
python manage.py setup_data

# Reset admin password
python manage.py reset_admin_password

# Send daily product list email
python manage.py send_daily_product_list
```

## 📦 Project Structure / هيكل المشروع

```
Point_De_Vente/
├── Point_De_Vente/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Siliana/                 # Main app
│   ├── models.py           # Database models
│   ├── views.py            # Views
│   ├── urls.py             # URL routing
│   ├── admin.py            # Admin configuration
│   ├── templates/          # HTML templates
│   ├── static/             # Static files (CSS, JS, images)
│   └── management/         # Custom commands
├── manage.py               # Django management script
└── db.sqlite3             # Database file
```

## 🔐 Security Notes / ملاحظات الأمان

⚠️ **Important:**
- Change `SECRET_KEY` in `settings.py` before deployment
- Set `DEBUG = False` in production
- Configure proper `ALLOWED_HOSTS`
- Use environment variables for sensitive data
- Never commit `db.sqlite3` to version control

## 🤝 Contributing / المساهمة

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License / الترخيص

This project is private and proprietary to مزرعة نوادر التين.

## 📞 Contact / التواصل

- **Phone:** 20.707.272
- **Project:** مزرعة نوادر التين Point of Sale System

---

Made with ❤️ for مزرعة نوادر التين
