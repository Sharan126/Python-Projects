#QRCode Generator Project

import qrcode

#Taking UPI ID as a input
upi_id = input("Enter your UPI ID: ")

#upi://pay?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining the UPI URL based on the UPI ID and the payment app
#You can modify these URLs on the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Creating QR codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#Saving the QR codes as images(Optional)
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

# Displaying the QR codes(You may need to install PIL/PILLOW library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
