from skpy import Skype

slogin = Skype("ditea4u@gmail.com","automate4m@m")
contact = slogin.contacts 
#contact.chat.sendMsg(" Welcome ")

for i in contact :
    print(i)



