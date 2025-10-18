# تعليمات إضافة شعار مزرعة نوادر التين

## Logo Setup Instructions

تم إعداد الموقع لعرض شعار "مزرعة نوادر التين" مع رقم الهاتف 20.707.272

### خطوات إضافة الشعار:

1. **احفظ صورة الشعار**
   - احفظ صورة الشعار التي أرسلتها باسم `logo.png`
   - يفضل أن تكون الصورة بحجم مربع (مثلاً 300×300 بيكسل)

2. **ضع الصورة في المجلد الصحيح**
   - انسخ ملف `logo.png` إلى المسار التالي:
   ```
   Point_De_Vente/Siliana/static/images/logo.png
   ```

3. **تحديث الإعدادات (إن لزم الأمر)**
   - تأكد من وجود إعداد STATIC في ملف `settings.py`
   - الإعداد الافتراضي يجب أن يكون موجوداً بالفعل

4. **تجميع الملفات الثابتة (للإنتاج فقط)**
   ```bash
   python manage.py collectstatic
   ```

### ملاحظات مهمة:

- ✅ تم تحديث ملف `base.html` لعرض الشعار في جميع الصفحات الداخلية
- ✅ تم تحديث ملف `public_order.html` لعرض الشعار في صفحة الطلبات العامة
- ✅ الشعار سيظهر بشكل دائري مع إطار أبيض
- ✅ رقم الهاتف 20.707.272 سيظهر تحت اسم المزرعة
- ✅ اسم المزرعة "مزرعة نوادر التين" سيظهر بدلاً من "نقطة البيع"

### مكان عرض الشعار:

1. **الصفحات الداخلية** (للمستخدمين المسجلين):
   - الصفحة الرئيسية
   - قائمة المنتجات
   - المبيعات
   - الطلبات
   - التقارير

2. **الصفحات العامة**:
   - صفحة طلب المنتجات العامة (http://127.0.0.1:8000/order/)

### تخصيص الشعار (اختياري):

إذا أردت تغيير حجم أو نمط الشعار، يمكنك تعديل CSS في الملفات:
- `base.html` (السطر الخاص بـ `.logo`)
- `public_order.html` (السطر الخاص بـ `.logo`)

الإعدادات الحالية:
```css
.logo {
    width: 100px;  /* للصفحات الداخلية */
    width: 120px;  /* للصفحة العامة */
    height: 100px; /* أو 120px */
    border-radius: 50%; /* شكل دائري */
    border: 3px solid white; /* أو 4px */
}
```

---

## English Instructions

The website has been prepared to display the "مزرعة نوادر التين" logo with phone number 20.707.272

### Steps to add the logo:

1. **Save the logo image**
   - Save your logo image as `logo.png`
   - Square dimensions recommended (e.g., 300×300 pixels)

2. **Place the image in the correct folder**
   - Copy `logo.png` to this path:
   ```
   Point_De_Vente/Siliana/static/images/logo.png
   ```

3. **The logo will automatically appear on all pages**

### What has been updated:

- ✅ `base.html` - Shows logo on all internal pages
- ✅ `public_order.html` - Shows logo on public order page
- ✅ Logo displays as a circle with white border
- ✅ Phone number 20.707.272 displays below farm name
- ✅ Farm name "مزرعة نوادر التين" replaces generic "نقطة البيع"
