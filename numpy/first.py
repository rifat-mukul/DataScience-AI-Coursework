import numpy as np

# 1. Generate synthetic data for demonstration purposes
# Create a dataset with 100 samples and 5 features
np.random.seed(0)
data = np.random.randn(100, 5) * 10 + 50  # Mean=50, Std=10

# 2. Basic array operations
# Calculate the mean of the dataset
mean = np.mean(data, axis=0)
print("Mean of each feature:", mean)

# Calculate the standard deviation of the dataset
std_dev = np.std(data, axis=0)
print("Standard deviation of each feature:", std_dev)

# 3. Data normalization
# Normalize the dataset (z-score normalization)
data_normalized = (data - mean) / std_dev
print("\nFirst 5 samples of normalized data:\n", data_normalized[:5])

# 4. Matrix operations
# Create a covariance matrix
cov_matrix = np.cov(data_normalized, rowvar=False)
print("\nCovariance matrix:\n", cov_matrix)

# Eigen decomposition
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
print("\nEigenvalues:\n", eigenvalues)
print("\nEigenvectors:\n", eigenvectors)

# 5. Data transformation
# Project data onto the first principal component
principal_component = eigenvectors[:, 0]
data_transformed = np.dot(data_normalized, principal_component)
print("\nFirst 5 samples of transformed data:\n", data_transformed[:5])

# 6. Statistical analysis
# Calculate the correlation matrix
correlation_matrix = np.corrcoef(data_normalized, rowvar=False)
print("\nCorrelation matrix:\n", correlation_matrix)

# Find the feature with the highest variance
max_variance_index = np.argmax(np.var(data_normalized, axis=0))
print("\nFeature with highest variance:", max_variance_index)

# 7. Boolean indexing and filtering
# Find samples where the first feature is greater than 1
filtered_samples = data_normalized[data_normalized[:, 0] > 1]
print("\nNumber of samples where the first feature is greater than 1:", filtered_samples.shape[0])

# 8. Aggregation operations
# Calculate the sum of each feature
sum_features = np.sum(data, axis=0)
print("\nSum of each feature:", sum_features)

# Calculate the minimum and maximum values of each feature
min_values = np.min(data, axis=0)
max_values = np.max(data, axis=0)
print("\nMinimum values of each feature:", min_values)
print("Maximum values of each feature:", max_values)

# 9. Reshaping and broadcasting
# Reshape the data to add a new axis
data_reshaped = data_normalized[:, np.newaxis, :]
print("\nShape of data after reshaping:", data_reshaped.shape)

# Create a new array with broadcasting
new_array = data_normalized * 2
print("\nFirst 5 samples of new array after broadcasting:\n", new_array[:5])
