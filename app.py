import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# --- ส่วนของการโหลดข้อมูล ---
df = pd.read_csv('prices.csv', encoding='utf-8') 

# นำเข้า Google Fonts
external_stylesheets = ['https://fonts.googleapis.com/css2?family=Sarabun:wght@400;700&display=swap']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# --- ส่วนของการจัดวางหน้าจอ (Layout) ---
app.layout = html.Div([
    html.H1("Dashboard ราคาสินค้าเกษตรไทย", 
            style={
                'textAlign': 'center', 
                'color': '#1a5276', 
                'fontFamily': 'Sarabun, sans-serif',
                'paddingTop': '20px'
            }),
    
    html.Div([
        html.Label("เลือกรายการสินค้า:", style={'fontFamily': 'Sarabun', 'fontWeight': 'bold'}),
        dcc.Dropdown(
            id='product-dropdown',
            options=[{'label': i, 'value': i} for i in df['PR_PROD_NAME'].unique()],
            value=df['PR_PROD_NAME'].unique()[0],
            searchable=True,
            clearable=True,
            style={'fontFamily': 'Sarabun'}
        ),
    ], style={'width': '50%', 'margin': '20px auto'}),

    html.Div([
        dcc.Graph(id='line-chart'),
        html.Div([
            dcc.Graph(id='bar-chart', style={'display': 'inline-block', 'width': '50%'}),
            dcc.Graph(id='pie-chart', style={'display': 'inline-block', 'width': '50%'})
        ])
    ])
], style={'backgroundColor': '#f9f9f9', 'minHeight': '100vh', 'padding': '10px', 'fontFamily': 'Sarabun'})

# --- ส่วนของระบบ Interactive (Callback) ---
@app.callback(
    [Output('line-chart', 'figure'),
     Output('bar-chart', 'figure'),
     Output('pie-chart', 'figure')],
    [Input('product-dropdown', 'value')]
)
def update_graphs(selected_product):
    if not selected_product:
        return {}, {}, {}

    filtered_df = df[df['PR_PROD_NAME'] == selected_product]

    fig1 = px.line(filtered_df, x='PRICE_DATE', y='PRICE_DAY', 
                  title=f'แนวโน้มราคา: {selected_product}', 
                  markers=True, color_discrete_sequence=['blue'])
    
    fig2 = px.bar(filtered_df, x='MARKET_NAME', y='PRICE_DAY', color='MARKET_NAME',
                 title='เปรียบเทียบราคาแต่ละตลาด')

    fig3 = px.pie(filtered_df, names='MARKET_NAME', title='สัดส่วนแหล่งข้อมูล')

    for fig in [fig1, fig2, fig3]:
        fig.update_layout(font_family="Sarabun", title_font_family="Sarabun")

    return fig1, fig2, fig3

if __name__ == '__main__':
   app.run(debug=True)