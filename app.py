import os
from flask import Flask, render_template, jsonify

# تهيئة التطبيق: قمنا بتحديد '.' كمجلد للقوالب لقراءة index.html من الجذر مباشرة
app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    """المسار الرئيسي الذي يعرض واجهة المتجر"""
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    """مسار للتحقق من أن التطبيق يعمل بشكل سليم"""
    return jsonify({"status": "online", "message": "Store is running"}), 200

if __name__ == '__main__':
    # الحصول على المنفذ من متغيرات البيئة (مهم جداً للتشغيل على Render)
    # إذا لم يتوفر، سيستخدم المنفذ 3000 بشكل افتراضي
    port = int(os.environ.get('PORT', 3000))
    # تشغيل التطبيق على العنوان 0.0.0.0 ليكون متاحاً للإنترنت
    app.run(host='0.0.0.0', port=port)