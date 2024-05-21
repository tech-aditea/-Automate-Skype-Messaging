from skpy import Skype
import os.path

# Initialize Skype
slogin = Skype("your_skype_email/username","your_skype_password")

# Get the contact or group to send the file to
contact = slogin.contacts["skype_username_or_email_of_recipient"]
 
# Sending text message
contact.chat.sendMsg(" Welcome ")

# Specify the file path of the image to be sent 
file_path = "https://github.com/tech-aditea/-Automate-Skype-Messaging/blob/main/skvp.png"

# Open the image file in binary mode
with open(file_path, 'rb') as file:
   # Send the file
   recipient.chat.sendFile(file, "image.jpg")


'''
#FOR  CREATING  GROUP
group = slogin.chats.create(["skype_username_or_email_of_recipient_1","skype_username_or_email_of_recipient_2","skype_username_or_email_of_recipient_3"])

 
#FOR VIEWING ENTIRE CONTACT LIST
contact = slogin.contacts 
for i in contact :
   print(i)
'''


# Logout
slogin.conn.close()

