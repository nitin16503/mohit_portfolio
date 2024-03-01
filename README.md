# Deploying Python Portfolio on AWS EC2

### Set up an AWS EC2 instance

1. Create an IAM user & login to your AWS Console
    - Access Type - Password
    - Permissions - Admin
2. Create an EC2 instance
    - Select an OS image - Ubuntu
    - Create a new key pair & download `.pem` file
    - Instance type - t2.micro
3. Connecting to the instance using ssh
```
ssh -i instance.pem ubunutu@<IP_ADDRESS>
```
### Configuring Ubuntu on remote VM

1. Updating the outdated packages and dependencies
```
sudo apt update
```
2. Install Git
```
sudo apt install git
```
3. Install Python3
```
sudo apt install python3
```
### Deploying the project on AWS
1. Clone this project in the remote VM
```
git clone https://github.com/mohitsharma012/mohitji.git
```
2. Install Django 
```
pip install django 
```
3. Install Requirements file
```
pip install -r requirements.txt 
```

4. Start the project in Devlopment Server
```
python manage.py run server 0.0.0.0:8000
```
> NOTE - We will have to edit the inbound rules in the security group of our EC2, in order to allow traffic from our particular port

> NOTE - Devlopment server is genrally use for testing application. Once you shut down the terminal your application stop working.
> So we will use Gunicorn for Production Server. 

#### Run project in Production Server
1. Install Gunicorn
```
sudo apt install gunicorn
```
2.  Start the project in Production Server
```
gunicorn mohitji.wsgi
gunicorn mohitji.wsgi:application --bind 0.0.0.0:8000
```
> Note - It will run even after your terminal is closed.


## Project is deployed on AWS 🎉😊
