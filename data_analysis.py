import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cleaned.csv')

df = df.rename(columns={
    'Ident (0 = TM, 1 =TF)': 'Ident',
    'Time on HRT (months)': 'HRT_Months',
    'Time out (months)': 'Out_Months',
    'Coefficient of Variation': 'CV',
    'Pitch Range (Hz)': 'Pitch_Range',
})

df_tm = df[df['Ident'] == 0]
df_tf = df[df['Ident'] == 1]

### months on hrt by pitch range
# transmascs
plt.figure(figsize=(7, 5))
plt.scatter(df_tm['HRT_Months'], df_tm['Pitch_Range'], label='TM', alpha=0.7)
plt.title('Pitch Range vs Months on HRT')
plt.xlabel('Months on HRT')
plt.ylabel('Pitch Range (Hz)')
plt.legend()
plt.show()

# transfems
plt.figure(figsize=(7, 5))
plt.scatter(df_tf['HRT_Months'], df_tf['Pitch_Range'], label='TF', alpha=0.7)
plt.title('Pitch Range vs Months on HRT')
plt.xlabel('Months on HRT')
plt.ylabel('Pitch Range (Hz)')
plt.legend()
plt.show()

### months out socially by pitch range
# transmascs
plt.figure(figsize=(7, 5))
plt.scatter(df_tm['Out_Months'], df_tm['Pitch_Range'], label='TM', alpha=0.7)
plt.title('Pitch Range vs Months Out')
plt.xlabel('Months Out')
plt.ylabel('Pitch Range (Hz)')
plt.legend()
plt.show()

# transfems
plt.figure(figsize=(7, 5))
plt.scatter(df_tf['Out_Months'], df_tf['Pitch_Range'], label='TF', alpha=0.7)
plt.title('Pitch Range vs Months Out')
plt.xlabel('Months Out')
plt.ylabel('Pitch Range (Hz)')
plt.legend()
plt.show()

### months on hrt by coefficient of variation
# transmascs
plt.figure(figsize=(7, 5))
plt.scatter(df_tm['HRT_Months'], df_tm['CV'], label='TM', alpha=0.7)
plt.title('Coefficient of Variation vs Months on HRT')
plt.xlabel('Months on HRT')
plt.ylabel('Coefficient of Variation')
plt.legend()
plt.show()

# transfems
plt.figure(figsize=(7, 5))
plt.scatter(df_tf['HRT_Months'], df_tf['CV'], label='TF', alpha=0.7)
plt.title('Coefficient of Variation vs Months on HRT')
plt.xlabel('Months on HRT')
plt.ylabel('Coefficient of Variation')
plt.legend()
plt.show()

### months out socially by coefficient of variation
# transmascs
plt.figure(figsize=(7, 5))
plt.scatter(df_tm['Out_Months'], df_tm['CV'], label='TM', alpha=0.7)
plt.title('Coefficient of Variation vs Months Out')
plt.xlabel('Months Out')
plt.ylabel('Coefficient of Variation')
plt.legend()
plt.show()

# transfems
plt.figure(figsize=(7, 5))
plt.scatter(df_tf['Out_Months'], df_tf['CV'], label='TF', alpha=0.7)
plt.title('Coefficient of Variation vs Months Out')
plt.xlabel('Months Out')
plt.ylabel('Coefficient of Variation')
plt.legend()
plt.show()

pitch_vars = ["Pitch_Range", "Pitch_Std_Dev", "CV"]
time_vars = ["Out_Months", "HRT_Months"]

correlation_results = []
for pitch_var in pitch_vars:
    for time_var in time_vars:
        valid_data = df_tm[[pitch_var, time_var]].replace([np.inf, -np.inf], np.nan).dropna() 
        r, p = pearsonr(valid_data[pitch_var], valid_data[time_var])
        correlation_results.append({
            "Pitch Feature": pitch_var,
            "Time Variable": time_var,
            "Pearson r": r,
            "p-value": p
        })

correlation_df = pd.DataFrame(correlation_results)
pivot_table = correlation_df.pivot(index="Pitch Feature", columns="Time Variable", values="Pearson r")
plt.figure(figsize=(8, 6))
sns.heatmap(pivot_table, annot=True, cmap="coolwarm", center=0, fmt=".2f")
plt.title("Pearson Correlation Between Pitch Features and Time Variables for TM")
plt.tight_layout()
plt.savefig('correlation_tm.jpg')
