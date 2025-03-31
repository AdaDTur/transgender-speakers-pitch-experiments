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
