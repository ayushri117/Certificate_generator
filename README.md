# Certificate_generator

I wanted to have some kind of feature by which sending certificates would be easy via mail, so here is a certificate generator which generates certificates based on the details in the csv file, and also adds a Qr code to the certificate for further verifications purposes. The QR code contains the link of the website, the html code for the website is also generated simultaneously with specific name so no two people have the same link on their certificate, after this all we need to do is upload the html files and the generated  certificates on to the website server, for this project i am using drive to web platform to host the sitefor this purpose i am using drive to web platform, this program also sends the mail to people automatically when running, 

so my code automatically generates all the certificates, and html code for the website and generates the QR code and finally sends the certificate to the respective person.


before executing the code run the following commands

      pip install Pillow
      
      pip install qrcode
      
On line 12 and 13 of the  code in main.py file the font  type is specified, the location of font is specified for Fedora 34, if using windows or any other OS change it accordingly
