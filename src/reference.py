# data_fe['ServiceArea'] = data_fe.ServiceArea.str[:3]
# data_fe = ohe_cat('ServiceArea', data_fe)
# data_fe.filter(like='ServiceArea')


# data_fe = ohe_cat('Occupation', data_fe)
# data_fe.filter(like='Occupation')


# last_col_names = ['MonthlyRevenue', 'MonthlyMinutes', 'TotalRecurringCharge', 'OverageMinutes', 'CurrentEquipmentDays', 'MonthsInService']
# data_fe = data_fe
# for col in last_col_names:
#     data_fe[col] = data_fe[col].transform(lambda x: np.arcsinh(x))
# transformed_set = data_fe
# for col in last_col_names:
# transformed_set[col] = transformed_set[col].transform(lambda x: np.arcsinh(x))


# dropped_cols.append('Churn')
# data_sd = data_fe.drop(columns = dropped_cols ,axis=1)
# data_sd.info()
# data_sd = data_sd.select_dtypes(include='number')
# num_scale = StandardScaler()
# data_scale = pd.DataFrame(num_scale.fit_transform(data_sd),
# columns = data_sd.columns,
##index = data_sd.index)
# data_scale.describe()
# df_standardise = pd.DataFrame(normalize(data_scale),
# columns = data_scale.columns,
# index = data_scale.index)
# df_standardise.describe()
# data_scale["Churn"] = data_fe["Churn"]
# df_standardise["Churn"] = data_fe["Churn"]
# df_standardise.info()


# PCA
#### Principle Component Analysis

# y = df_standardise["Churn"].copy()

# X = df_standardise.drop("Churn", axis=1).copy()

# X.shape

# pca = PCA()

# pca.fit(X)

# var_exp = pca.explained_variance_ratio_

# var_exp.shape

# plt.figure(figsize=(10, 8))
# plt.plot(range(1, 46), var_exp.cumsum(), marker="o", linestyle="--")
# plt.title("Explained Variance by Components")
# plt.xlabel("# of Components")
# plt.ylabel("Cumulative Explained Variance")
# plt.grid()

# plt.savefig("Explained Variance by Components.jpeg")
# plt.show()

# pca = PCA(n_components=30)
# pca.fit(X)
# var_exp = pca.explained_variance_ratio_
# var_exp.shape


# comp_indecies = ["Component" + str(i) for i in range(1, 31)]

# df_pca_comp = pd.DataFrame(
#     data=pca.components_, columns=X.columns.values, index=comp_indecies
# )

# df_pca_comp


# scores_pca = pca.transform(X)
# scores_pca.shape

# df_pca = pd.DataFrame({})

# df_pca = pd.DataFrame(data=scores_pca, columns=comp_indecies)
# df_pca["Churn"] = df_standardise["Churn"]
# df_pca.reset_index(drop=True, inplace=True)
# df_pca.shape
