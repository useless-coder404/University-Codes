book_genres = {'sci fi': 12, 'mystery': 15, 'horror': 8,
               'mythology': 10, 'young_adult': 4, 'adventure': 14}

max_key = 0
max_value = 0

for key, value in book_genres.items():
    if max_value == 0 or value > max_value:
        max_key = key
        max_value = value

print("The highest selling book genre is", f"'{max_key}'", end=" ")
print(f"and the number of books sold are {max_value}")
