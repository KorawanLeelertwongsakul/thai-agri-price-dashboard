import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# --- ส่วนของการโหลดข้อมูล ---
df = pd.read_csv('prices.csv', encoding='utf-8') 
sapp = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard ราคาสินค้าเกษตรไทย", style={'textAlign': 'center', 'color': '#2c3e50'}),
    
    html.Div([
        html.Label("เลือกรายการสินค้า:"),
        dcc.Dropdown(
            id='product-dropdown',
            options=[{'label': i, 'value': i} for i in df['PR_PROD_NAME'].unique()],
            value=df['PR_PROD_NAME'].unique()[0] 
        ),
    ], style={'width': '50%', 'margin': '20px auto'}),

    html.Div([
        dcc.Graph(id='line-chart'),
        html.Div([
            dcc.Graph(id='bar-chart', style={'display': 'inline-block', 'width': '50%'}),
            dcc.Graph(id='pie-chart', style={'display': 'inline-block', 'width': '50%'})
        ])
    ])
])

@app.callback(
    [Output('line-chart', 'figure'),
     Output('bar-chart', 'figure'),
     Output('pie-chart', 'figure')],
    [Input('product-dropdown', 'value')]
)
def update_graphs(selected_product):
    filtered_df = df[df['PR_PROD_NAME'] == selected_product]

    # กราฟที่ 1: Line Chart แนวโน้มราคาตามวันที่
    fig1 = px.line(filtered_df, x='PRICE_DATE', y='PRICE_DAY', 
                  title=f'แนวโน้มราคา: {selected_product}', markers=True)

    # กราฟที่ 2: Bar Chart ราคาแยกตามตลาด
    fig2 = px.bar(filtered_df, x='MARKET_NAME', y='PRICE_DAY', color='MARKET_NAME',
                 title='เปรียบเทียบราคาแต่ละตลาด')

    # กราฟที่ 3: Pie Chart สัดส่วนการบันทึกข้อมูลแต่ละตลาด
    fig3 = px.pie(filtered_df, names='MARKET_NAME', title='สัดส่วนแหล่งข้อมูล')

    return fig1, fig2, fig3

if __name__ == '__main__':
   app.run(debug=True)