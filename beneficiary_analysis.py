import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('C:/Users/karnv/OneDrive/Desktop/code/Project/py/py/Dataset.csv')
print(data.head())
print(data.info())
print(data.describe())
print(data.isnull().sum())

# 1.Find the total number of beneficiaries state-wise.
data['state_name'] = data['state_name'].replace(
    'THE DADRA AND NAGAR HAVELI AND DAMAN AND DIU',
    'DNH & DIU'
)
statewise_benf = data.groupby('state_name')['total_beneficiaries'].sum()
statewise_benf = statewise_benf.sort_values(ascending=False)
print(statewise_benf)
plt.figure(figsize=(9, 6) , dpi=120)
statewise_benf.plot(kind='barh', color='darkgoldenrod')
plt.xticks(
    ticks=[0, 20000000, 40000000, 60000000, 80000000, 100000000, 120000000, 140000000],
    labels=['0', '2 Cr', '4 Cr', '6 Cr', '8 Cr', '10 Cr', '12 Cr', '14 Cr']
)
plt.title('Total Beneficiaries by State')
plt.xlabel('Total Beneficiaries')
plt.ylabel('State')
plt.tight_layout()
plt.show()

# 2.Identify top 5 districts with the highest and lowest number of beneficiaries.
districtwise_benf = (
    data.groupby(
        ['state_name','district_name'],
        as_index=False
    )['total_beneficiaries'].sum()
)
top_5_districts = districtwise_benf.sort_values('total_beneficiaries', ascending=False).head()
print("Top 5 districts according to total beneficiaries:")
print(top_5_districts)

# Plotting top 5 Districts
plt.figure(figsize=(7, 3.5),dpi=120)
top_5_districts.plot(kind='bar', color='darkorange')
plt.title('Top 5 Districts by Total Beneficiaries')
plt.xticks(
    ticks=range(len(top_5_districts)), 
    labels=top_5_districts['district_name'],
    rotation=0
)
plt.yticks(
    ticks=[0, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000],
    labels=['0', '10 Lakh', '20 Lakh', '30 Lakh', '40 Lakh', '50 Lakh', '60 Lakh']
)

plt.xlabel('District Name')
plt.ylabel('Total Beneficiaries')
plt.tight_layout()
plt.legend().remove()
plt.show()

lowest_5_districts = districtwise_benf.sort_values('total_beneficiaries',ascending=True).head()
lowest_5_districts = lowest_5_districts.sort_values('total_beneficiaries',ascending=False)
print("\nLowest 5 districts according to total beneficiaries:")
print(lowest_5_districts)

# Plotting Lowest 5 Districts
plt.figure(figsize=(10, 3.5), dpi=300)
lowest_5_districts.plot(kind='barh', color='salmon')
plt.title('Lowest 5 Districts by Total Beneficiaries')
plt.yticks(
    ticks=range(len(lowest_5_districts)), 
    labels=lowest_5_districts['district_name'],
    rotation=0
)

plt.ylabel('District Name')
plt.xlabel('Total Beneficiaries')
plt.tight_layout()
plt.legend().remove()
plt.show()

# 3.Check the correlation between Aadhaar availability and total beneficiaries.
correlation = data['total_beneficiaries'].corr(data['total_aadhar'])
print("Correlation between Aadhaar availability and total beneficiaries:", correlation)
plt.figure(figsize=(7,4), dpi=150)
sns.scatterplot(data=data, x='total_beneficiaries', y='total_aadhar')
plt.title('Aadhaar vs Total Beneficiaries')
plt.xlabel('Total Beneficiaries')
plt.ylabel('Aadhaar Available')
plt.show()

# 4.Compare the number of SC, ST, OBC, and GEN beneficiaries.
data['demographic_sum'] = (
    data['total_sc'] +
    data['total_st'] +
    data['total_gen'] +
    data['total_obc']
)
mismatch = data[data['demographic_sum'] != data['total_beneficiaries']]
print(f"Rows where SC+ST+GEN+OBC ≠ total: {len(mismatch)}")

# 1.2 Aadhaar > total_beneficiaries
bad_aad = data[data['total_aadhar'] > data['total_beneficiaries']]
print(f"Rows where Aadhaar > total: {len(bad_aad)}")
data = data.drop(bad_aad.index)

