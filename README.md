# DIU Counseling Management System (DIUCMS)

## Table of contents
* [Introduction](#introduction)
* [Status](#status)
* [Technologies](#technologies)
* [Setup](#setup)
* [Contribution](#contribution)

## Introduction
This project, DIUCMS (DIU Counseling Management System), is a Django-based web application for managing counseling sessions. The project includes a superuser account for administrative purposes and uses PostgreSQL as the database.

## Status

## Technologies

| <p align="center">Front End</p> | <p align="center">Back End</p> | <p align="center">Databse</p>
| :------------- | :-------------: | -------------: |
| ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) | ![DJANGO](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) | ![POSTGRESQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) | 

## Project Setup
1. Initialize the virtual environment:
   ```bash
   python -m venv virtenv
   ```
2. Activate the virtual environment: 
   - On Windows:
   ```bash
   virtenv\Scripts\activate.bat
   ```
   - On macOS/Linux:
   ```bash
   source virtenv/bin/activate
   ```

3. Install Django and other required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Navigate to the project folder:
   ```bash
   cd diucms
   ```
5. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```
  






<div align="center">
<h3>Show some ❤️ by starring this awesome repository!</h3>
</div>
