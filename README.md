# DIU Counseling Management System (DIUCMS)

## Table of contents
* [Introduction](#introduction)
* [Status](#status)
* [Technologies](#technologies)
* [Setup](#setup)
* [Contribution](#contribution)
* [Contributors](#contributors)

## Introduction
This project, DIUCMS (DIU Counseling Management System), is a Django-based web application for managing counseling sessions. The project includes a superuser account for administrative purposes and uses PostgreSQL as the database.

## Status

![Static Badge](https://img.shields.io/badge/Repo%20Size-12.16%20MB-brightgreen)
![Static Badge](https://img.shields.io/badge/License-CC%20BY%20NC%204.0-blue)
![GitHub Repo stars](https://img.shields.io/github/stars/ishan-nahid/diu__cms)


## Technologies

| <p align="center">Front End</p> | <p align="center">Back End</p> | <p align="center">Databse</p>
| :------------- | :-------------: | -------------: |
| ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) | ![DJANGO](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) | ![POSTGRESQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) | 

## Setup
1. Initialize the virtual environment:
   ```
   python -m venv virtenv
   ```
2. Activate the virtual environment: 
   - On Windows:
   ```
   virtenv\Scripts\activate.bat
   ```
   - On macOS/Linux:
   ```
   source virtenv/bin/activate
   ```

3. Install Django and other required packages:
   ```
   pip install -r requirements.txt
   ```
4. Navigate to the project folder:
   ```
   cd diucms
   ```

5. Make sure to setup database
   ```
   "NAME": "diucmsdb",
   "HOST": "localhost",
   "PORT": "5432",
   ```
6. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
7. Start the development server:
   ```
   python manage.py runserver
   ```
  

## Contribution:
- Fork the repo to your Github.<br/>

- Clone the Forked Repository to your local machine.
	```
	git clone https://github.com/<username>/diu_cms
	```
- Change the directory to diucms (if not in it).
	```
	cd diucms
	```
- Add remote to the Original Repository.
	```
	git remote add upstream https://github.com/ishan-nahid/diu_cms
	```
- Check the remotes for this repository.
        ```
        git remote -v
        ```
- Always take a pull from the upstream repository to your master branch to keep it at par with the main project(updated repository).
        ```
        git pull upstream main
        ```
- Create a new branch.
        ```
        git checkout -b <your_branch_name>
        ```
- Perform your desired changes to the code base.
- Track your changes:heavy_check_mark: .
        ```
        git add . 
        ```
- Commit your changes .
        ```
        git commit -m "Relevant message"
        ```
- Push the committed changes in your feature branch to your remote repo.
        ```
        git push -u origin <your_branch_name>
        ```
- To create a pull request, click on `compare and pull requests`. Please ensure you compare your feature branch to the desired branch of the repository you are supposed to make a PR to.

- Add appropriate title and description to your pull request explaining your changes and efforts done.


- Click on `Create Pull Request`.


- Voila! You have made a PR to this repo. Sit back patiently and relax while your PR is reviewed


<!--
## Contributors
<div>
<h1 align="center">
 <b>Thanks to these amazing people
<h1>
<a href="https://github.com/ishan-nahid/diu_cms/contributors">
  <img src="https://contrib.rocks/image?repo=ishan-nahid/diu_cms&&max=817" />
</a>
</div>	-->

## Contributors
<!-- [![contributors](https://contrib.rocks/image?repo=ishan-nahid/diu_cms)](https://github.com/ishan-nahid/diu_cms/graphs/contributors) -->
<!-- [![](https://opencollective.com/ishan-nahid/diu_cms/contributors.svg?width=890&button=false)](https://github.com/ishan-nahid/diu_cms/graphs/contributors) -->
[![ISHAN AHMAD](https://github.com/ishan-nahid.png?size=70)](https://github.com/ishan-nahid)
[![ATIQUE SHAHRIAR](https://github.com/atiqueshahriar.png?size=70)](https://github.com/atiqueshahriar)
[![Faiyaz Rafid](https://github.com/faiyaz666.png?size=70)](https://github.com/faiyaz666)
[![MK Rashmi](https://github.com/mahjabin-rashmi.png?size=70)](https://github.com/mahjabin-rashmi)
[![Shreya](https://github.com/shreya-14489.png?size=70)](https://github.com/shreya-14489)


##

<div align="center">
   <h3>Show some ❤️ by starring this awesome repository!</h3>
</div>
