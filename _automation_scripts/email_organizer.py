# Email Organizer
# Automatically sorts incoming emails into folders based on predefined rules.

import imaplib
import email

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("email@gmail.com", "password")
mail.select("inbox")
status, messages = mail.search(None, 'FROM "newsletter@examples.com"')

for num in messages[0].split():
	mail.store(num, '+X-GM-LABLES', 'Newsletters') #Labels email
	mail.store(num, '+FLAGS', '\\Deleted') # Marks as deleted
mail.expunge()
mail.logout()