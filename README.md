# Certificate_generator

I wanted to have some kind of feature by which sending certificates would be easy via mail, so here is a certificate generator which generates certificates based on the details in the csv file, and also adds a Qr code to the certificate for further verifications purposes, After generating the certificates it savs them in diferent folder, and then sends the certificates to the respective users via mail (the email of users is there in the csv file)


before executing the code run the following commands

      pip install Pillow
      
      pip install qrcode
      
On line 13 and 14 of the  code in main.py file the font  type is specified, the location of font is specified for ubuntu, if using windows change it accordingly
