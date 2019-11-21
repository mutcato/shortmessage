# SHORT MESSAGE SENDER
## 
__1.__ git clone 
 
        git clone https://github.com/mutcato/shortmessage.git
        
__2.__ Install requirements
 
        pip install -r requirements.txt
 
__3.__ Create bit.ly account
 
        Click Settings on top right > Settings > Advanced Settings > API Support > User settings > Type your password and click Generate Token > Copy that token

 __4.__ Create a .env file inside the project directory. Put the access token you have copied from bit.ly
 
        access_token=f*************df

 __5.__ Create a Google App 
 
        with following the <a href="https://github.com/mutcato/AutoLoginTest">instructions</a> in steps 1-5.
        After you have downloaded the json file that you created at step 5, name it as googlecredentials.json
     

 __6.__ Create a Sheet file at docs.google.com. Then name it give it a name
        Share that sheet file with email in googlecredentials.json file
        Put your all phone numbers at first column of that file
        Column names must be as ordered (tel,shortened-video-url,sent,clicked)

 __7.__ Set up the settings.py
 
        # Chromedriverın tam dosya yolu (absolute path)
        CHROME_DRIVER = "chromedriver.exe"
        # developers.google.com'dan indirilen json dosyası
        CREDENTIALS = "/googlecredentials.json"
        FILE_NAME = "arac-tel"
        SHEET_NAME = "Sheet1"
        # URL which will be shortened
        long_url_cell = 'F2'
        # mesaj göndermye kaçıncı satırdan başlasın? 2. satırdan başlıyor.
        starting_row = 20
        # kaçıncı satırda bitirsin? 22. satırda bitiriyor.
        end_row = starting_row + 40
    

 __8.__ Run the shortener code
 
        python shortener.py
        
 
 __9.__ Build the text column which will be sent to the phones as a shot message
                
 __10.__ Run the post file
  
        python post.py
         
It will sent text to it's phone number statring with starting_row to the end_row which are in settings.py
          
 __11.__ You can run count_clicks.py  to check if that link clicked or not
        python count_clicks.py
  
