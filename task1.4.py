import re

# Read the number of email addresses
n = int(input())

# Read the email addresses into a list
email_addresses = []
for _ in range(n):
    email = input()
    email_addresses.append(email)

# Define a lambda function to check if an email address is valid
is_valid_email = lambda email: re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$', email)

# Filter and sort valid email addresses lexicographically
valid_emails = list(filter(is_valid_email, email_addresses))
valid_emails.sort()

# Print the sorted valid email addresses
for email in valid_emails:
    print(email)