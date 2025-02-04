import streamlit as st
import os

# Title of the app
st.title("Directory Explorer")

# Get the current working directory
current_directory = os.getcwd()

# Display the current directory path
st.write(f"**Current Directory:** `{current_directory}`")

# Fetch all files and folders in the current directory
try:
    items = os.listdir(current_directory)
except Exception as e:
    st.error(f"Error accessing directory: {e}")
    items = []

# Separate files and folders
files = [item for item in items if os.path.isfile(os.path.join(current_directory, item))]
folders = [item for item in items if os.path.isdir(os.path.join(current_directory, item))]

# Display folders
st.subheader("Folders")
if folders:
    st.write("📁 " + ", ".join(folders))
else:
    st.write("No folders found.")

# Display files
st.subheader("Files")
if files:
    st.write("📄 " + ", ".join(files))
else:
    st.write("No files found.")