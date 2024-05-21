from skpy import Skype

slogin = Skype("your_skype_email/username","your_skype_password")

#FOR SENDING AUTOMATED MSSG TO GROUP
#group = slogin.chats.create(["skype_username_or_email_of_recipient_1","skype_username_or_email_of_recipient_2","skype_username_or_email_of_recipient_3"])

#FOR SENDING AUTOMATED MSSG TO PARTICULAR PERSON  
#contact = slogin.contacts["skype_username_or_email_of_recipient"] 
#contact.chat.sendMsg(" Welcome ")

#FOR VIEWING ENTIRE CONTACT LIST
#contact = slogin.contacts 
#for i in contact :
#   print(i)



