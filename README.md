<h1 align="center">Pizza Heaven - Resturant Booking</h1>

[View the live project here.](https://resturant-booking-p4.herokuapp.com/)

This is the official page for Pizza Heaven. It is designed to be responsive and accessible on a range of devices, making it easy to navigate.
The booking system offers a staff user to see the bookings in the databse, via the admin page. And customers can place new booking with date, time, and number of people. They also have to incude an email address. For the production environment, the send mail function is not activated, but it's implemented.

<h2 align="center">
    <img src="assets/images/screenshots/devices/frontpage.JPG">
</h2>

## User Experience (UX)
-   ### User stories

    -   #### Resturant Booking - Staff

        1. As a booking responsible for the resturant, I want to be able to see all the customers bookings time and date, and number of people in each booking, so that i can prepare the resturant in time.

    -   #### esturant Booking - Customer

        1. As a customer, I want to be able to book a table for a specific data and time in the resturant, so that I can get a booking confirmation on my email.


-   ### Design
    -   #### Colour Scheme
        -   The three main colours used are cyan darken-4, white, and black. The css uses the materializecss css library.
    -   #### Typography
        -   Uses the materializecss standard fonts.
    -   #### Imagery
        -   Theres one image, background image for all pages, this is an illustrative image of an italian pizza.

        #### Media
        -  There are no particular media elements.

        #### Social Media
        -  The footer has all social media links with icons making it easy for the user to click
        and follow. There is no added links to these, because this is a fictive site. But the icons are taken 
        from fontawesome cdn. See base.html.
    <h2 id="wireframes"></h2>
-   ### Wireframes/Mockup
-   There are no wireframes for this webpage




## Features

-   Fully interactive booking form, submitting the booking request to the heroku postgresql server. 

-   The booking form has input validation, and has included date and time pickers from the materializecss library.

-   The user will be greeted with a booking confirmation if succesfully added to the database, this page also renders the 
    booking details back to the user.

-   Staff people for the resturant can login to the database to see the bookings, and do changes if necessary. The staff can login
    to django admin by adding "/admin" to the url, and login with user: staff, pass: staff.

-   The about and menu/booking sites is just fictive and illustrative for demonstration purposes only.

-   The navbar is responsive, and uses side-nav functionality from materializecss during resizing to mobile/tablet devices.

<h2 align="center">
    <img src="assets/images/screenshots/contact/contact-pre.JPG">
    <img src="assets/images/screenshots/contact/contact-after.JPG">
</h2>

<h2 align="center">
    <img src="assets/images/screenshots/devices/ipad-pro-about.JPG">
    <img src="assets/images/screenshots/devices/ipad-pro-music.JPG">
</h2>


## Features to be added/fixed
-   Make images under “About” section smaller, becomes too big on desktop.
-   Make the social media links more accesible.
-   Indicate on the cover arts that they are clickable.
-   When cover art is clicked, add a selection dialogue for the user to select preferred platform.
-   Add more songs and videos to “Music” section
-   Add more items for purchase, then add another section called “store”.
-   Add funding/support option for volunteers/fans.
-   Add calendar with live shows, own section.
-   Add artistic animation to give the page a more dynamic feel.
-   Add scrolling hint, so that the user is informed the webpage has more content and need to be scrolled.

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://www.javascript.com/about)

### Frameworks, Libraries & Programs Used
1. [EmailJs](https://www.emailjs.com/)
    -EmailJs was used for interactivity on the contact form. Specifically to forward the contact form when submitted to a real email address.
    Also to genereate auto replies back to the sender when contact form was submitted.
1. [Hover.css:](https://ianlunn.github.io/Hover/)
    - Hover.css was used on the navigation menu.
11. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [GitPod:](https://gitpod.io/)
    - GitPod is used as the IDE for the project.
1. [Figma:](https://figma.com/)
    - Figma was used to create the [wireframes](#wireframes) during the design process.
1. [Chrome-DevTools:](https://developer.chrome.com/docs/devtools/)
    - Chrome DevTools was used to test responsiveness on all devices,to inspect html/css, and to debug the application.
1.  [Am I Responsive?](http://ami.responsivedesign.is/)
    - Am I Responsive? was used to create the screenshot of the website for all devices, the first image of the README.



## Testing

The W3C Markup Validator, W3C CSS Validator, and JSHint JavaScript Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](assets/validation/html-val.JPG)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](assets/validation/css-val.JPG)
-   [JSHint JavaScript Validator](https://jshint.com/) - [Results](assets/validation/jshint.JPG)

### Testing User Stories from User Experience (UX) Section

-   #### New potential/existing fan

    1. I want to easily and efficiently follow the artist by accessing the social media links.
        1. The user can easally access the artists social media in the footer. However this can be enhanced, because you have to scroll all the way down to the bottom of the page.
    2. I want to easily and efficiently learn more about the artist.
        1. The user can easily and efficiently learn more about the artist by selecting "About" from the navigation menu, or by scrolling half page.
    3. I want to easily and efficiently browse and/or purchase the artist's contents.
        1. The user can easily and efficiently  browse and/or purchase content from the "Music" section, either by scrolling or by selecting "Music" from the navigation.
    4. I want to easily and efficiently get in touch with the artist for booking inqueries.
        1. The user can easily and efficiently get in touch with the artist by selecting "Contact" from the navigation menu, or by scrolling down to the bottom of the page.

-   #### New potential business person

    1. I want to easily and efficiently follow the artist by accessing the social media links.
        1. The user can easally access the artists social media in the footer. However this can be enhanced, because you have to scroll all the way down to the bottom of the page.
    2. I want to easily and efficiently learn more about the artist.
        1. The user can easily and efficiently learn more about the artist by selecting "About" from the navigation menu, or by scrolling half page.
    3. I want to easily and efficiently browse the artist's contents.
        1. The user can easily and efficiently  browse content from the "Music" section, either by scrolling or by selecting "Music" from the navigation.
    4. I want to easily and efficiently get in touch with the artist for business inqueries.
        1. The user can easily and efficiently get in touch with the artist by selecting "Contact" from the navigation menu, or by scrolling down to the bottom of the page.
 
### Further Testing

-   The Website was tested on Google Chrome, Vivaldi, Microsoft-Edge, Internet Explorer and Firefox .
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone10 X, Huawei P20 Pro, iPhone5, iPad and iPad pro.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-   During test sessions, it was observed that the "home button", which is the artist logo in the top left, was not taking the page back to top. This was observed on chrome, but saw it rarely.

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/nno24/javascript-p02)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com/nno24/javascript-p02) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/nno24/javascript-p02)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/nno24/javascript-p02)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/nno24/javascript-p02
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/nno24/javascript-p02
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits
1. Nikolay Cranner's artwork and media/music.
2. Friends and family for critical feedback during review.
3. Coding ideas on how to validate input fields for the contact form [here](https://www.w3schools.com/js/js_validation.asp)

### Code

-   The about pictures of the artist came from [Instagram](https://www.instagram.com/nikolay_cranner/)

-   The embedded videos came from [Youtube](https://www.youtube.com/channel/UC5ntUYnW40FCXeuowJYUOPw)

-   The embedded music for purchase came from [Beatport](https://www.beatport.com/artist/nikolay-cranner/709007)

-   The embedded music for streaming came from [Spotify](https://open.spotify.com/artist/4NvkvOJ0mDM7QjdzOZLDRd?si=QshNNTHJQRab-LCm2i6Osw&dl_branch=1)

### Content

-   All content was written by the developer.

### Media

- Proprietary images and logo was used with acceptance from Nikolay Cranner.

### Acknowledgements

-   My Mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/?originalSubdomain=ng) for continuous helpful feedback.

-   Tutor support at Code Institute for their support.
