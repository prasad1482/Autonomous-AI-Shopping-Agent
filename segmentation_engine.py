import pandas as pd
import datetime as dt
import plotly.express as px

def create_rfm_table(df):
    print("Step 2: Generating RFM Segments...")
    snapshot_date = df['InvoiceDate'].max() + dt.timedelta(days=1)
    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
        'InvoiceNo': 'nunique',
        'TotalSum': 'sum'
    }).rename(columns={'InvoiceDate': 'Recency', 'InvoiceNo': 'Frequency', 'TotalSum': 'Monetary'})
    
    # Thresholds for tiers
    monetary_threshold = rfm['Monetary'].quantile(0.75)
    
    # Save the leak report
    at_risk = rfm[(rfm['Monetary'] >= monetary_threshold) & (rfm['Recency'] > 90)]
    at_risk.to_csv('at_risk_whales.csv')
    
    return rfm

def visualize_segments(rfm):
    print("Generating Treemap Visualization...")
    # Add simple tier logic for the chart
    rfm['Tier'] = 'Average'
    rfm.loc[(rfm['Recency'] <= 30) & (rfm['Frequency'] >= 5), 'Tier'] = 'Champion'
    rfm.loc[(rfm['Recency'] > 90), 'Tier'] = 'At-Risk'
    
    fig = px.treemap(rfm, path=['Tier'], values='Monetary', color='Recency',
                     color_continuous_scale='RdYlGn_r',
                     title='Customer Base Segmentation')
    fig.write_html("customer_segmentation_chart.html")
    fig.show()