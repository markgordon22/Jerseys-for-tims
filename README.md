# Project Overview
 
View the live project [here.]()
 
Jerseys for Tims was my final milestone project as part of the Code Institute's Software Development Diploma. This project is intended to be a full-stack e-commerce site, with the use Python, Django, based on a fictional online Irish celtic jersey website (Jerseys for Tims) which sells celtic jerseys over the previous 4 decades(home and away), home merchandise with deals and special offeres. Users of the site can search products available. Read FAQS of the site posted by the owner, register an account to keep track of purchases. Jerseys for Tims, ultimately is a store where users can find their favorite celtic jerseys and merchandise that promotes celtic football club, for people who love and follow their team like it is a religon.
 
 
The rationale behind making Jerseys for Tims was my love for celtic football club. Jerseys for Tims was made to reflect  every valuable takeaway studied from the [Code Institute's Full Stack Diploma in Web Development](https://codeinstitute.net/) course, maintaining a MVP approach to the site whilst creating a fully-functioning e-commerce site.
 
 
Primary functions of Siopa Fia:
- Product purchase functionality
- User authentication and authorisation
- Customer profile page which will contain purchase history and store customer details
- All CRUD functionalities
 
 
---
 
## Contents
 
- [UX](#ux)
   - [Strategy](#strategy)
       - [Business Logic](#business-logic)
       - [User Stories](#user-stories)
   - [Scope](#scope)
       - [Existing Features](#current-features)
           - [Base HTML](#base-html)
           - [Home Page](#home-page)
           - [All Products Page](#all-products-page)
           - [Product Detail Page](#product-detail-page)
           - [Shopping Bag Page](#shopping-bag-page)
           - [Checkout Page](#checkout-page)
           - [Checkout Success Page](#checkout-success-page)
           - [Profile Page](#profile-page)
           - [FAQs Page](#faqs-page)
           - [Profile Page](#profile-page)
           - [Contact Page](#contact-page)
       - [Features Left To Implement](#features-left-to-implement)
   - [Structure](#structure)
   - [Skeleton](#skeleton)
       - [Wireframes](#wireframes)
   - [Surface](#surface)
       - [Design](#design)
           - [Colour Scheme](#colour-scheme)
           - [Typography](#typography)
           - [Imagery](#imagery)
           - [Icons](#icons)
- [Information Architecture](#information-architecture)
   - [Database](#database)
   - [Data Modelling](#data-modelling)
- [Technologies used](#technologies-used)
   - [Languages Used](#languages-used)
   - [Frameworks, Libraries & Programs Used](#frameworks-libraries-programs-&-databases-used)
- [Testing](#testing)
- [Deployment](#deployment)
    - [Heroku Deployment with AWS](#heroku-deployment-with-aws)
    - [Amazon Web Services](#amazon-web-services)
    - [Local Deployment](#local-deployment)
- [Credits](#credits)
- [Disclaimer](#disclaimer)
- [Acknowledgements](#acknowledgements)
 
# User Experience (UX)
 
## Strategy
 
### Business Logic
 
- For the site to be easyily navigated, create positive ux's for the user
- To add, edit or delete products available(crud functionality)
- To encourage the user to understand the story behind Jerseys for Tims
- To promote awareness of Jerseys for Tims to boost brand awareness to become the top celtic provider for celtic fans.
 
### User Stories
 
|      As a/an...      |                         I want the ability to...                         |                        So that I can...                       |
|:--------------------:|:------------------------------------------------------------------------:|:-------------------------------------------------------------:|
|                      |                                                                          |                                                               |
|          ---         |                                    ---                                   |                              ---                              |
| First time user      | easily navigate Jerseys for Tims;                                                | see what I am searching for quickly                            |
| First time user      | view the site on aa multiple of screen sizes;                                       | view the platform across a multiple of screen devices                             |
| First time user      | see different lists of products                                                  | see items that are available to purchase                                   |
| First time user      | see product details/info                                          | see exactly what I am buying or might buy                                 |
| First time user      | read company description and the story behind it                                       | gain trust in the company and support local business activity          |
| First time user      | search for product categories                                       | find the best-rated/priced products in a specific category    |
| First time user      | search for a product by name, category.                                | easily find the exact product Im looking for                  |
| First time user      | view items chosen/selected in my shopping bag                                  | easily see how much I might be spending                             |
| First time user      | modify shopping bag contents                         | easily alter my order, when I might change my mind               |
| First time user      | access contact details of the company;                                                  | get in touch with any questions I may have now or in the future                              |
| First time user      | access social media platforms of the company;                                      | view their social media presence  and be able to contact via those respective platforms               |
| First time user      | register a user profile account by picking a username, password; | use this as storage of my own details and purchase history            |
| First time user      | make purchases as a guest user                                          | do not have to set up an account if I dont wish to           |             
|          ---         |                                    ---                                   |                              ---                              |
| Registered user      | log in and out of my profile;                                |  prevent negligence of other users trying to access my account       |
| Registered user      | update my personal details                                                        | update address, phone number etc, in case they need to be altered          |
| Registered user      | store address                                          | dont have to type it every occasion I want to purchase something        |
| Registered user      | save my past purchases;                                               | view my purchase history                           |
| Registered user      | store my choices in checkout;                                            | go back to the site in case I wish to add more options        |
| Registered user      | Make safe and secure transactions/payments                                                    | ensure my payments are handled safely and securley                       |
| Registered user      | to be sent confirmation by email of purchases                                     | finalise that payment for items was successful |
|          ---         |                                    ---                                   |                              ---                              |
| Site Owner           | add new items and category listings;                                     | continuously update the site with new items or specials       |
| Site Owner           | update items                                                             | alter price or product criteria                              |
| Site Owner           | remove items                                                             | remove items that are no longer for sale                      |
| Site Owner           | view orders made through siopaFIA                                                              | keep track of new and existing orders                      |
| Site Owner           | view and manage users of Jerseys for Tims                                                            | keep track of new and existing users                      |
| Site Owner           | Continually update/modify faqs so users won't have to wait for responses from Jerseys for Tims   on their concerns                                                        | to inform visitors to the site of concerns they could have                  |
 
---
 
 
## Scope
 
### Existing Features
 
### Base HTML
 
Seen across all pages of site
 
### Navbar
 
The navbar for Jerseys for Tims includes separate designs - one for mobile and tablet devices and the other design for larger devices such as desktop. Simarliy, in the walkthrough project, Boutique Ado supplied by Code Institute, for smaller devices I incorporated Bootstrap's [collapsible toggler](https://getbootstrap.com/docs/4.1/components/navbar/#external-content), the user to the site can be redirected to the main componenents in a drop-down view. The items in the dropdown menu are identical to the ones in the navbar on desktop view. The company logo is present to be a link to the home page of the aswell as the home link on the top of the dropdown list via the hamburger icon from bootstrap. There is also a search icon and a My Account link, where users of the site can register, sign in or view their profile. The user can always view their current spending by the bag displaying the total amount of the items purchased which is posible to view on every page of Jerseys for Tims
 
### Delivery Banner
 
Throughout the site, users will see the free delivery offer on spending anything over £80 using a [scroll-text animation](https://stackoverflow.com/questions/55227106/css-animation-text-sliding-left-to-right) feature from stackoverflow.
 
![image]()
 
### Messages (Toasts)
  Toasts were used so users are aware of important site interactions, such as items being added to their bag, signing up to the newsletter/confirmation, logging in to their profile etc. I imported 'messages' from Django's 'django-contrib' the messages displayed included (error, success, warning, info) are in [Bootstrap's Toast](https://getbootstrap.com/docs/5.0/components/toasts/) format:
 
![image]()
 
### Footer
The footer is displayed on every page of Jerseys for Tims and includes two sections. into three separate parts: social links (where the user can follow the company via Facebook, Twitter etc), Shop and Company links.
 
![image]()
 
### Home Page:
Upon directing to the site, the user will receive a sense of what the Jerseys for Tims is about with css fade in texted slogan above the "Shop now!" fade in texted button. The hero image of Parkhead which is the home stadium for Celtic Football Club is which is dubbed "Paradise" by celtic supporters as it is the club they live and breath was selected to convey the message of "home" as it is a home the stadium of celtic football club and the place where many fond memories have been made and will continue to be made, watching the football team they love. The main logo of the site reads "Jerseys for Tims" the word "tim" is a nickname for a celtic fc supporter. The sale button redirects the user to all  94 products the website has, where the user can see the products Jerseys for Tims sells.
 
 
### All Products Page:
Similarly to Boutique Ado, the sample walkthrough project supplied to by Code Institute, I demonstrated similar design of displaying 4 products larger deviced pages, medium devices contained 3 products, smaller deviced contained 2 products, with extra small devices containing just one device. The product cards displays an image of the product along with its name, price, category. The user is abled to click an image where they are redirected to the product detail page where they can see further details and description of the product they selected and have the opportunity to add the product to their shopping bag. I decided to place in buttons with the text "quick view" to entice perhaps impulsive users into making them decide to buy a product for business and marketing purposes.
 
As the product list could be large depending on the category of products selected by the user, I included a yellow scroll button which corresponds to the color scheme of the site so that the user can be brought back to the top of the page once scroll button is clicked.
 
### Product Detail Page:
Displaying a larger image and more detail information with a description on the product selected by the user, the user can select the item's size (depending on if the product has sizes), the quantity (within range of the site) they desire to purchase. The user can either click the "Keep Shopping" button at the bottom of the product details where they are redirected back to the all products page or they can add the product to their respective bag by clicking "Add to Bag" button to the right of the "keep shopping" button. The user gets informed they have selected the item with a toast success message from bootstrap which alerts them of the products they've in their bag, with how much (depending on the amount they've in their bag) more they will be required to spend in order to avail of the free delivery offer that is on offer by Jerseys for Tims.
The edit and delete anchor links in the product card is only displayed on the superusers account of the site.
 
### Shopping Bag Page:
This page is divided into 5 sections- a smaller image of the item,product name,SKU number, product price and the quantity box selector with respective remove and update links and the subtotal. Should the user want to modify contents of their bag, they can update their order on this page via the quantity selector box using the remove or update buttons. The grand total is shown, along with its delivery charge information (unless user has spent over the free delivery threshold) towards the bottom of the page. The user can also return to the all products page of the site by selecting "Keep Shopping" button, or if they are happy with their bag contents they can follow on with their purchase by selecting the  "Secure Checkout" button.
 
### Checkout Page:
 
The checkout page includes forms such as user's name, details of billing and the payment form that is mandatory in order to complete the purchase. Below the credit card form they're yet again informed the total their card will get charged and can proceed to confirm payment or they if unsure of their payment can adjust their bag and return to the shopping bag page by clicking the "adjust bag" button:
 
![image]()
 
### Checkout Success Page:
 
Once the purchase is finalised and completed, a success message from bootstrap toasts appears with confirmation that the payment was successfull, along with details of the order number and a confirmation email will be sent to the user. The details of the user's order are shwon and a button redirecting to the "new-arrivals" category page is below:
 
![image]()
 
 
### FAQs Page:
 
Accessible by clicking "FAQS" from the navbar, the user is redirected to the faq app. There is a series of questions with answers on matters that the user may potentially now have or have in future references. Only the site admin can edit/delete faqs. user can also not manually enter the url for the edit/add faqs as they will get instaly get redirected to the sign in page
 
 ### Profile Page:
 
This Profile is reachable only to a registered user that is logged in where the user can track their own individual purchases and payments and modify their personal information. Divided into two sections, the first shows the default delivery information of that user and the second section depicts the past orders of that user along with its cost,order number, items bought and the date the payment for the order was made
 
### Product Pages
---
 
### Product Management Page
 
Accessible only to site admin, once logged in they can select "My Account" (dropdown in the navbar) and from there select Product Management where from here they can add any new product that fits into one of the categories listed (Clothing, Footwear, Skincare, etc.)
 
 
### Features Left To Implement
- None.
 
 
## Structure
- I wanted to create Jerseys for Tims in a manner that deemed clear to new users; easy navigation, find products intuitively and make quick and easy transactions. The site is divided into clear sections and created with Django using the apps listed below: 
- Home, 
- Products, 
- Profiles,
- Bag,
- Checkout,
- Contact,
- About,
- FAQ.

Having installed Django allauth, respective authentication, registration, account management with bootstrap responsive elements such as toasts, navbar, buttons, links, the pathway to payment for the user was a simple one.
 
## Information Architecture
 
### Database
- SQLlite  was used for local development.
- PostgreSQL was used when deployed through Heroku(Hobby Dev).
 
### Data Modelling
 
- All data related to Products was compiled in a JSON format and is stored in a fixtures folder, as does the FAQ data in its own fixtures folder.
- The Data Model below was created using [drawSQL]():
 
![image]()
 
**Changes made to the Database Model since creation:**
- The one addition I made to the Blog Model was alter and create three further fields (intro, body_one, body_two, body_three) that contain TextFields. This was to allow more spacing and better paragraph usage in the blog_detail page thus avoiding long and chunky text that can be difficult to read.
 
#### [Back to Contents](#contents)
---
 
## Wireframes
 
see wireframes [here](https://github.com/markgordon22/Jerseys-for-tims/tree/main/wireframes)
 
## Surface
 
### Design
-  #### Colour Scheme
   As the colour green is the dominant colour throughout the site, I thought it was a good choice that suited the theme of the site. It is fresh, clean and most often the colour choice for use with the term, "eco" or "environment". The colour chart used is as below, taken from [Color-Hex:](https://www.color-hex.com/color-palette/112498)
 
   ![image]()
 
-   In addition to the colour chart chosen, primarily green, to add some diversity is #FFC107 - a strong, bold and mustard-toned yellow that I found eye catching and grabs the user's attention towards it. I used it for the CTA button on the home page, the submit button below the newsletter signup and when hovering over the links in the footer:
 
   ![image](
 
 
 
### Typography
[) font is the logo font used throughout the whole website for headers, navbar categories and dropdown list items partnered with font for the bulk text/paragraph use. Sans Serif was the fallback font in case for
any reason the font isn't being imported into the site correctly. I chose these fonts as I felt it fit well with the 'eco' theme of the business without overstyling the site with flambouyancy. I believe it has a modern feel, both fonts stand out and fit well throughout the site.
 
![image]()
 
### Imagery

 
### Icons
The icons used throughout the site are taken from [Font Awesome](https://fontawesome.com/).
 
 
---
 
# **Technologies used**
 
## **Languages**
 
-   [HTML5](https://en.wikipedia.org/wiki/HTML5): used for creating the structure of the project
-   [CSS3](https://en.wikipedia.org/wiki/CSS): cascading style shhets to style, position create animations.
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript): to make interactivity for elements o site
-   [Python](https://www.python.org/): the backend frameword
 
## **Frameworks, Libraries and Other Sources**
 
- [Balsamiq](https://balsamiq.com/) to make wireframes for site
 
- [Django](https://www.djangoproject.com/) utilised as the predominant framework for the project.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) for forms on site.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) for user authenticity for site.
- [Stripe](https://stripe.com/) to deal with payments for site.
- [Bootstrap4](https://getbootstrap.com/) to get site responsive
- [Amazon Web Services](https://aws.amazon.com/) stirage for static and media files.
- [SQLite3](https://www.sqlite.org/index.html) is the database utilized during production.
- [PostgreSQL](https://www.postgresql.org/) database for deployed the site.
- [Heroku](https://www.heroku.com/) cloud platform to host the site.
- [JQuery](https://jquery.com/) for ultimate bootstrap functionality
- [GitPod](https://gitpod.io/) the IDE for the site production
- [GitHub](https://github.com/) storage for Jerseys for Tims repo. Commits were frequent, code was pushed to GitHub from GitPod.
 
# **Testing**
 
Jerseys for Tims has been documented in a separate file that can be accessed here: [TESTING.md](https://github.com/elerel/ms4-siopa-fia/blob/master/TESTING.md)
 
#### [Back to Contents](#contents)
 
---
 
# **Deployment**
 
## **Heroku Deployment with AWS**
 
To deploy Jerseys for Tims to [Heroku](https://dashboard.heroku.com/apps), the following steps were taken in chronological order:
1. Instalation of the following
- gunicorn
- psycopg2-binary and dj-database-url using [PIP](https://pypi.org/project/pip/).
2. Made a requirements.txt file and then froze all the required modules and dependencies to the respective file using "pip3 freeze > requirements.txt"
3. Made a Procfile and added "web: gunicorn jerseys_for_tims.wsgi:application"
4. To push changes up to my github repo, the following commands were used in chronological order.
- git status
- git add
- git commit -m "commit message"
- git push
5. I logged into my own respective account on followed by creating a new app, I selected Europe (eu-west-1) as I am based in Dublin region.
6. Select Resources tab in Heroku nav menu. After that I clicked the Add-ons search bar added Heroku Postgres to act as my database when site is not using sqlite3 as the database, choose  the plan name of "Hobby Dev - Free" followed by clicking
**Submit Order Form** to add it to the Jerseys for Tims project.
7. In the dashboard for the application, I clicked on Settings, then Reveal Config Vars and set the following values to appear as below:
 
|Key|Value|
|--|--|
|AWS_ACCESS_KEY_ID|```Your AWS Access Key```|
|AWS_SECRET_ACCESS_KEY|```Your AWS Secret Access Key```|
|DATABASE_URL   |```Your Postgres Database URL```|
|SECRET_KEY |```Your Secret Key```|
|STRIPE_PUBLIC_KEY  |```Your Stripe Public Key```|
|STRIPE_SECRET_KEY  |```Your Stripe Secret Ke```y|
|STRIPE_WH_SECRET   |```Your Stripe WH Key```|
|USE_AWS    |```True```
 
8. I navigated to the deploy tab in the medu, under Deployment method, I clicked GitHub and then enabled automatic deploys. When the app has finished building, click **Open app** button on the top of the page, it is next to a "more" button.
9. Commented out current DATABASE setting in settings.py, and insert the following code:
```
DATABASES = {    
       'default': dj_database_url.parse("<your Postgres database URL here>")    
   }   
```
 
10. Retreat to the heroku dashboard, click 'deploy', and then underneath the 'Deployment' method, select GitHub and enable 'Automatic Deploys'.
 
11. In settings.py, the following code is commented out(old code):
```
Database
https://docs.djangoproject.com/en/3.1/ref/settings/#databases
```
and then instead the following code is added(new code):
```
DATABASES = {
       'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
   }
```
12. Plan for migration via this command:
```
python3 manage.py makemigrations --dry-run
```
 
13. Make migrations via this command:
```
python3 manage.py makemigrations
```
14. and migrate the database models to the Postgres database using the following command:
```
python3 manage.py migrate
```
15. Load fixtures from the relevant JSON files, which are contained in the 'fixtures' folders in the respective apps into the database.
This is done by using the following command:
```
python3 manage.py loaddata <file name>
```
16. Create a new superuser with the following command:
```
python3 manage.py createsuperuser
```
proceed to then enter chosen email, username and password.
 
17. In settings.py, contain the previously entered database setting in an if statement, and add an else condition, so that different databases are
used depending on the environment whether it is the local one or deployed one on heroku.
```
 
#local database
if 'DATABASE_URL' in os.environ:
   DATABASES = {
       'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
   }
 
#deployed database
else:
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
```
18. Disable 'COLLECTSTATIC' with:
```
heroku config:set DISABLE_COLLECTSTATIC=1
```
so that Heroku will not try to collect static files.
 
19. Add
```
ALLOWED_HOSTS = ['.herokuapp.com', 'localhost']
```
to settings.py.
 
20. Addition of Stripe env variables to settings.py.
 
21. Finally, push to Heroku using the:
```
git push heroku main
```
 
---
 
 
## **Amazon Web Services**
 
I used Amazon web services to host static and media files for the deployed site kept in the Jerseys for Tims S3 bucket. I made an account followed by creating a new S3 bucket
and uploaded the jerseys for Tims static, media files. Detailed surrounding these services can be seen [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
Similarly, in the Boutiquqe Ado walkthrough, I used this following CORS configuration:
```
[
   {
       "AllowedHeaders": [
           "Authorization"
       ],
       "AllowedMethods": [
           "GET"
       ],
       "AllowedOrigins": [
           "*"
       ],
       "ExposeHeaders": []
   }
]
```
 
1. Returning to the IDE terminal, I installed boto3 and django-storages using the ```pip3 install``` and then froze them using ```pip3 freeze > requirements.txt```
in order to connect the S3 bucket to Django.
2. Added 'storages' to the list of ```INSTALLED_APPS``` in settings.py
3. Added the following also in settings.py:
```
if 'USE_AWS' in os.environ:
   if 'USE_AWS' in os.environ:
       # Cache control
       AWS_S3_OBJECT_PARAMETERS = {
           'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
           'CacheControl': 'max-age=94608000',
       }
 
 
   # Bucket Config
   AWS_STORAGE_BUCKET_NAME = 'jerseysfortims'
   AWS_S3_REGION_NAME = 'eu-west-1'
   AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
   AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
   AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
 
   # Static and media files
   STATICFILES_STORAGE = 'custom_storages.StaticStorage'
   STATICFILES_LOCATION = 'static'
   DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
   MEDIAFILES_LOCATION = 'media'
 
   # Override static and media URLs in production
   STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
   MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
4. Created a custom_storages.py file at the top level folder which includes the location of the Static Storage and Media Storage.
5. Removed DISABLE_COLLECTSTATIC from Heroku's Config Var.
6. Pushed all the changes to Github and thus Heroku.
 
## **Local Deployment**
Alternatively, you can follow these steps, which are detailed on the official
[GitHub Documentation](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)
 
You should then make an env.py file in the root directory of the project, and add it a file to .gitignore file.
This project will only run locally if an env.py file is set up containing
- the IP
- the PORT
- the SECRET_KEY.
The following code must be used in your env.py file:
 
```
import os 
os.environ["DEVELOPMENT"] = "True"   
os.environ["SECRET_KEY"] = "<Your Secret Key>"
os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public Key>"   
os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret Key>"   
os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH Secret Key>"  
```
 
Ensure the respective required packages have been installed with:
 
```
pip install -r requirements.txt
 
```
 
After you have endured the releavnt required package are installed you should then
 
Make migrations with
```
python3 manage.py makemigrations
 
```
Then run the following command to ensure the database is created
```
python3 manage.py migrate
 
```
 
Load the fixtures from the 'products.json' and 'faq.json' files - which are contained in the 'fixtures' folder into the database.
This is done by using the following command:
```
   python3 manage.py loaddata <file name>
```
 
Make your own superuser with: ```python3 manage.py createsuperuser``` and make your own username and password .
 
Run your own app with:
```python3 manage.py runserver```
 
 
### **Credits**
 
**Code:**
- The walkthrough project in the Full Stack Frameworks with Django Module, Boutique Ado, was the primary source and guide when it came to building Jerseys for Tims. This was a template for me to build my own faq and contact apps.
- For the contact app I followed [Twilio](https://www.twilio.com/blog/build-contact-form-python-django-twilio-sendgrid)
- To render the scroll back to top arrow on the about page and products pages I used code from [W3 schools](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp)
- [Bootstrap](https://getbootstrap.com/docs/5.0/forms/layout/) used to make footer, navbar, cards, toasts, cards images and buttons.
- [Stackoverflow](https://stackoverflow.com/questions/55227106/css-animation-text-sliding-left-to-right) for help on how to make the scroll text animation on the delivery banner
- [Stackoverflow](https://stackoverflow.com/questions/29211115/adding-link-to-the-admin-index-page-in-django) on adding the Django admin index url
- [Django Docs](https://django-book.readthedocs.io/en/latest/chapter14.html) was a guide used to look over elements such as django imports, models and admin panels.
 
**Content:**
- [Yours Clothing](https://www.yoursclothing.ie/faq?glCountry=IE&glCurrency=GBP) was used to generate some sample faqs.
- All jerseys descriptions were written by me as Ive grown up watching celtic and knowing the different jerseys used     over  the past years
 
**Media:**
- All images were taken from Google imagess

***images***




 
### **Disclaimer**
All content on this site is for educational purposes solely.
 
### **Acknowledgements**
- My thanks to my mentor [**Rohit Sharma**] for his time and support during the throughout the course of being my mentor and a guide, the ever selfless Slack Community, CI tutor support (my special thanks to Scott, Igor, John, Sheryl and Michael!) and last but not least, [Chris Z](https://github.com/ckz8780) for explaining the walkthrough project so brilliantly.
- A big Thanks aswell to my family for their continued support.
 
 
##### [Back to Contents](#contents)
