# Feedback Form Flask App

[![Demo](https://img.shields.io/badge/Demo-Feedback%20Form%20App-blue)](https://feedbackform-flask-app.onrender.com/) [![GitHub Repo](https://img.shields.io/badge/GitHub%20Repo-FeedbackForm--Flask--App-red)](https://github.com/PrathameshDhande22/FeedbackForm-Flask-App)

The Feedback Form Flask App is a web application built with Python, Flask, Pandas, and MongoDB. It allows users to fill out a form and provide feedback on a particular product. The form consists of 5 questions related to the product.


The website is made responsive using Bootstrap and includes some additional JavaScript functionalities.

## Screenshots 
- Home Page
![HomePage](/images/img1.png)

- Feedback Form Page
![Feedback](/images/img2.png)

- About Page
![About](/images/img3.png) 

## Installation

To run the Feedback Form Flask App locally, follow these steps:

1. Create a virtual environment for the project.

```
pip install virtualenv
virtualenv venv
```

2. Install the required dependencies using the following command:
```
pip install -r requirements.txt
```

3. Set up the `.env` file located in the `feedback` folder and add the following variables:

```
MONGODB=<MongoDB_URI>
SECRETKEY=<Flask_Secret_Key>
```
Replace `<MongoDB_URI>` with your MongoDB connection string and `<Flask_Secret_Key>` with a secret key of your choice.

## Usage

To run the app, use the following command:

```
python3 run.py
```

Access the app in your browser at `http://localhost:5000`.

## Generating CSV File

After users fill out the feedback form, their responses are stored in the MongoDB database. You can download a CSV file containing all the users' data from the app.

## Contributions

Contributions to the project are welcome! Feel free to submit pull requests.

## Support

If you have any questions or need assistance, please reach out to us.
OR
[Email](mailto:prathameshdhande534@gmail.com)

## Acknowledgements

We would like to acknowledge the following open source projects for their valuable contributions:

- [Flask](https://flask.palletsprojects.com/) - Web development framework
- [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis
- [MongoDB](https://www.mongodb.com/) - NoSQL database

## Links

- [Demo](https://feedbackform-flask-app.onrender.com/)
- [GitHub Repo](https://github.com/PrathameshDhande22/FeedbackForm-Flask-App)


## Author : Prathamesh Dhande
