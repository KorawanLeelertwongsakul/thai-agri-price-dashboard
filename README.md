Thailand Agricultural Price Dashboard
Dashboard สำหรับวิเคราะห์ราคาสินค้าเกษตรรายวันในประเทศไทย เพื่อทดสอบความเข้าใจในการสร้าง Interactive Data Visualization และการจัดการเวอร์ชันด้วย Git ตามหลัก Commit Early, Commit Often

ข้อมูลที่ใช้ (Data Source)
ที่มา: data.go.th (ราคาสินค้าเกษตรรายวัน)

คอลัมน์สำคัญ:

PRICE_DATE: วันที่บันทึกราคา

PR_PROD_NAME: ชื่อสินค้าเกษตร

MARKET_NAME: ชื่อตลาดหรือแหล่งข้อมูล

PRICE_DAY: ราคาขายปลีก/ส่งในวันนั้น

วิธีการติดตั้งและรันโปรแกรม (How to Run)

1. Clone Repository :
git clone https://github.com/KorawanLeelertwongsakul/thai-agri-price-dashboard.git

2. สร้าง Virtual Environment :
python -m venv venv
.\venv\Scripts\activate  # สำหรับ Windows

3. ติดตั้ง Library ที่จำเป็น :
pip install -r requirements.txt

4. รันโปรแกรม :
python app.py

5. เข้าชม Dashboard : เปิด Browser ไปที่ http://127.0.0.1:8050