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

อธิบายการทำงานของโค้ด (Code Explanation)
Data Loading: ใช้ pandas ในการอ่านไฟล์ CSV และจัดการเรื่อง Encoding (TIS-620 หรือ UTF-8) เพื่อให้แสดงผลภาษาไทยได้อย่างถูกต้อง

Layout Design: ออกแบบด้วย Dash HTML Components และ Dash Core Components โดยเน้นความสะอาดตา ใช้ฟอนต์ Sarabun เพื่อความสวยงามและอ่านง่าย

Interactivity (Callback):

ใช้ระบบ Reactive Programming ของ Dash โดยเมื่อผู้ใช้เลือกสินค้าจาก Dropdown ระบบจะส่งค่านั้นไปกรองข้อมูลใน DataFrame

ข้อมูลที่ถูกกรองจะถูกส่งไปยังฟังก์ชันสร้างกราฟ 3 ตัว เพื่ออัปเดตผลลัพธ์พร้อมกันโดยไม่ต้อง Refresh หน้าเว็บ

Visualizations:

Line Chart: แสดงแนวโน้มราคาตามกาลเวลา

Bar Chart: เปรียบเทียบราคาในแต่ละตลาดแหล่งข้อมูล

Pie Chart: แสดงสัดส่วนปริมาณข้อมูลในแต่ละตลาด