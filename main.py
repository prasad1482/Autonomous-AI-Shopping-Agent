from data_pipeline import load_and_clean_data
from segmentation_engine import create_rfm_table, visualize_segments # Added visualize
from predictive_model import train_churn_model

def run_project():
    raw_df = load_and_clean_data('C:\machihe learning\Projects\AI shoping agent\dataset\Online_Retail.csv')
    rfm_table = create_rfm_table(raw_df)
    
    # NEW: Run the visualization
    visualize_segments(rfm_table)
    
    final_rfm, model = train_churn_model(rfm_table)
    print("\n--- FINAL SYSTEM STATUS ---")
    print(final_rfm.head())

if __name__ == "__main__":
    run_project()