import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/hospital_data_cleaned.csv")

st.set_page_config(layout="wide")
st.title("Hospital Admissions Dashboard")
st.markdown("Overview of inpatient characteristics and outcomes")

# ---------------------- Key Metrics ----------------------
st.header("📊 Key Summary Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Admissions", f"{df.shape[0]:,}")
col2.metric("Average Length of Stay", f"{df['Length_of_Stay'].mean():.1f} days")
col3.metric("Top Diagnosis", df['APR_DRG_Description'].value_counts().idxmax())

# ------------------ Plot 1: Admissions by Age & Severity ------------------
st.subheader("🧓 Admissions by Age Group and Severity of Illness")
age_order = ['0 to 17', '18 to 29', '30 to 49', '50 to 69', '70 or Older']
severity_order = ['Minor', 'Moderate', 'Major', 'Extreme']

df['Age_Group'] = pd.Categorical(df['Age_Group'], categories=age_order, ordered=True)
df['APR_Severity_of_Illness_Description'] = pd.Categorical(
    df['APR_Severity_of_Illness_Description'], categories=severity_order, ordered=True
)

fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.countplot(
    data=df,
    x='Age_Group',
    hue='APR_Severity_of_Illness_Description',
    order=age_order,
    hue_order=severity_order,
    ax=ax1
)
plt.title("Admissions by Age Group and Severity")
plt.xlabel("Age Group")
plt.ylabel("Number of Admissions")
plt.legend(title="Severity", bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig1)

# ------------------ Plot 2: Top Diagnoses by Count ------------------
st.subheader("🔝 Top 10 Diagnoses by Admission Count")
top_drg = (
    df['APR_DRG_Description']
    .value_counts()
    .head(10)
    .reset_index()
    .rename(columns={'index': 'DRG_Description', 'APR_DRG_Description': 'Count'})
)
fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.barplot(data=top_drg, y='DRG_Description', x='Count', ax=ax2)
plt.title("Top 10 APR DRG Diagnoses")
plt.xlabel("Number of Admissions")
plt.ylabel("DRG Description")
st.pyplot(fig2)

# ------------------ Plot 3: Mortality Risk by Age ------------------
st.subheader("⚠️ Mortality Risk Distribution by Age Group")
mortality_order = ['Minor', 'Moderate', 'Major', 'Extreme']
mort_by_age = pd.crosstab(df['Age_Group'], df['APR_Risk_of_Mortality'], normalize='index') * 100
mort_by_age = mort_by_age[mortality_order]

fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.heatmap(mort_by_age, annot=True, fmt=".1f", cmap="Reds", ax=ax3)
plt.title("Mortality Risk (%) by Age Group")
plt.ylabel("Age Group")
plt.xlabel("Risk of Mortality")
st.pyplot(fig3)

# ------------------ Plot 4: Avg LOS by Discharge ------------------
st.subheader("🏥 Average Length of Stay by Discharge Disposition")
los_by_disp = (
    df.groupby('Patient_Disposition')['Length_of_Stay']
    .mean()
    .sort_values()
    .reset_index()
    .rename(columns={'Length_of_Stay': 'Avg_LOS'})
)

fig4, ax4 = plt.subplots(figsize=(10, 6))
palette = sns.color_palette("Blues", len(los_by_disp))
barplot = sns.barplot(
    data=los_by_disp,
    y='Patient_Disposition',
    x='Avg_LOS',
    palette=palette,
    ax=ax4
)

for i, (value, label) in enumerate(zip(los_by_disp['Avg_LOS'], los_by_disp['Patient_Disposition'])):
    ax4.text(value + 0.3, i, f"{value:.1f}", va='center')

plt.title("Average Length of Stay by Discharge Disposition")
plt.xlabel("Average LOS (Days)")
plt.ylabel("Disposition Type")
plt.xlim(0, los_by_disp['Avg_LOS'].max() + 3)
st.pyplot(fig4)

st.markdown("---")
st.markdown("📌 **Note:** Each chart corresponds directly to data patterns that help inform patient outcomes, severity profiles, and resource usage.")
