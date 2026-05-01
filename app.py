import os
from flask import Flask, render_template

# إعداد التطبيق ليعمل في المجلد الرئيسي مباشرة بدون الحاجة لمجلد templates
app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

# مسار إضافي للتعامل مع أي طلبات فرعية وتوجيهها للرئيسية
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')

if __name__ == '__main__':
    # الحصول على المنفذ من البيئة (مهم جداً لـ Render) أو استخدام 3000 افتراضياً
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port)