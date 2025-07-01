import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1. Generate fake data
np.random.seed(0)
n = 200

# 1.1. Create a DataFrame with age, priors
data = pd.DataFrame({
    'age': np.random.randint(18, 60, size=n),
    'priors': np.random.poisson(2, size=n),
    'race': np.random.choice(['White', 'Black', 'Asian'], size=n)
})

# 2. Define biased "AI risk score"
def compute_risk(row):
    base_score = 0.3 * row['age'] + 1.5 * row['priors']
    if row['race'] == 'Black':
        base_score += 10  # Intentional bias
    elif row['race'] == 'Asian':
        base_score -= 5
    return base_score + np.random.normal(0, 5)  # noise

data['risk_score'] = data.apply(compute_risk, axis=1)

# 3. Plot risk score by race
data.groupby('race')['risk_score'].mean().plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen'])
plt.title('Average AI Risk Score by Race (Simulated Bias)')
plt.ylabel('Risk Score')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()