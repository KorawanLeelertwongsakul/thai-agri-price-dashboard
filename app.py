import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# --- ส่วนของการโหลดข้อมูล ---
# มั่นใจว่าไฟล์ชื่อ prices.csv และมีคอลัมน์ PR_PROD_NAME, PRICE_DATE, PRICE_DAY, MARKET_NAME
df = pd.read_csv('prices.csv', encoding='utf-8') 
app = dash.Dash(__name__)

# --- ส่วนของการจัดวางหน้าจอ (Layout) ---
app.layout = html.Div([ # [จุดแก้ไข Commit 14: ใส่พื้นหลังและระยะห่าง]
    
    # [จุดแก้ไข Commit 13 & 16: เปลี่ยนสีและฟอนต์หัวข้อ]
    html.H1("Dashboard ราคาสินค้าเกษตรไทย", 
            style={
                'textAlign': 'center', 
                'color': '#1a5276', 
                'fontFamily': 'Arial, sans-serif',
                'paddingTop': '20px'
            }),
    
    html.Div([
        html.Label("เลือกรายการสินค้า:", style={'fontFamily': 'Arial'}),
        dcc.Dropdown(
            id='product-dropdown',
            options=[{'label': i, 'value': i} for i in df['PR_PROD_NAME'].unique()],
            value=df['PR_PROD_NAME'].unique()[0],
            style={'fontFamily': 'Arial'}
        ),
    ], style={'width': '50%', 'margin': '20px auto'}),

    html.Div([
        dcc.Graph(id='line-chart'),
        html.Div([
            dcc.Graph(id='bar-chart', style={'display': 'inline-block', 'width': '50%'}),
            dcc.Graph(id='pie-chart', style={'display': 'inline-block', 'width': '50%'})
        ])
    ])
], style={'backgroundColor': '#f9f9f9', 'minHeight': '100vh', 'padding': '10px'}) # พื้นหลังสีเทาอ่อนแบบเต็มหน้าจอ

# --- ส่วนของระบบ Interactive (Callback) ---
@app.callback(
    [Output('line-chart', 'figure'),
     Output('bar-chart', 'figure'),
     Output('pie-chart', 'figure')],
    [Input('product-dropdown', 'value')]
)
def update_graphs(selected_product):
    # กรองข้อมูลตามสินค้าที่เลือก
    filtered_df = df[df['PR_PROD_NAME'] == selected_product]

    # กราฟที่ 1: Line Chart 
    fig1 = px.line(filtered_df, x='PRICE_DATE', y='PRICE_DAY', 
                  title=f'แนวโน้มราคา: {selected_product}', 
                  markers=True, 
                  color_discrete_sequence=['blue'])
    
    # ปรับแต่งฟอนต์ในกราฟ
    fig1.update_layout(font_family="Arial")

    # กราฟที่ 2: Bar Chart
    fig2 = px.bar(filtered_df, x='MARKET_NAME', y='PRICE_DAY', color='MARKET_NAME',
                 title='เปรียบเทียบราคาแต่ละตลาด')
    fig2.update_layout(font_family="Arial")

    # กราฟที่ 3: Pie Chart
    fig3 = px.pie(filtered_df, names='MARKET_NAME', title='สัดส่วนแหล่งข้อมูล')
    fig3.update_layout(font_family="Arial")

    return fig1, fig2, fig3

if __name__ == '__main__':
   app.run(debug=True)