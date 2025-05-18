import qrcode

#Talking UPI as a input
upi_id=input("enter the UPI id or mobile number = ")  #or otherwise enter your phone number or upi id 

#upi://pay?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE
#pa=upi id we have to pay 
#apn= my upi id 
#am= amount cu=currency

#defining the payment url based on the upi id and the payment app 
#you can modify these urls based on the paymnet apps you wan tto support 

phonepe_url= f'upi://pay?pa={upi_id}&pn+Recipient%20Name&mc=1234'
paytm_url= f'upi://pay?pa={upi_id}&pn+Recipient%20Name&mc=1234'
google_pay_url= f'upi://pay?pa={upi_id}&pn+Recipient%20Name&mc=1234'

#Create OQ codes for each paymner app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#save the qr code to image file(optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pe_qr.png')

#display the qr code (you may need to install PIL/Pillow Library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()