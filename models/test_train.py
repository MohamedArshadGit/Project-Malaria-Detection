import os
from sklearn.model_selection import train_test_split


main_directory =r"C:\Users\Mohamed Arshad\Downloads\Malaria\cell_images\cell_images"

# Get the list of 2 categories directories
Uninfected_images = os.listdir(os.path.join(main_directory, 'Uninfected'))
Parasitized_images = os.listdir(os.path.join(main_directory, 'Parasitized'))


file_paths = []
labels = []

# Append Uninfected file paths and labels
file_paths.extend([os.path.join('Uninfected', img) for img in Uninfected_images])
labels.extend(['Uninfected'] * len(Uninfected_images))

# Append Parasitized file paths and labels
file_paths.extend([os.path.join('Parasitized', img) for img in Parasitized_images])
labels.extend(['Parasitized'] * len(Parasitized_images))

# Split the data into train and test sets (80% train, 20% test)
train_files, test_files, train_labels, test_labels = train_test_split(file_paths, labels, test_size=0.20, random_state=42)

# Create train and test directories
train_directory = r"c:\Users\Mohamed Arshad\Desktop\cell_images\train"
test_directory = r"C:\Users\Mohamed Arshad\Desktop\cell_images\test"

os.makedirs(train_directory, exist_ok=True) 
os.makedirs(test_directory, exist_ok=True)

# Move train files to train directory
for file, label in zip(train_files, train_labels):
    src = os.path.join(main_directory, file)
    dst = os.path.join(train_directory, label, os.path.basename(file)) 
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    os.replace(src, dst)

# Move test files to test directory
for file, label in zip(test_files, test_labels):
    src = os.path.join(main_directory, file)
    dst = os.path.join(test_directory, label, os.path.basename(file))
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    os.replace(src, dst)
