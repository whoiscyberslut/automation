# The script connects to the IMAP server, logs in using the provided email credentials, and selects the desired mailbox (e.g., "INBOX"). It then 
# searches for email messages based on the specified criteria (in this case, all emails) and iterates over each message.

# For each email message, it fetches the message content, parses it using the email library, and extracts relevant information such as the sender 
# and subject. You can perform further analysis, filtering, or actions based on this extracted information. In the example, it simply prints the 
# sender and subject of each email.

import imaplib
import email

# Connect to the IMAP server
mail = imaplib.IMAP4_SSL("your_imap_server")
mail.login("your_email", "your_password")

# Select the mailbox to process
mailbox = "INBOX"
mail.select(mailbox)

# Search for email messages based on criteria
search_criteria = "ALL"
status, message_ids = mail.search(None, search_criteria)

# Process each email message
for message_id in message_ids[0].split():
    # Fetch the email message
    status, data = mail.fetch(message_id, "(RFC822)")
    raw_email = data[0][1]

    # Parse the email message
    email_message = email.message_from_bytes(raw_email)

    # Extract relevant information from the email message
    sender = email_message["From"]
    subject = email_message["Subject"]

    # Perform actions or analysis based on the extracted information
    # Example: Print the sender and subject of each email
    print(f"Sender: {sender}")
    print(f"Subject: {subject}")
    print("")

    # Perform actions such as moving or deleting the email
    # Example: Move the email to a different mailbox
    # mail.copy(message_id, "DestinationMailbox")
    # mail.store(message_id, "+FLAGS", "\\Deleted")

# Expunge any flagged emails (if required)
# mail.expunge()

# Close the connection to the IMAP server
mail.close()
mail.logout()
