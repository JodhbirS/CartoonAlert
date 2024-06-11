# Cartoon Alert System

## Overview

The **Cartoon Alert System** is a web application that monitors Patrick Corrigan's website for new cartoon updates and sends alerts to subscribed users via SMS. This project uses Python for the backend, with a combination of Flask for the web interface, Redis for data storage, and the Twilio API for sending SMS notifications. The application also includes a cron job that runs daily to check for new cartoons and notify users.

## Features

- **User Subscription**: Users can subscribe to receive SMS notifications for new cartoon updates by providing their phone numbers.
- **Daily Check**: A cron job runs daily to check for new cartoon updates on the specified website.
- **SMS Notifications**: Users receive an SMS notification whenever a new cartoon is detected.
- **Data Storage**: User phone numbers and other data are stored securely in Redis.

## Technologies Used

- **Python**: Backend language.
- **Flask**: Web framework for the application.
- **Redis**: In-memory data structure store for storing user data.
- **Twilio API**: For sending SMS notifications.
- **GitHub Actions**: For running the daily cron job.
- **BeautifulSoup**: For web scraping to detect new cartoons.
- **Vercel**: For deployment.
