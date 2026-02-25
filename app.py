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

@app.callback(
    [Output('line-chart', 'figure'),
     Output('bar-chart', 'figure'),
     Output('pie-chart', 'figure')],
    [Input('product-dropdown', 'value')]
)
def update_graphs(selected_product):
    # กรองข้อมูลตามสินค้าที่เลือก
    filtered_df = df[df['ชื่อคอลัมน์สินค้า'] == selected_product]
    
    # กราฟที่ 1: Line Chart (แนวโน้มราคา)
    fig1 = px.line(filtered_df, x='คอลัมน์วันที่', y='คอลัมน์ราคา', title=f'แนวโน้มราคา: {selected_product}')

    # กราฟที่ 2: Bar Chart (เปรียบเทียบราคาตามแหล่งข้อมูล/จังหวัด)
    fig2 = px.bar(filtered_df, x='ชื่อจังหวัด', y='คอลัมน์ราคา', color='ชื่อจังหวัด', title='ราคาแยกตามพื้นที่')

    # กราฟที่ 3: Pie Chart (สัดส่วนข้อมูล)
    fig3 = px.pie(filtered_df, names='หน่วยนับ', title='สัดส่วนหน่วยวัดสินค้า')
    
    return fig1, fig2, fig3

if __name__ == '__main__':
    app.run_server(debug=True)