# Company Project Management System

An app that helps a company to manage its different projects and inventory.


## Table of Contents
- [Purpose](#purpose)
- [Technologies and Libraries Used](#technologies-and-libraries-used)
- [Setup](#setup)
- [Usage](#usage)


## Purpose
I created this app to help small businesses around me in managing their projects and inventory. I wanted to create an app with a simple form of password protection that is not too complex and can be easily utilized. I also wanted to ensure that a user-friendly aspect was incorporated and thus I used the Tkinter library to achieve that by creating a graphical user interface.


## Technologies and Libraries Used
- Programming Languages
    - Python
- Libraries
    - tkinter
    - sqlite3
    - datetime
    - ttkthemes


## Setup
Make sure to git clone this repository. After cloning, ensure the latest version of Python and all mentioned packages are installed and the project is ready for use!


## Usage
To run the program, run the Main_Page.py file. This will open up the GUI. To use the application, follow the steps below:

<details>
    <summary>
        Click to expand
    </summary>

<br>

- On the main page, enter the password and click on the login button. If the password is correct, the member portal will open up. If the password is incorrect, an error message will pop up.
- In order to add a new member (username and password), the client can change the variables (list_usernames and list_passwords) in the Main_Page.py file.

<kbd><img src="readme_docs/pic1.PNG" width="400"></kbd>

<br>

- In the member portal, the members of the company can add new projects, view existing projects, add new inventory, view existing inventory, and view the company's About page.

<kbd><img src="readme_docs/pic2.PNG" width="400"></kbd>

<br>

- In order to view projects, the user can click on the view projects button. This will open up a new window that will display all the projects in the database which includes the list of teams and inventory used in the project.

<kbd><img src="readme_docs/pic3.PNG" width="600"></kbd>

<br>

- From there the user can view, add and delete a project.

<kbd><img src="readme_docs/pic4.PNG" width="600"></kbd>

<br>

- The members of the company can view more information by pressing the About Us option on the member portal.

<kbd><img src="readme_docs/pic5.PNG" width="400"></kbd>

</details>
