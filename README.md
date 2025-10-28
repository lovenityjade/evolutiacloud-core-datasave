# evolutiacloud-core-datasave
EvolutiaCloud Core Server - Savegame Synchronisation Module

- Save files keep their **original RetroArch filenames**  
- Storage usage automatically updated and verified  
- Synchronization only triggers when local files are newer (`lastsync` check)

---

## 🗃️ Database Structure

**Database:** `evolutiacloud-core`

### Table: `CloudSave_users`
| Field | Description |
|--------|-------------|
| userid | Unique user ID |
| username | Account username |
| password | Encrypted password (SHA3-512) |
| email | Email address |
| permissions | Permission level (`userperm_new`, `userperm_confirm`, `userperm_admin`) |
| maxstorage | Maximum storage in MB |
| currentstorage | Current usage in MB |
| patreontier | Patreon tier (0–3) |
| active | Account status (true/false) |
| creationdate / creationtime | Registration date and time |
| cloudsavepath | Path to user’s save directory |
| discordname | Linked Discord username |
| profilepicture | Path to profile picture (not counted in storage) |
| lastlogin | Last login timestamp |

### Table: `CloudSave_saves`
| Field | Description |
|--------|-------------|
| id | Unique save ID |
| userid | Linked user ID |
| savefilename | Original filename |
| savecore | RetroArch core used |
| console | Console type (Gameboy, PlayStation, GameCube, etc.) |
| savesize | File size in MB |
| savepath | Full cloud path |
| lastsync | Last synchronization date/time |

---

## 🎖️ Patreon Storage Tiers

| Tier | Description | Storage Limit |
|------|--------------|----------------|
| 0 | Free | 50 MB |
| 1 | Supporter | 100 MB |
| 2 | Super Supporter | 150 MB |
| 3 | Ultra Supporter | 250 MB |
| Admin | Debug / Internal | Unlimited |



---

## 🧰 Installation Overview

Target OS: **Linux (Debian / Ubuntu)**  
Web server: **Apache2 with PHP**  
Database: **MariaDB**

---

## 🧠 Development Roadmap

| Milestone | Status | Description |
|------------|--------|-------------|
| Alpha 0.01.0 | 🟢 In progress | Core server, DB, upload/download, SHA3 checks |
| Alpha 0.02.0 | ⚙️ Upcoming | Web user dashboard |
| Beta 0.1.0 | ⏳ Planned | Discord OAuth integration, Admin panel |
| Release 1.0.0 | 🔜 Future | Public stable cloud sync release |

---

## 🧩 Tech Stack

- **Backend:** Python 3.12 + FastAPI  
- **Frontend:** PHP + HTML + CSS (Dashboard)  
- **Database:** MariaDB  
- **Web Server:** Apache2  
- **OS:** Linux (Debian/Ubuntu)

---

## 🤝 Contributing

Contributions are welcome!  
If you'd like to participate:
1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/your-feature`)  
3. Commit and push your changes  
4. Open a Pull Request  

All code should follow PEP8 and include comments for maintainability.

---

## ⚖️ License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute it, provided that proper credit is given.

---

## 💬 Author

**TheLovenityJade**  
VTuber & Developer — Québec, Canada 🇨🇦  
Part of the **EvolutiaCloud Project Suite**  
© 2025 TheLovenityJade. All rights reserved.

