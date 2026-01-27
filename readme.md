# Project Title: Autonomous Customer Retention Engine (RFM Segmentation & Predictive Analytics)

## Project Status: Completed & Production-Ready

This project shows an analytics solution for e-commerce businesses. It shifts from reactive reporting to proactive, data-driven customer retention strategies.

It uses the **Recency, Frequency, and Monetary (RFM)** model. It also uses data engineering to find high-value customer segments, pinpoint "revenue leaks," and maximize profit margins.

---

## 🚀 Business Value & Key Deliverables

This provides insights that translate directly into ROI:

### 1. The "Revenue Leak" Report

*   **Insight:** Identifies high-value customers who are close to churning.
*   **Result:** A list of **95 high-value customers** identified as being "At-Risk," representing a potential recovery of over **$434,984.93** in revenue if targeted with win-back campaigns immediately.

### 2. The "Margin Protection" Report

*   **Insight:** Identifies "Champion" customers who should never receive discounts.
*   **Result:** Identification of **623 loyal customers** generating over **$4.6 Million** in revenue. A strategy is implemented to move these customers to a "VIP/Early Access" track instead of general discount campaigns, protecting profit margins.

### 3. Visual Customer Health Dashboard

*   **Insight:** A visualization showing the distribution of customer value across the entire business landscape.
*   **Result:** An interactive Treemap that visually breaks down customer tiers (Champions, At-Risk Whales, Hibernating, Average) to guide marketing spend decisions.

---

## ⚙️ Technical Approach & Methodology

The project uses a phased methodology:

### Phase 1: Data Engineering & Cleaning Pipeline

A Python script handles data from the raw Kaggle dataset. It removes missing Customer IDs, cancelled orders (Invoice numbers starting with 'C'), and non-positive transactional values. The output is a clean, feature-engineered dataframe ready for modeling.

### Phase 2: Feature Engineering (RFM Metrics)

Transaction logs were aggregated at the `CustomerID` level to calculate three core metrics:

*   **Recency:** Days since the last purchase.
*   **Frequency:** Total number of unique orders.
*   **Monetary:** Total amount spent by the customer.

### Phase 3: Segmentation & Analysis

A thresholding approach was used to categorize customers into tiers (`Champion`, `At-Risk Whale`, `Hibernating`, `Average`). This provides actionable data for marketing teams.

---

## 🛠️ Tech Stack & Libraries

*   **Language:** Python
*   **Libraries:** `pandas`, `numpy`, `datetime`, `plotly` (for visualization), `scikit-learn` (for potential future K-Means clustering expansion)
*   **Environment:** VS Code
*   **Version Control:** Git/GitHub

---

## 📊 Visualizations

*(**Instructions:** Add your generated Treemap image file (e.g., as a PNG) to your GitHub repository and link it here.)*

![Customer Segmentation Treemap](link-to-your-treemap-image.png)

---

## 🎯 Next Steps & Future Expansion

*   **Integration with AI Agents:** Integrate the `at_risk_whales` list with an LLM API (e.g., OpenAI, Gemini) to automatically generate personalized win-back email/SMS copy in real-time.
*   **Predictive Modeling:** Implement an XGBoost or Random Forest model to predict the *probability* of churn for the next 30 days, rather than relying on a static "90-day" threshold.

---

## Author

[Duggirala jnana satya prasad/[LinkedIn Profile Link](http://linkedin.com/in/prasad-duggirala/)]