# 1.3 Mobile > total_beneficiaries
bad_mob = data[data['total_mobileno'] > data['total_beneficiaries']]
print(f"Rows where Mobile > total: {len(bad_mob)}")
data = data.drop(bad_mob.index)

total_by_caste = data[['total_sc', 'total_st', 'total_obc', 'total_gen']].sum()
print("Before droping the data: ")
total_by_caste = total_by_caste.sort_values(ascending=True)
print(total_by_caste)
data1 = data.copy()
data1 = data.drop(mismatch.index)
total_by_caste = data1[['total_sc', 'total_st', 'total_obc', 'total_gen']].sum()
print("After droping the data:")
print(total_by_caste)

# Plotting the summed values
categories = ['SC', 'ST', 'OBC', 'GEN']
plt.figure(figsize=(1,1),dpi=150)
total_by_caste.plot(kind='bar',  color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], figsize=(8, 6))
plt.title("Total Beneficiaries by Caste Category")
plt.xlabel("Caste Category")
plt.ylabel("Number of Beneficiaries")
plt.yticks(
    ticks=[0, 30_000_000, 60_000_000, 90_000_000, 120_000_000, 150_000_000],
    labels=['0', '3 Cr', '6 Cr', '9 Cr', '12 Cr', '15 Cr']
)
plt.xticks(
    rotation = 0,
    ticks=range(len(categories)),
    labels=categories
)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 5.Calculate the percentage of beneficiaries with Aadhaar and Mobile numbers.
total_beneficiaries = data['total_beneficiaries'].sum()
total_aadhar = data['total_aadhar'].sum()
total_mobile = data['total_mobileno'].sum()
aadhar_percentage = (total_aadhar / total_beneficiaries) * 100
mobile_percentage = (total_mobile / total_beneficiaries) * 100
print(f"Percentage of beneficiaries with Aadhaar: {aadhar_percentage:.2f}%")
print(f"Percentage of beneficiaries with Mobile Number: {mobile_percentage:.2f}%")
labels = ['With Aadhaar', 'Without Aadhaar']
sizes = [total_aadhar, total_beneficiaries - total_aadhar]
colors = ['#66b3ff', '#ff9999']
plt.figure(figsize=(4,4))
plt.pie(sizes, labels=labels, autopct='%.1f%%', startangle=40, colors=colors)
plt.title('Aadhaar Availability Among Beneficiaries')
plt.axis('equal')
plt.show()

# Pie chart for Mobile Number availability
labels = ['With Mobile Number', 'Without Mobile Number']
sizes = [total_mobile, total_beneficiaries - total_mobile]
colors = ['#99ff99', '#ffcc99']
plt.figure(figsize=(4, 4))
plt.pie(sizes, labels=labels, autopct='%.1f%%', startangle=40, colors=colors)
plt.title('Mobile Number Availability Among Beneficiaries')
plt.axis('equal')
plt.show()

both_present = data[(data['total_aadhar'] > 0) & (data['total_mobileno'] > 0)]
both_total = both_present['total_beneficiaries'].sum()
total_beneficiaries = data['total_beneficiaries'].sum()
both_percentage = (both_total / total_beneficiaries) * 100
print(f"Percentage of beneficiaries with both Aadhaar and Mobile: {both_percentage:.2f}%")
labels = ['With Both Aadhaar & Mobile', 'Missing Either or Both']
sizes = [both_total, total_beneficiaries - both_total]
colors = ['#8fd9b6', '#f08080']
plt.figure(figsize=(4, 4))
plt.pie(sizes, labels=labels, autopct='%.1f%%', startangle=40, colors=colors)
plt.title('Beneficiaries with Both Aadhaar and Mobile Number')
plt.axis('equal')
plt.show()

# 6.Detect any outliers in beneficiary data.
beneficiaries = data['total_beneficiaries']

Q1 = beneficiaries.quantile(0.25)
Q3 = beneficiaries.quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = data[(beneficiaries < lower_bound) | (beneficiaries > upper_bound)]
print(f"Number of outlier records: {len(outliers)}")
print(outliers[['state_name', 'district_name', 'total_beneficiaries']])
plt.figure(figsize=(10, 5),dpi=200)
sns.boxplot(x=beneficiaries, color='royalblue')
plt.title('Boxplot of Total Beneficiaries (Outlier Detection)')
plt.xlabel('Total Beneficiaries')
plt.show()
