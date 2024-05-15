def count_phrases_in_files(file_names):
  # Define the phrases to search for
  phrases_to_count = [
      "Text contrast", "Item description", "Touch target", "Image contrast",
      "Unexposed Text", "Item label", "Item type label", "Clickable items",
      "Unsupported item type"
  ]

  # Initialize a dictionary to store the count of each phrase
  phrase_counts = {phrase: 0 for phrase in phrases_to_count}

  # Iterate over each file
  for file_name in file_names:
    # Open the file and read its contents
    with open(file_name, "r") as file:
      # Read each line in the file
      for line in file:
        # Check if any of the phrases appear in the line
        for phrase in phrases_to_count:
          if phrase in line:
            # Increment the count for the current phrase
            phrase_counts[phrase] += 1

  # Print the counts of each phrase
  for phrase, count in phrase_counts.items():
    print(f"{phrase}: {count}")


# List of file names to process
file_names = [
    "report1.txt", "report2.txt", "report3.txt", "report4.txt", "report5.txt",
    "report6.txt", "report9.txt", "report10.txt", "report12.txt",
    "report14.txt", "report16.txt", "report18.txt", "report19.txt"
]  # Add all file names here

# Call the function with the list of file names
count_phrases_in_files(file_names)
