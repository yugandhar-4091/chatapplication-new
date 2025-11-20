# chatapplication-new
# 💬 TalkNest — Real-Time Chat Application (Django + WebSockets)

TalkNest is a modern, real-time chat application built using **Django**, **Django Channels**, **WebSockets**, and **TailwindCSS**.  
It supports multiple chat rooms, typing indicators, emoji picker, message timestamps, and a clean neon-glass UI.

This project is fully deployed on Render and supports WebSocket communication for real-time messaging.

---

## 🚀 Features

### ✅ **Authentication**
- User Sign Up / Login / Logout  
- Secure session management  
- Redirects to chat rooms after login  

### 💬 **Chats & Rooms**
- Multiple chat rooms (general, office, friends, custom rooms)
- Real-time messaging using WebSockets  
- Clean UI with neon glassmorphism  
- Responsive for **Mobile, Tablet, Laptop, and Desktop**

### 😄 **Emoji Support**
- Built-in emoji picker  
- Click to insert emojis into message box  

### ⚡ **WebSockets**
- Real-time two-way communication  
- No page reloads  
- Automatic scroll-to-latest message  

### 📁 **File / Image Support (Optional)**
- Upload images or files inside rooms  
- Preview inside chat (coming soon)

### 📱 **Fully Responsive**
- Looks amazing on:
  - 💻 Desktop  
  - 🖥️ Laptop  
  - 📱 Mobile  
  - 📟 Tablet  

---

## 🛠️ **Tech Stack**

| Layer | Technology |
|-------|------------|
| Backend | Django 5.x |
| Realtime Engine | Django Channels + WebSockets |
| Frontend | TailwindCSS |
| Deployment | Render |
| Database | SQLite / PostgreSQL |
| Web Server | Daphne |

---

## 📂 **Project Structure**

chatapplication/
│── chat/
│ ├── consumers.py
│ ├── models.py
│ ├── routing.py
│ ├── templates/chat/
│ └── urls.py
│
├── chatproject/
│ ├── asgi.py ← WebSocket entry
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── templates/
│ ├── registration/login.html
│ ├── registration/signup.html
│ ├── chat/room.html
│ └── chat/room_list.html
│
├── requirements.txt
├── Procfile
└── render.yaml
