# def numIslands(grid):
#     if not grid:
#         return 0

#     def dfs(grid, i, j):
#         if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
#             return
#         grid[i][j] = '0'  # Mark the cell as visited
#         dfs(grid, i + 1, j)  # Move down
#         dfs(grid, i - 1, j)  # Move up
#         dfs(grid, i, j + 1)  # Move right
#         dfs(grid, i, j - 1)  # Move left

#     count = 0
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] == '1':
#                 dfs(grid, i, j)
#                 count += 1

#     return count

# # Example usage:
# grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]

# print(numIslands(grid))  # Output: 3




# import tkinter as tk
# from tkinter import ttk
# import pandas as pd

# # Load your dataset (Make sure the file name matches your dataset)
# df = pd.read_csv("books.csv")

# # Recommendation functions
# def recomd_books_publisheres(x):
#     a = df[df['publisher'] == x][['title', 'average_rating']]
#     a = a.sort_values(by='average_rating', ascending=False)
#     return a.head(10)

# def recomd_books_authors(authors_name):
#     a = df[df['authors'] == authors_name][['title', 'average_rating']]
#     a = a.sort_values(by='average_rating', ascending=False)
#     return a.head(10)

# def recomd_books_lang(language):
#     a = df[df['language_code'] == language][['title', 'average_rating']]
#     a = a.sort_values(by='average_rating', ascending=False)
#     return a.head(10)

# # GUI Setup
# root = tk.Tk()
# root.title("Book Recommendation System")
# root.geometry("500x400")

# # Publisher Dropdown
# tk.Label(root, text="Select Publisher").pack()
# publisher_var = tk.StringVar()
# publisher_dropdown = ttk.Combobox(root, textvariable=publisher_var, values=list(df['publisher'].unique()))
# publisher_dropdown.pack()

# # Author Dropdown
# tk.Label(root, text="Select Author").pack()
# author_var = tk.StringVar()
# author_dropdown = ttk.Combobox(root, textvariable=author_var, values=list(df['authors'].unique()))
# author_dropdown.pack()

# # Language Dropdown
# tk.Label(root, text="Select Language").pack()
# lang_var = tk.StringVar()
# lang_dropdown = ttk.Combobox(root, textvariable=lang_var, values=list(df['language_code'].unique()))
# lang_dropdown.pack()

# # Output Box
# output_text = tk.Text(root, height=10, width=50)
# output_text.pack()

# # Function to Get Recommendations
# def get_recommendations():
#     output_text.delete("1.0", tk.END)
    
#     selected_publisher = publisher_var.get()
#     selected_author = author_var.get()
#     selected_language = lang_var.get()
    
#     recommendations = pd.DataFrame()
    
#     if selected_publisher:
#         recommendations = recomd_books_publisheres(selected_publisher)
#     elif selected_author:
#         recommendations = recomd_books_authors(selected_author)
#     elif selected_language:
#         recommendations = recomd_books_lang(selected_language)
    
#     for idx, row in recommendations.iterrows():
#         output_text.insert(tk.END, f"{row['title']} (Rating: {row['average_rating']})\n")

# # Recommend Button
# recommend_button = tk.Button(root, text="Recommend", command=get_recommendations)
# recommend_button.pack()

# root.mainloop()




import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter Test Window")
root.geometry("300x200")  # Set window size

# Label
label = tk.Label(root, text="Hello! Tkinter is working!", font=("Arial", 12))
label.pack(pady=20)  # Add some space

# Button Function
def on_click():
    label.config(text="Button Clicked!")

# Button
button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

# Run the Tkinter loop
root.mainloop()
