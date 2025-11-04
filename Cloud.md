
[Back to HadCM3_technical_notes](HadCM3_technical_notes.md)

# Cloud Services

These are instructions for how to set up the VPS (virtual private server) for [https://data.deepmip.org](https://data.deepmip.org) , but will be useful to anyone setting up cloud services.

(1) In order to pay for cloud services with corporate credit card, need this category (0005 - telecommunications services, or maybe 4816) to be unlocked on the card.  Contact corporate-cloud mailbox, and IT services.  

(2) Need to have a cloud provider.  We will rent a VPS (virtual private server).  Seb uses ovhcloud. Another option is microsoft azure.  [https://ovcloud.com](https://ovhcloud.com) .  Go to "Bare Metal and VPS / VPS / Configure your VPS".  I went for VPS-1 (8GB RAM (smallest size available, sufficient for data.deepmip.org), and Ubuntu (same as Seb).  12 months.  France (Gravelines).  £48.96.  Made an ovh account.

(3) go to ovh.com, log in, and go to "Dashboard".  Click on your new VPS.  Also click on "getting started".  

(4) You will receive an email with login details, e.g.:
our VPS name is: vps-b97454e8.vps.ovh.net  
  - IPv4 address: 37.59.98.55  
  - IPv6 address: 2001:41d0:305:2100::b644  
  - Username:  ubuntu
and a link to reset your password.

(5) Log in using e.g. `ssh ubuntu@37.59.98.55`

(6) reset your password

(7) Have a beer.

(8) This is the big bit..... 

```
sudo apt update
sudo apt upgrade
sudo reboot
```
```
sudo adduser deepmip-app
sudo usermod -aG sudo deepmip-app
```

Create key-pairs etc so log in from another machine
`ssh-copy-id deepmip-app@VPS-IP`

Traffic limiting:
```
sudo ufw allow OpenSSH
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

`nslookup data.deepmip.org`  

load docker:
follow instructions here: [https://docs.docker.com/engine/install/ubuntu](https://docs.docker.com/engine/install/ubuntu)  
(1) `for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done`  
(2) text from "Set up Docker's apt repository"  
(3) `sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`

Now we can actualyl start the app:  
`sudo docker run -p 8501:8501 sebsteinig/deepmip-eocene-app:latest`

You can now view your Streamlit app in your browser:  
URL: http://37.59.98.55:8501

------

Now needs a web server (engine-x)  
`sudo apt install -y nginx`

```
sudo vi /etc/nginx/sites-available/data.deepmip.org
server {
    listen 80;
    server_name data.deepmip.org;
 
    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 86400;
    }
}
```
replaced data.deepmip.org to 37.59.98.55 (will change back later).

```
sudo ln -s /etc/nginx/sites-available/data.deepmip.org /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl reload nginx
```

`sudo docker run -p 8501:8501 sebsteinig/deepmip-eocene-app:latest`

Now, browser http://37.59.98.55/ works!  Have removed need for :8501

enable Docker to start on boot  
`sudo systemctl enable docker`
 
remove any existing container (if it exists)  
`sudo docker rm -f deepmip-app`
 
run the container in detached mode with restart policy  
```
sudo docker run -d \
  --name deepmip-app \
  --restart unless-stopped \
  -p 8501:8501 \
  sebsteinig/deepmip-eocene-app:latest
# get status of all running docker apps
sudo docker ps
```

If website goes down:
`sudo reboot`  
or, via ovh webpages.  Either way, it should restart the docker

`sudo apt install -y certbot python3-certbot-nginx`

David has updated the A record of data.deepmip.org so that it points to 37.59.98.55 in place of 51.89.165.226  
Check with: `nslookup data.deepmip.org`

edit /etc/nginx/sites-available/data.deepmip.org  
change server_name to data.deepmip.org

Once A server is set.....  
`sudo certbot --nginx -d data.deepmip.org`  
To enable https://

To check apps running:  
`sudo docker ps`  






