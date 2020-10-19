<p align="center">
 
  <h2 align="center"><strong>PREMIUM BUSINESS DIRECTORY</strong></h2>

  <p align="center">
    A BUSINESS DIRECTORY WITH PAID LISTINGS
  </p>

## Welcome

## Table of Contents

* [About the Project](#about-the-project)
* [User Experience](#user-experience)
* [Inspiration](#inspiration)
* [Testing](#testing)
* [Wireframes](#wireframes)
* [Future Development](#future-development)
* [Technologies](#technologies)
* [Author](#author)

## Welcome

## About the Project
The objective of this project is to create a Business Directory for B2B (*business to business*) and B2C (*business to consumer*) purposes. Users can buy a listing by paying for it using a credit card function on the website (see user stories below).
The directory could be added to with many directories but there are some there for the moment in order that people can get a feel of how the site works.


## User Experience (UX)

- ### User stories
As a consumer, I want to a place to search for businesses and products. It should be easy to find products and services by entering a search term.
As a consumer, I want to be able to filter the entries so that I can find the best results based on the type of thing that I am searching for and where I am located.

As a business, I want to create an entry on a business directory to display my business to attract new clients. It should be easy and fast to create an account and be able to fill in the details of the businesses.
As a business, I want to be able to easily edit the account or, if need be, delete the account.

- ### User Experience
It should be easy to search for a product or a service in a search bar on the home page.
It should be easy to filter the entries by various criteria such as business type, business category, etc.
It should be easy to navigate around the website to move from entry to entry and to return to the home page.
The information in the entries should be clearly laid out and easy to read.

- ### Design
    - #### Colour Scheme
    This website is based on the Boutique Ado website. The style is clear - stark even - and easy on the eye. Strong colours of white, red, and black are used throughout in order to make it clear and easy to use. In some areas of the website, colours offer guidance about what the functions will do. In the case of Delete a listing, the fact that it is in red indicates that it is a serious option to choose and should be approached with caution.

    - #### Imagery
    The image on the home page is of the Grand Canal dock area in Dublin. It shows the modern architecture and urban landscape in an area of the city that is full of leading international companies. I felt that this image would be a nice introduction to the website as well as giving a hint of a place that professionals would want to use when searching for a business online.

## Inspiration
I was inspired to make the business directory as I came across a business directory that was very clumsy and shoddy in the way that it was designed. I particularly like the [Manta business directory](http://www.manta.com).

## Testing
The testing consisted of the following areas:
 - (i) Registration and logging in
 - (ii) Adding a listing
 - (iii) Stripe testing
 - (iv) Deployment

 (i) Registration and logging in

 Users need to be able to register a new account and sign in and out. This was tried and tested with various real and fake e-mail addresses. It works.
 
 (ii) Adding a listing

 When users sign in, they are presented with a Create Listing page where they can fill out a form to create a listing in directory. The form is easy to use and it allows the business owner lots of space in the text area to describe their business in their own words.
 
 (iii) Stripe testing

Setting up the Stripe payment system involved a large amount of work and testing. It was found that the CSS of Stripe and the project were at odds with each other so the best thing was to change the Stripe system so that it would redirect the paying user to Stripe's own checkout page in order to complete the transaction and, once complete, the user would be returned to the listings' page. This is painless for the user and does not cause confusion or delay. Whilst trying the approach of embedding the Stripe payment form in the page, it caused too much technical problems and was not viable as an option. Stripe is to be commended for allowing such a seamless transition from one site to their own checkout page and then a seamless return to the original site. 
 
 (iv) Deployment Testing

It was recommended to use Heroku and AWS to deploy and host the project. Having tried to deploy to Heroku, it would not work as it claims to work. Heroku is excrebable as a means to deploy this project. It never worked the way that it should have and is best to be avoided. The static and media files would not show up from AWS. This is infuriating as the keys and code were correct. The rough solution for that was to use inline CSS styling and to provide a direct link to the image that is the background on the home page. AWS's poor performance meant that it was rejected as a means of hosting.
In this [article about Django hosting](https://www.hostingadvice.com/how-to/best-django-hosting/), the author wrote "_The big three cloud providers — Amazon Web Services, Microsoft Azure, and Google Cloud — all support robust Django development, but we tend to reserve those platforms for experienced developers with enterprise-grade hosting requirements._" This project is far from needing enterprise-grade hosting requirements and I, as a developer, am far from being an experienced developer, so I prefer something that works easily and requires less of a learning curve to set it up and maintain it.
I also tried www.pythonanywhere.com but this did not meet my expectations despite initially looking promising. That is why I chose to buy a cheap URL www.premiumbd.site and use private hosting which is a much better way to host a website like this. Everything is hosted in the one location and there is no reliance on various platforms to make it function properly.

## Wireframes
See the wireframes in the Github folders.

## Future Development
The current website, as is stands, is to represent how a directory would function. The plan for future development is to add to the website and the directory so that it has more functions such being able to add photographs to the listings, being able to pay for a premium listing on the home page, more categories and filters so that users can search more to find their desired business. Users would be able to navigate the website better with buttons in order to move listings.

## Technologies

#Languages used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)

The technologies that the site was built and designed with are:

[Django](https://www.djangoproject.com/) - used to create the database of the website.

[Balsamiq](https://www.balsamiq.com/) - used to make the wireframes for the pages.

[JSON Editor Online](http://jsoneditoronline.org/) - this tool was used to format the JSON files.

[Github](https.github.com) - used to store and share the project.

[Gitpod](https://www.gitpod.io/) - used to design and upload the wepages to Github.com.

[Google Fonts](https://fonts.google.com/) - used to provide the Lato font for the website.

[Fontawesome Icons](https://fontawesome.com/v4.7.0/icons/) - used to provide some icons to make the site prettier.

[HTML Formatter](https://webformatter.com/) - used to correct the indentation of the html files.

[LightShot](https://app.prntscr.com/en/index.html) - used to make the images taken from the webpages.

[Stripe](https.stripe.com) - used to process payments on the website.

[Rose Hosting](https://www.rosehosting.com/) - the hosting company that hosts the website.

[GoDaddy](https://www.godaddy.ie/) - the domain company used to buy www.premiumbd.site from.

[Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) - used to generate a secret key for Django.

[Temp Mail](https://temp-mail.org/) - used to generate a temporary e-mail address in order to begin using Stripe.

[Gmail](https://mail.google.com/) - used to set up an e-mail system to aid account creation on the website.

Code for Django Phone Field
https://pypi.org/project/django-phone-field/


## Author
Seanán Ó Coistín