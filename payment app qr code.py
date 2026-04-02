import qrcode as qr

#Taking input from user
upi_id = input("Enter the UPI ID to be encoded in the QR code: ")
#upi://pay?pa={upi_id}&pn=Name&am=Amount&cu=CUURRENCY&tn=Transaction Note/Message

phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
googlepay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

#Creating QR code
phonepe_qr = qr.make(phonepe_url)
paytm_qr = qr.make(paytm_url)
googlepay_qr = qr.make(googlepay_url)

#Saving QR code as image
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
googlepay_qr.save("google_pay_qr.png")

#Display the QR code using pillow library
phonepe_qr.show()
paytm_qr.show()
