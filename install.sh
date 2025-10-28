#!/bin/bash
echo "=== EvolutiaCloud DataSave Installer ==="

# Update system
apt update -y && apt upgrade -y

# Install dependencies
apt install -y python3 python3-pip mariadb-server libmariadb-dev apache2 php libapache2-mod-php

# Install Python packages
pip3 install -r requirements.txt

# Create database and tables
mysql -u CHANGE_THIS -pCHANGE_THIS <<EOF
CREATE DATABASE IF NOT EXISTS \`evolutiacloud-core\`;
USE \`evolutiacloud-core\`;

CREATE TABLE IF NOT EXISTS \`CloudSave-users\` (
  userid INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255),
  password VARCHAR(255),
  email VARCHAR(255),
  permissions VARCHAR(50),
  maxstorage INT DEFAULT 50,
  currentstorage INT DEFAULT 0,
  patreontier INT DEFAULT 0,
  active BOOLEAN DEFAULT TRUE,
  creationdate DATE,
  creationtime TIME,
  cloudsavepath VARCHAR(255),
  discordname VARCHAR(255),
  profilepicture VARCHAR(255),
  lastlogin DATETIME
);

CREATE TABLE IF NOT EXISTS \`CloudSave-Saves\` (
  id INT AUTO_INCREMENT PRIMARY KEY,
  userid INT,
  savefilename VARCHAR(255),
  savecore VARCHAR(255),
  console VARCHAR(255),
  savesize INT,
  savepath VARCHAR(255),
  lastsync DATETIME,
  FOREIGN KEY (userid) REFERENCES \`CloudSave-users\`(userid)
);

INSERT INTO \`CloudSave-users\`
(username, password, email, permissions, patreontier, active, creationdate, creationtime, cloudsavepath)
VALUES ('admin', '$(openssl passwd -6 CHANGE_THIS)', 'admin@thelovenityjade.com', 'userperm_admin', 3, TRUE, CURDATE(), CURTIME(), '/etc/evolutiacloud/saves/admin/');
EOF

# Create folders
mkdir -p /etc/evolutiacloud/saves
mkdir -p /var/www/thelovenityjade/evolutiacloud/cloudsaves
mkdir -p /var/log/evolutiacloud

# Permissions
chown -R www-data:www-data /var/www/thelovenityjade/evolutiacloud
chmod -R 755 /etc/evolutiacloud/saves

echo "=== Installation Complete! ==="
