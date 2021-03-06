# Project Overview
 
View the live project [here.](https://jerseys-for-tims.herokuapp.com/)
 
Jerseys for Tims was my final milestone project as part of the Code Institute's Software Development Diploma. This project is intended to be a full-stack e-commerce site, with the use Python, Django, based on a fictional online Irish celtic jersey website (Jerseys for Tims) which sells celtic jerseys over the previous 4 decades(home and away), home merchandise with deals and special offeres. Users of the site can search products available. Read FAQS of the site posted by the owner, register an account to keep track of purchases. Jerseys for Tims, ultimately is a store where users can find their favorite celtic jerseys and merchandise that promotes celtic football club, for people who love and follow their team like it is a religon.
 
 
The rationale behind making Jerseys for Tims was my love for celtic football club. Jerseys for Tims was made to reflect  every valuable takeaway studied from the [Code Institute's Full Stack Diploma in Web Development](https://codeinstitute.net/) course.
 
 
Primary functions of Jerseys for Tims
- Product purchase functionality in bag and checkou apps
- authentication,authorisation for users to the site
- Consumer profile pagethat will contain purchase history and act as a storage unit for customer details
- Create Read, update and delete functionality(CRUD)
 
 
---
 
## Contents
 
- [UX](#ux)
   - [Strategy](#strategy)
       - [Business Logic](#business-logic)
       - [User Stories](#user-stories)
   - [Scope](#scope)
       - [Existing Features](#existing-features)
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
 
- For the site to be easily navigated, create positive ux's for the user
- To add, edit or delete products available(crud functionality)
- To encourage the user to understand the story behind Jerseys for Tims
- To promote awareness of Jerseys for Tims to boost brand awareness and loyalty and to become the top celtic jersey provider for celtic fans.
 
### User Stories
 
|      As a/an...      |                         I want the ability to...                         |                        So that I can...                       |
|:--------------------:|:------------------------------------------------------------------------:|:-------------------------------------------------------------:|
|                      |                                                                          |                                                               |
|          ---         |                                    ---                                   |                              ---                              |
| First time user      | easily navigate around Jerseys for Tims;                                                | see what I am searching for quickly                            |
| First time user      | view the site on multiple screen devices and sizes;                                       | view site on different screen sizes                             |
| First time user      | see different lists of products                                                  | see items that are available to purchase                                   |
| First time user      | see product details/info                                          | see exactly what I am buying or might buy                                 |
| First time user      | read company description and the story behind it                                       | gain trust in the company I might be buying from         |
| First time user      | search for product categories                                       | find the best-rated/priced products in a specific category    |
| First time user      | search for a product by name, category.                                | easily find the exact product Im looking for                  |
| First time user      | view items chosen/selected in my shopping bag                                  | easily see how much I might be spending                             |
| First time user      | modify shopping bag contents                         | easily alter my order, when I might change my mind               |
| First time user      | access contact details of the company;                                                  | get in touch with any questions I may have now or in the future                              |
| First time user      | access social media platforms of the company;                                      | view their social media presence  and be able to contact via those respective platforms               |
| First time user      | register a user profile account by picking a username, password; | use this as storage of my own details and purchase history            |
| First time user      | make purchases as a guest user                                          | not have to set up an account if I dont wish to           |             
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
| Site Owner           | remove items                                                             | remove items that are no longer for sale                      ||
| Site Owner           | view and manage users of Jerseys for Tims                                                            | keep track of new and existing users                      |
| Site Owner           | Continually update/modify faqs so users won't have to wait for responses from Jerseys for Tims   on their concerns                                                        | to inform visitors to the site of concerns they could have                  |

 
---
 
 
## Scope
 
### Existing Features
 
### Base HTML
 
Seen across all pages of site
 
### Navbar
 
The navbar for Jerseys for Tims includes separate designs - one for mobile and tablet devices and the other design for larger devices such as desktop. Simarliy, in the walkthrough project, Boutique Ado supplied by Code Institute, for smaller devices I incorporated Bootstrap's [collapsible toggler](https://getbootstrap.com/docs/4.1/components/navbar/#external-content), the user to the site can be redirected to the main componenents in a drop-down view. The items in the dropdown menu are identical to the ones in the navbar on desktop view. The company logo is present to be a link to the home page aswell as the home link on the top of the dropdown list via the hamburger icon from bootstrap. There is also a search icon and a My Account link, where users of the site can register, sign in or view their profile. The user can always view their current spending by the bag displaying the total amount of the items purchased which is posible to view on every page of Jerseys for Tims

Navbar
![image](uximages/navbar.png)



mobile navbar
![image](uximages/mobilenav.png)
 
### Delivery Banner
 
Throughout the site, users will see the free delivery offer on spending anything over ??80 using a [scroll-text animation](https://stackoverflow.com/questions/55227106/css-animation-text-sliding-left-to-right) feature from stackoverflow.
 
![image](uximages/deliverybanner.png)
 
### Messages (Toasts)
  Toasts were used so users are aware of important site interactions, such as items being added to their bag or logging in to their profile etc. I imported 'messages' from Django's 'django-contrib' the messages displayed included (error, success, warning, info) are in [Bootstrap's Toast](https://getbootstrap.com/docs/5.0/components/toasts/) format:
 
 Here is the success message which is apparent throughout the site.
![image](uximages/toast.png)
 
### Footer
The footer is displayed on every page. It contains quotes from famous celtic footballers. There are links to the product categories and contact/faq section of the site.
 
![image](uximages/footer.png)
 
### Home Page:
Upon directing to the site, the user will receive a sense of what the Jerseys for Tims is about with css fade in texted slogan above the "Shop now!" and the fade in button below it. The hero image of Parkhead which is the home stadium for Celtic Football Club is dubbed "Paradise" by celtic supporters as it is the club they live and breath. It was selected to convey the message of "home" as it is the home stadium of celtic football club and the place where many fond memories have been made and will continue to be made, watching the football team they love. The main logo of the site reads "Jerseys for Tims" the word "tim" is a nickname for a celtic fc supporter. The shop button redirects the user to all 93 products the website has, where the user can see the products Jerseys for Tims sells.

![image](uximages/homepageimg.png)
 
 
### All Products Page:
Similar to Boutique Ado, the sample walkthrough project supplied to by Code Institute, I demonstrated similar design of displaying 4 products on larger deviced pages, medium devices contained 3 products, smaller deviced contained 2 products, with extra small devices containing just one product per row. The product cards displays an image of the product along with its name, price, category. The user is able to click an image where they are redirected to the product detail page where they can see further details and description of the product they selected and have the opportunity to add the product to their shopping bag. I decided to place in buttons with the text "quick view" to entice perhaps impulsive users into making them decide to buy a product for business and marketing purposes.
 
As the product list could be large depending on the category of products selected by the user, I included a yellow scroll button which corresponds to the color scheme of the site so that the user can be brought back to the top of the page once scroll button is clicked. This is from w3 schools and is credited in the readme.

![image](uximages/productpageimg.png)
 
### Product Detail Page:
Displaying a larger image and more detailed information with a description on the product selected by the user, the user can select the item's size (depending on if the product has sizes), the quantity (within range of the site) they desire to purchase. The user can either click the "Keep Shopping" button at the bottom of the product details where they are redirected back to the all products page or they can add the product to their respective bag by clicking "Add to Bag" button to the right of the "keep shopping" button. The user gets informed they have selected the item with a toast success message from bootstrap which alerts them of the products they have in their bag, with how much (depending on the amount they've in their bag) more they will be required to spend in order to avail of the free delivery offer that is on offer at Jerseys for Tims.
The edit and delete anchor links in the product card is only displayed on the superusers account of the site.

![image](uximages/productdetailspageimg.png)
 
### Shopping Bag Page:
This page is divided into 5 sections- a smaller image of the item,product name,SKU number, product price and the quantity box selector with respective remove and update links and the subtotal. Should the user want to modify contents of their bag, they can update their order on this page via the quantity selector box using the remove or update buttons. The grand total is shown, along with its delivery charge information (unless user has spent over the free delivery threshold) towards the bottom of the page. The user can also return to the all products page of the site by selecting "Keep Shopping" button, or if they are happy with their bag contents they can follow on with their purchase by selecting the  "Secure Checkout" button.

![image](uximages/bagpageimg.png)
 
### Checkout Page:
 
The checkout page includes forms such as user's name, details of billing and the payment form that is mandatory in order to complete the purchase. Below the credit card form they're yet again informed the total their card will get charged and can proceed to confirm payment or theyare unsure of their payment, they can adjust their bag and return to the shopping bag page by clicking the "adjust bag" button:
 
![image](uximages/checkoutpageimg.png)
 
### Checkout Success Page:
 
Once the purchase is finalised and completed, a success message from bootstrap toasts appears with confirmation that the payment was successfull, along with details of the order number and a confirmation email will be sent to the user. The details of the user's order are shown and a button redirecting to the "new-arrivals" category page is below:
 
![image](uximages/checkoutsuccesspageimg.png)
 

### Contact Page

The contact page is a simple form with 3 text and input and a textarea. The user once submitting the form will be redirected to the contact success page, along with a toast message that they're email was a success and will receive an email from Jerseys for Tims that they will be in contact with the user over their question or concern shortly.

![image](uximages/contactpageimg.png)
 
### FAQs Page:
 
Accessible by clicking "FAQS" from the navbar, the user is redirected to the faq app. There is a series of questions with answers on matters that the user may potentially now have or have in future references. Only the site admin can add/edit/delete faqs. user can also not manually enter the url for the edit/add faqs as they will get instantly get redirected to the sign in page. Some questions and answers were taken from [Your Clothing](https://www.yoursclothing.ie/faq?glCountry=IE&glCurrency=GBP)

![image](uximages/faqpageimg.png)

### FAQ add page 

Only accessible to the admin/superusers to add a faq that may be of a concern to a number of users to the site.

![image](uximages/addfaqpageimg.png)

## FAQ edit page

Editing of a faq is carried out here so that the admin/superuser can edit or delete a faq.

![image](uximages/editfaqpageimg.png)

### Profile Page:
 
This Profile is reachable only to a registered user that is logged in where the user can track their own individual purchases and payments and modify their personal information. Divided into two sections, the first shows the default delivery information of that user and the second section depicts the past orders of that user along with its cost,order number, items bought and the date the payment for the order that was made.

![image](uximages/profilepageimg.png)

 
### Product Management Page
 
Accessible only to site admin or superusers, once logged in they can select "My Account" (dropdown in the navbar) on large and small devices, and from there select Product Management. From here, they can add any new product that fits into one of the categories.

![image](uximages/addproductpageimg.png)
 

### Edit product page

Only accessible to admin and superusers. Editing of products can be achieved here such as its price or rating.

![image](uximages/editproductpageimg.png)
 
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

Having installed Django allauth, respective authentication, registration, account management with bootstrap responsive elements such as toasts, navbar, buttons, links, the pathway to payment for the user was a far less daunting task.
 
## Information Architecture
 
### Database
- SQLlite  was used for local development.
- PostgreSQL was used when deployed through Heroku(Hobby Dev).
 
### Data Modelling
 
- All data related to Products was compiled in a JSON format and is stored in a fixtures folder
- The Data Model below was created using [drawSQL](https://drawsql.app/):
 
![image](uximages/datamodel.png)
 
---
 
## Wireframes
 
see wireframes [here](https://github.com/markgordon22/Jerseys-for-tims/tree/main/wireframes)
 
## Surface
 
### Design
-  #### Colour Scheme
   The color of the site adopted yellow(#ffc107), a lightgrey(#343A40) and white(#ffffff)due to being a attractive array of colors. A decision was made at the start to not use green as a dominant color despite celtic fc that actually play in green kits. My thought though however was since the majority of the jerseys will be green, I turned my back on the idea of incorporating green into the foundation of the website make up to prevent green overflow.[Color-Hex:](https://coolors.co/). I decided to give the contact page and faq page an antique-white background as the form was the only material in the block content so it look very light on content and unattractive since the whole block content was nearly completley white excluding the heading and buttons.
 
   ![image](uximages/coolors.png)
 
### Typography
The font used for the site was [Noto Sans TC
](https://fonts.google.com/specimen/Noto+Sans+TC). A very clear, concise and readable font family from [google fonts](https://fonts.google.com/). Sans serif was used as the back up font in the case that Noto Sans TC did not work.
 
### Imagery

Images for the site were taken from google images.
 
### Icons
The icons used throughout the site are taken from [Font Awesome](https://fontawesome.com/). Particularly for social media icons.
 
 
---
 
# **Technologies used**
 
## **Languages**
 
-   [HTML5](https://en.wikipedia.org/wiki/HTML5): used for creating the structure of the project
-   [CSS3](https://en.wikipedia.org/wiki/CSS): cascading style shhets to style, position create animations.
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript): to make interactivity for elements o site
-   [Python](https://www.python.org/): the backend frameword
 
## **Frameworks, Libraries and Other Sources**
 
- [Balsamiq](https://balsamiq.com/) to make wireframes for site
- [Font Awesome](https://fontawesome.com/)
    - Font awesome used in site to implement icons for atractive visual purposes, boosting user experience. 
- [Git](https://git-scm.com/)
    - for version control with the use of the gitpod terminal to commit to Git and push code to GitHub.
- [GitHub](https://github.com/)
    - used for storage of code after it has been pushed Gitpod terminal.
- [Google Fonts](https://fonts.google.com/)
    - Google fonts were used to import selected font
- [CSS formatter](https://www.cleancss.com/css-beautify/)
    - To beautify css code
- [Javascript formatter](https://beautifier.io/)
    - To beautify javascript code.
- [Heroku](https://dashboard.heroku.com/apps)
    - Heroku is used for deployment of the site.
- [HTML validator](https://validator.w3.org/)
    - testing validator for html code
- [Javascript validator](https://jshint.com/)
    - testing validator for javascript code
- [CSS validator](https://validator.w3.org/) 
    - testing validator for css code
- [pep8 validator](http://pep8online.com/checkresult)
    - testing validator for python code
- [Autoprefixer](https://autoprefixer.github.io/) 
    - to add vendor prefixes to css
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
 
## Responsiveness Testing

Responsiveness of the site was one of the most important aspects to get right for the site. Responsiveness testing was carried out over the course of the devlopment via chrome dev tools.

Results of the responsiveness on dev tool devices are below.

* Moto G4 - Successful
* Iphone 4 - Successful
* Galaxy s5 - Successful
* Pixel 2 - Successful
* Pixel 2 XL - Successful
* Iphone 5/SE - Successful
* Iphone 6/7/8 - Successful
* Iphone 6/7/8 plus - Successful
* Iphone X - Successful
* Ipad - Successful
* Ipad Pro - Successful
* Surface Duo - Successful

Desktop responsiveness - successful


## Usability Testing

* Jerseys for Tims was shared with family, friends, along with my mentor who gave me tips including to start getting the responsiveness for smaller devices working first and working my way up to larger devices.
Getting the site responsive on smaller devices was a challenge, although the responsiveness of the site as I carried on working to get it right on larger devices was significantly easier.

## Lighthouse Testing

Click [here](https://github.com/markgordon22/Jerseys-for-tims/tree/main/testing) for lighthouse test results. The only noticeable cause for concern is the products page on mobile.


## Compatability Testing


| Compatability tests                         | Chrome | Firefox | Edge |
| --------------------------------------------| ------ | ------- | ---- |
| Is the website compatable on these browsers?     |   Yes  |    Yes |  Yes   |



## Bugs

Bugs encountered throughout production.

1. Webhook handlers were an issue throughout production. A series of 400 and 404 errors. With the help of tutor support and the respective documentation given to us to handle such an error this became not a cause for concern anymore.

2. Mobile top header icons were down below the nav toggler and thus demonstrated poor ux. With the help of bootstrap p-0 class there was room for all 3 icons to sit neatly beside the nav toggler and give a better ux.

3. Nav toggler wouldnt turn a white background color. This was a major bug that I kept with me throughout production only to read that the bg-dark bootstrap class was residing. I simply removed the bg-dark class and the nav toggler gave a nice white background color.

4. I thought that I had removed accidentally my category and products models in the admin when gitpod workspaces had shut down for some time(I had not commited the models). It turned I commented out the local_database_url. I uncommented the local dj_database_url and my models were displaying once more.

5. Bootstrap gutters were an issue throughout production. As this applicable when working with bootstrap. I inserted the container class to wrap the row class and this successfully removed the bug.

6. Aws bucket once rendering in the application was giving me incorrect urls to product images. By accident I inserted another folder into the media folder in the bucket rather than copying and pasting the images I wanted for the site. Once I spotted thid mistake I redid the bucket and copied only the files I wanted to render on the site.

7. A regular occurence was the unsuccessful form submissions in production. This was quite apparrent as I was inserting incorrect variables into the urls to passed into the views on the backend. To handle this, I took extra precaution when building my urls to be passed through into the views.

8. Confirmation emails were not being sent to the user once they had made a purchase. With help from Michael at tutor support he saw that my stripe webhook in the heroku configs was not corresponding to the webhook in my stripe account. Once the stripe webhooks matched this bug became a thing of the past and confirmation emails were being successfully sent once a user made a purchase.

## Validation

No errors in html.

![image](testing/htmlvalidator.png)

2 errors in css from the bootstrap cdn which is out of my control to try and fix.

![image](testing/cassvalidator.png)

Javascript

No errors in stripe js

![image](testing/stripejs.png)

No errors in countryfield js

![image](testing/countryfieldjs.png)

Pep 8

![image](testing/pepvalidator.png)
![image](testing/pep2.png)
No errors in views. py

## Test user stories

### First time user stories

"easily navigate around Jerseys for Tims"
- With the use of the navlinks, nav toggler it is simple to be able to navigate around the site and look at items.

"view the site on multiple screen devices and sizes"
- The site has been tested on multiple devices on dev tools so this allows users to the site to view our site on their phone, tablet or desktop devices.

"see different lists of products"
- Below is an image of the lists of products that is on offer at Jerseys for Tims.

![image](userstories/userstory1.png)

![image](userstories/userstory1(2).png)


"see product details/info"
- Once the user clicks on a product that they like on the products page, they can click the product image or the quick view button and they will be redirected to the product details page.

![image](userstories/userstory3.png)


"read company description and the story behind it"
- The user can read about the company, their operations and the people behing Jerseys for Tims

![image](userstories/companyuserstory.png)

"search for product categories"
- The user can search for categories through the select box that is present on every products page regardless of what category it is.

![image](userstories/categoryuserstory.png)


"search for a product by name, category."
- The user can easily search for a product by name/category. Example below is the user is looking for jerseys and has the options of browsing jerseys over the last 4 decades.

![image](userstories/categorybynameuserstory.png)


"view items chosen/selected in my shopping bag"
- User can view items in their bag by clicking on the bag icon on the top right of the screen

![image](userstories/baguserstory.png)

"modify shopping bag contents"
- User can alter the number of items in their bag by clicking either the update or remove links just below the select box.

![image](userstories/alterbagitems.png)

"access contact details of the company"
- The user can get contact details for the company as the company phone number is on the contact page.

![image](userstories/contactuserstory2.png)



"access social media platforms of the company"
- The user can contact the company via there many social media platforms in the footer.

![image](userstories/contactuserstory.png)

"register a user profile account by picking a username, password"
- A new user to the site can register for an account by inserting a username that has not been taken and a password.

![image](userstories/registeruserstory.png)

When the user successfully registers they get brought to this page.

![image](userstories/register(2)userstory.png)

Once they confirm their email address they then get brought to this page.

![image](userstories/register(3).png)

They get asked to sign in and then they are redirected to the home page of the site

![image](userstories/register4.png)


"make purchases as a guest user"
- The user can successfully make purchases even if they dont wish to make an account.

![image](userstories/non-registerreduserstory.png)

Above there are buttons to login into the account or and to register. The user if they wish to can login/register to carry out their payment or should they please, pay for their goods as a guest.

### Registered user stories

"log in and out of my profile"

Below the user can login by clicking the login link in the myaccount dropdown

![image](userstories/loginlogoutuserstory.png)

Then the user can safely logout once they wish to via the myaccount dropdown

![image](userstories/loginlogout(2).png)

"update my personal details"
- The user can update there details in their designated profile below

![image](userstories/profileupdateuserstory.png)

"save my past purchases"
- The user can see there past purchases in their profile

![image](userstories/savepastpurchases.png)

"store my choices in checkout"
- The user can store there past purchases in the checkout and then revert back to the products page to look for other products should they wish to.

![image](userstories/storechoicesincheckout.png)

"Make safe and secure transactions/payments"
- The user can make safe and secure payments. security was 100% a priority in building the site for payments and personal details.

"to be sent confirmation by email of purchases"
- The user will be sent a confirmation email of their order by email

![image](userstories/emailuserstory.png)

### Site owner user stories

"add new items and category listings"
- The site owner can add new items to the site

![image](userstories/additemuserstory.png)

"update items"
- Site owner can update items in the edit product page

![image](userstories/edititem.png)

"remove items"
- Site owner can remove items from site with some defensive programming of a modal to ensure site owner is sure they want to delete the item from the site.

![image](userstories/removeitem.png)

"view and manage users of Jerseys for Tims"
- site owner can revert to the site admin to manage and keep an eye on orders.

![image](userstories/manageordersuserstory.png)

"Continually update/modify faqs so users won't have to wait for responses from Jerseys for Tims on their concerns"
- Site owner can modify site faqs only as displayed here2

![image](userstories/managefaq.png)


## Manual testing

Home page

All links work and navigate to their correct destination. Hero image is responsive, as well as the navbar, footer, delivery banner and navbar icons and social media icons.

Products page

The products page is responsive. All items render the price, buttons, rating and category of product. Quick view button navigates to the product details pafe as per intended.

About page

Text is displaying correctly, as well as base template features.
Founder images are responsive.

Contact page

Form is responsive, Confirmation email is being successfully sent to the user as seen in the user story above. Buttons are operating correctly.

Faq page

Page renders all model content. Buttons are successfully only displaying on the site admin so only the site admin/owner can modify them.

Product detail page

Displaying all content of buttons, product description and edit and delete buttons for site owner in case they want to remove/update the item. All base template features are working correctly.

Register page

Form is rendering as per intended. Buttons redirect users to their correct destination and hero image is working as per intended along with all the base template features.

Login page

Form is rendering as per intended. Buttons redirect users to their correct destination and hero image is working as per intended along with all the base template features.

Profile page

User profile successfully saves all user's data and past orders. Base template features are responsive and rendering correct size/height as per device.

Faq edit/add page

Both pages work just fine. Base template features are responsive and rendering correct size/height. Site owner can easily update/remove/add faq should they wish.

--The search bar in the navbar--

The user can search for a product should they want to in the search bar. The backend code is working in regards to that the product name and description once entered in the bar will render any related products.

--Select box--

The select correctly adjust the search criteria for the users demands for all aspects such as highest rated products and cheapest products.

-- The bag icon--

Once clicked will correctly lead the user to their individual bag with their items that they have selected. If user clicks the bag icon but they have not put any items in the bag, then the else block will be fired "you have no items in your bag" with the button to redirect the user back to the products page.

-- Payments --

Payments have been tested and user will be successfully redirected back to the checkout success page with a receipt of their purchase.
The payments were carried out with stripe with code courtesy of boutique ado.

--- Email to confirm proof of identity upon registering an account -- 

The user once registering an account will be redirected to a page that gets them to go to their email and confirm their identity. Once this has been done, then the user is free to roam the site.

I used a fake email address from [temp.org](https://temp-mail.org/en/view/6121e4bd814d68007593ab80) to test this.

![image](testing/tempmail1.png)

Once successfully passed registration the user will be asked to go too their email to confirm their identity.

![image](testing/tempmail2.png)

Then the user can simpy click to confirm in their email

![image](testing/tempmail3.png)

Then the user can confirm by clicking confirm on the site.

![image](testing/tempmail4.png)

the user has now registered an account

---social media links--

links users to the social media platforms to the company

- facebook

- instagram

- youtube

- linkedinn

- Twitter

All social media links work accordingly.

## Crud testing

### Create product

Site owner can add a new product to the store by going into the myaccount dropdown and clicking product management from there the site owner will be greeted with this page.

![image](userstories/crudtesting.png)

The user can now go and add a product like so

![image](userstories/addproduct.png)

The site owner will now be redirected to the product detail page with the new product.

![image](userstories/addproductcrudtesting.png)

The site owner has created added a product and should they wish they can edit the product on the dit product page via the edit link like so

![image](userstories/editproductcrudtesting.png)

You can see below that the name and description of the product has been edited/updated.

![image](userstories/updatedproductcrudtesting.png)

The site owner should they wish can delete the product by clicking the delete link where they will be given this model clarifying to the site owner that they are sure of deleting the product as it will removed indefintley

![image](userstories/deleteproduct.png)

The product has now been removed.

![image](userstories/deletedproductcrustesting.png)

### Create faq

The site owner can add faqs to the faq page by clicking the faqs page from the about us dropdown.

![image](userstories/addfaq.png)

The user can get to the add faq page by clicking the add button
where they will see this below

![image](userstories/addfaq2.png)

The site owner can now add an faq

![image](userstories/addfaq3.png)

The site owner has successfully added an faq

![image](userstories/editfaqcrustesting.png)

The edited faq can be seen above.

The site owner can now delete the faq by clicking the delete button.
where a model will render asking the site owner are they sure they want to delete the faq.

![image](userstories/editfaqcrustesting2.png)

The site owner once sure they want to delete the faq can click delete and the faq will be removed.

![image](userstories/editfaq3.png)

## Test stripe payments

In order to make sure the Stripe payments were operating as per intended, I had to make sure the test webhooks were working, I had to make sure the correct endpoint was added:

----https://jerseys-for-tims.herokuapp.com/checkout/wh/----

Testing for stripe webhook success involved the respective url, email confirmation and image receipt on the checkout success page.

Payment was a success

![image](userstories/teststripe1.png)

Email receipt

![image](userstories/teststripe2.png)

Webhook success

![image](userstories/teststripe3.png)

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
to settings .py.
 
20. Addition of Stripe env variables to settings .py.
 
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
 
After you have endured the relevant required package are installed you should then
 
Make migrations with
```
python3 manage.py makemigrations
 
```
Then run the following command to ensure the database is created
```
python3 manage.py migrate
 
```
 
Load the fixtures from the 'products.json' - which are contained in the 'fixtures' folder into the database.
This is done by using the following command:
```
   python3 manage.py loaddata <file name>
```
 
Make your own superuser with: ```python3 manage.py createsuperuser``` and make your own username and password .
 
Run your own app with:
```python3 manage.py runserver```
 
 
### **Credits**
 
**Code:**
- The walkthrough project in the Full Stack Frameworks with Django Module, Boutique Ado, this was core template to get the javascript working correctly for the site as well as the views in the backend. It was the primary source and guide when it came to building Jerseys for Tims. This was a template for me to build my own faq and contact apps.

- For the contact app I followed [Twilio](https://www.twilio.com/blog/build-contact-form-python-django-twilio-sendgrid)
- To render the scroll back to top arrow on the about page and products pages I used code from [W3 schools](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp)
- [Bootstrap](https://getbootstrap.com/docs/5.0/forms/layout/) used to make footer, navbar, cards, toasts, cards, images,links and buttons.
- [Stackoverflow](https://stackoverflow.com/questions/55227106/css-animation-text-sliding-left-to-right) for help on how to make the scroll text animation on the delivery banner
- [Django Docs](https://django-book.readthedocs.io/en/latest/chapter14.html) was a guide used to look over elements such as django imports, models and admin panels.
- Credit to the [Structure for this Readme](https://github.com/elerel/ms4-siopa-fia)
- Fade-in text on home page from [stackoverflow](https://stackoverflow.com/questions/11679567/using-css-for-a-fade-in-effect-on-page-load)
 
**Content:**
- [Yours Clothing](https://www.yoursclothing.ie/faq?glCountry=IE&glCurrency=GBP) was used to generate some sample faqs.
- All jerseys descriptions were written by me as Ive grown up watching celtic and knowing the different jerseys used over the past years and the players that have worn them.
 
**Media:**
- All images were taken from Google images.

### **Disclaimer**
All content on this site is for educational purposes solely.
 
### **Acknowledgements**
- My thanks to my mentor [**Rohit Sharma**] for his time and support during the throughout the course of being my mentor and a guide, the ever selfless Slack Community, CI tutor support (my special thanks to Scott, Igor, John, Sheryl and Michael!) but without [Chris Z's](https://github.com/ckz8780) excellent explaination throughout the walkthrough project, it would not have been possible

- A big Thanks aswell to my family for their continued support.
 
 
##### [Back to Contents](#contents)
