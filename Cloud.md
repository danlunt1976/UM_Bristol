
[Back to HadCM3_technical_notes](HadCM3_technical_notes.md)

# Cloud Services

## Setting up cloud services

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

#### security
these steps are optional, but recommended for improved security of the VPS
1. update system packages:
```
sudo apt update
sudo apt upgrade
sudo reboot
```
2. create a non-root user with sudo priviliges:
```
sudo adduser deepmip-app
sudo usermod -aG sudo deepmip-app
```

3. Create key-pairs etc so log in from another machine
`ssh-copy-id deepmip-app@VPS-IP`

4. Configure firewall and traffic limiting:
```
sudo ufw allow OpenSSH
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

We can check the status of the website:
`nslookup data.deepmip.org`  

#### Install docker engine
We use Docker to quickly deploy the containerised DeepMIP application. In order to run a Docker container, we need to install the Docker engine on the VPS first.
To load docker, follow instructions here: [https://docs.docker.com/engine/install/ubuntu](https://docs.docker.com/engine/install/ubuntu)  
(1) `for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done`  
(2) text from "Set up Docker's apt repository"  
(3) `sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`

Now we can actually launch the app:  
`sudo docker run -p 8501:8501 sebsteinig/deepmip-eocene-app:latest`

You can now view your Streamlit app in your browser:  
URL: [http://37.59.98.55:8501](http://37.59.98.55:8501)

#### Configure domain DNS

This works, but we want to access the app via data.deepmip.org, not by going to http://$VPS-IP:8501.

To do this, we need to modify the DNS configuration of our deepmip.org domain. This can be done via the web interface of our domain hosting company and look for the DNS settings.

We need to create/modify the "A record" for the data subdomain:

**A Record:**
- **Type**: A
- **Name**: data
- **Value**: YOUR_VPS_IP
- **TTL**: lowest possible

This entry will mean, that whenever a user accesses data.deepmip.org, they will be redirected to our new VPS server. So they don't need to remember the full IP address.

We can check whether this worked with `nslookup data.deepmip.org`. And we should be able to access the app in a browser via: http://data.deepmip.org:8501

#### Install and configure nginx

But we don't want to always add the streamlit port 8501 to the URL, but rather reach the app via the base URL alone.

For this, we need to run a web server on our VPS which constantly listens to incoming traffic and redirects it to the according application running in the backend on our VPS (also called a "reverse proxy server"). The most used solution for this is nginx (https://nginx.org/en/).

1. Now needs a web server (engine-x)  
`sudo apt install -y nginx`

2. create nginx configuration for the app
`sudo vi /etc/nginx/sites-available/data.deepmip.org`

3. add this configuration:
```
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

4. enable the site
```
sudo ln -s /etc/nginx/sites-available/data.deepmip.org /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
```

5. test and reload nginx:
```
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

#### install certbot and obtain SSL certificate

We really don't want to use HTTP, but the more secure HTTPS. For this, we need a SSL certificate for our nginx server config so that the user's browser can trust the connection. Easiest is to use certbot to automatically get this certificate:

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

To see details of an app:  
`sudo docker inspect deepmip-app | grep -A 5 Mounts`


## Deploying changes to the app

The way to implement any changes to the app is to change the files in this repo: [https://github.com/sebsteinig/deepmip-web-app](https://github.com/sebsteinig/deepmip-web-app "https://github.com/sebsteinig/deepmip-web-app"). Best practice is to clone the repo, create a new branch, implement all changes you want, push the new branch to GitHub and then open a pull request to merge the changes into the main branch. Since this is only one line in this case, I created this pull request and merged it already (for reference: [https://github.com/sebsteinig/deepmip-web-app/pull/2](https://github.com/sebsteinig/deepmip-web-app/pull/2 "https://github.com/sebsteinig/deepmip-web-app/pull/2")). Once any file in main changes, the Docker image gets automatically updated and pushed to [https://hub.docker.com/repository/docker/sebsteinig/deepmip-eocene-app/general](https://hub.docker.com/repository/docker/sebsteinig/deepmip-eocene-app/general "https://hub.docker.com/repository/docker/sebsteinig/deepmip-eocene-app/general"). So, the only thing left to do is to tell your VPS to use this updated docker image. I attached the commands you need to run as a Markdown file to this email. Afterwards, the contact email on the deployed app should be updated.

To do this, on the VPS, run:
```bash
sudo docker pull sebsteinig/deepmip-eocene-app:latest
```

to fetch the new image. Then stop and delete the old image with:
``` bash
sudo docker stop deepmip-app
sudo docker rm deepmip-app
``` 

Finally, you can use the same command you previously used to deploy the app, which should probably be: 

```bash
sudo docker run -d \
  --name deepmip-app \
  --restart unless-stopped \
  -p 8501:8501 \
  sebsteinig/deepmip-eocene-app:latest
```

To check apps running:  
`sudo docker ps`  

