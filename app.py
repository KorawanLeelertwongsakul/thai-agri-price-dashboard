import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# --- ส่วนของการโหลดข้อมูล ---
# ลองใช้ encoding='tis-620' หรือ 'utf-8' ถ้าอ่านภาษาไทยไม่ออก
df = pd.read_csv('prices.csv', encoding='utf-8') 

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard ราคาสินค้าเกษตรไทย", style={'textAlign': 'center'}),
    
    html.Div([
        html.Label("เลือกรายการสินค้า:"),
        dcc.Dropdown(
            id='product-dropdown',
            options=[{'label': i, 'value': i} for i in df['ชื่อคอลัมน์สินค้า'].unique()], # เปลี่ยน 'ชื่อคอลัมน์สินค้า' ให้ตรงกับในไฟล์
            value=df['ชื่อคอลัมน์สินค้า'].unique()[0] # เลือกตัวแรกเป็นค่าเริ่มต้น
        ),
    ], style={'width': '40%', 'margin': 'auto'}),

    dcc.Graph(id='line-chart'),
    dcc.Graph(id='bar-chart'),
    dcc.Graph(id='pie-chart')
])