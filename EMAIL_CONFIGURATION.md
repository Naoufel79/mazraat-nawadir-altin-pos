# Email Configuration for Order Confirmations
# تكوين البريد الإلكتروني لتأكيدات الطلبات

## Overview / نظرة عامة

The system now sends email confirmations to customers when they place orders through the public order page (http://127.0.0.1:8000/order/).

يرسل النظام الآن رسائل تأكيد بالبريد الإلكتروني للعملاء عند تقديم طلباتهم عبر صفحة الطلبات العامة.

## What's Included in the Email / ما يتضمنه البريد الإلكتروني

The confirmation email includes:
- Order number / رقم الطلب
- Order date and time / تاريخ ووقت الطلب
- Customer information / معلومات العميل
- Delivery address / عنوان التوصيل
- List of ordered products with quantities and prices / قائمة المنتجات المطلوبة مع الكميات والأسعار
- Total amount / المبلغ الإجمالي
- Contact phone number / رقم الهاتف للتواصل

## Configuration Steps / خطوات التكوين

### Option 1: Gmail Configuration (Recommended for Testing)

Add the following to your `settings.py`:

```python
# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'  # Use App Password, not regular password
DEFAULT_FROM_EMAIL = 'مزرعة نوادر التين <your-email@gmail.com>'
```

**Important for Gmail:**
1. Enable 2-Factor Authentication on your Google account
2. Generate an App Password:
   - Go to: https://myaccount.google.com/apppasswords
   - Create app password for "Mail"
   - Use this password in EMAIL_HOST_PASSWORD

### Option 2: Development/Testing (Console Backend)

For testing without actual email sending:

```python
# Email Configuration - Console (for development)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'مزرعة نوادر التين <noreply@mazraat-nawadir.tn>'
```

This will print emails to the console instead of sending them.

### Option 3: File Backend (Save to Files)

For testing by saving emails to files:

```python
# Email Configuration - File (for development)
EMAIL_BACKEND = 'django.core.mail.backends.filebacked.EmailBackend'
EMAIL_FILE_PATH = 'tmp/app-emails'  # emails will be saved here
DEFAULT_FROM_EMAIL = 'مزرعة نوادر التين <noreply@mazraat-nawadir.tn>'
```

### Option 4: Production SMTP Server

For production with a custom SMTP server:

```python
# Email Configuration - Production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.your-domain.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'noreply@your-domain.com'
EMAIL_HOST_PASSWORD = 'your-smtp-password'
DEFAULT_FROM_EMAIL = 'مزرعة نوادر التين <noreply@your-domain.com>'
```

## Security Best Practices / أفضل ممارسات الأمان

### Use Environment Variables

Instead of hardcoding credentials, use environment variables:

1. Install `python-decouple`:
```bash
pip install python-decouple
```

2. Create a `.env` file in your project root:
```
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

3. Update `settings.py`:
```python
from decouple import config

EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
```

4. Add `.env` to `.gitignore` (already done)

## Testing the Email Feature / اختبار ميزة البريد الإلكتروني

1. Configure email settings in `settings.py`
2. Run the development server:
   ```bash
   python manage.py runserver
   ```
3. Go to: http://127.0.0.1:8000/order/
4. Fill in the order form including an email address
5. Submit the order
6. Check:
   - Console (if using console backend)
   - Email inbox (if using SMTP)
   - File directory (if using file backend)

## Troubleshooting / استكشاف الأخطاء

### Email not sending

1. **Check settings.py** - Verify email configuration
2. **Check firewall** - Ensure port 587/465 is not blocked
3. **Check credentials** - Verify email and password are correct
4. **Check logs** - Look at terminal output for error messages
5. **Try console backend** - Test if code is working by using console backend

### Gmail specific issues

- **"Username and Password not accepted"**: Use App Password instead of regular password
- **"Less secure apps"**: This is deprecated, use App Passwords
- **"SMTP Authentication Error"**: Enable 2FA and generate App Password

## Current Implementation Details / تفاصيل التنفيذ الحالي

### Email Field
- The email field is **optional** in the order form
- Customers can place orders without providing an email
- If email is provided, a confirmation is sent automatically

### Email Content
- Written in Arabic / مكتوب بالعربية
- Professional format
- Includes all order details
- Uses Unicode characters (emojis) for visual appeal

### Error Handling
- Email sending uses `fail_silently=True`
- Order is created even if email fails
- Email errors don't prevent order completion
- Errors are logged to console

## Email Template Customization / تخصيص قالب البريد

To customize the email template, edit the `public_order` function in `views.py`:

```python
subject = f'تأكيد طلبك رقم #{order.id} - مزرعة نوادر التين'
message = '''
Your custom email content here
'''
```

## Production Recommendations / توصيات الإنتاج

For production deployment:

1. **Use a dedicated email service**:
   - SendGrid
   - Amazon SES
   - Mailgun
   - Postmark

2. **Implement HTML emails**:
   - Use Django's `EmailMultiAlternatives`
   - Create HTML templates
   - Add styling and branding

3. **Add email queue**:
   - Use Celery for async email sending
   - Prevent delays in order processing

4. **Monitor email delivery**:
   - Track delivery rates
   - Handle bounce backs
   - Log failed emails

5. **Comply with regulations**:
   - Add unsubscribe option
   - Include physical address
   - Follow GDPR if applicable

## Additional Features to Consider / ميزات إضافية للنظر فيها

- ✅ Order confirmation email (implemented)
- ⏳ Status update emails (when order is confirmed/completed)
- ⏳ Admin notification emails (when new order is received)
- ⏳ Password reset emails
- ⏳ Newsletter/promotional emails
- ⏳ HTML email templates with branding
- ⏳ Email with PDF invoice attachment

---

## Quick Setup for Testing / إعداد سريع للاختبار

**Fastest way to test (Console Backend):**

Add to `Point_De_Vente/settings.py`:

```python
# At the end of the file
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'مزرعة نوادر التين <noreply@example.com>'
```

This will print emails to your terminal/console when orders are placed!

---

**Contact:** ☎ 20.707.272
**Project:** مزرعة نوادر التين Point of Sale System
