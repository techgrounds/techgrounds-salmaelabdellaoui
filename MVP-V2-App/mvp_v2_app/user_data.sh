       
#!/bin/bash
# perform a quick software update on instance
sudo dnf update -y
# install the latest versions of Apache web server and PHP packages for AL2023
sudo dnf install -y httpd wget php-fpm php-mysqli php-json php php-devel
# Download Lab files
sudo wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip
sudo unzip lab-app.zip -d /var/www/html/
# Turn on web server
sudo chkconfig httpd on
sudo service httpd start





   
       
       
       
       
       
