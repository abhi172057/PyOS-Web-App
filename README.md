# 🚀 PyOS Web App

A cloud-based virtual operating system built using **React.js**, **Django REST Framework**, and **PostgreSQL**. PyOS simulates core operating system functionalities such as file management, folder management, recycle bin, history tracking, logging, search, and multi-user authentication through a modern web interface.

---

# 📌 Features

## 👤 User Management

* User Registration
* User Login
* JWT Authentication
* Multi-user Support
* User Profile Management

## 📁 File System Operations

* Create Folder
* Create File
* List Files and Folders
* Move Files
* Move Folders
* Search Files and Folders
* Delete Files
* Recycle Bin Support

## ♻️ Recycle Bin

* Soft Delete Implementation
* Restore Deleted Files
* Recover Original Location

## 📜 History Tracking

* Store User Commands
* Track User Activities
* Command History Management

## 📊 Logging System

* File Creation Logs
* File Deletion Logs
* Folder Creation Logs
* Move Operation Logs
* Error Logs

## 🔒 Security

* JWT Based Authentication
* User Data Isolation
* Owner-Based Access Control
* Secure Password Hashing

---

# 🏗️ System Architecture

```text
┌─────────────────┐
│ React Frontend  │
└────────┬────────┘
         │ HTTP Request (Axios)
         ▼
┌─────────────────┐
│ Django URLs     │
│ Routing Layer   │
└────────┬────────┘
         ▼
┌─────────────────┐
│ Views Layer     │
│ Request Handler │
└────────┬────────┘
         ▼
┌─────────────────┐
│ Service Layer   │
│ Business Logic  │
└────────┬────────┘
         ▼
┌─────────────────┐
│ Models Layer    │
│ Django ORM      │
└────────┬────────┘
         ▼
┌─────────────────┐
│ PostgreSQL DB   │
│ Render Cloud DB │
└─────────────────┘
```

---

# ⚙️ Technology Stack

## Frontend

* React.js
* Vite
* Axios
* React Router

## Backend

* Django
* Django REST Framework
* JWT Authentication
* Service Layer Architecture

## Database

* PostgreSQL

## Deployment

* Render
* PostgreSQL Render Database

---

# 📂 Project Structure

```text
PyOS
│
├── frontend/
│   ├── src/
│   ├── pages/
│   ├── services/
│   └── layouts/
│
├── users_api/
├── filesystem_api/
├── recyclebin_api/
├── history_api/
├── logs_api/
│
├── pyos_backend/
│
├── requirements.txt
├── manage.py
└── Procfile
```

---

# 🔄 Complete Request Flow

## Example: Create Folder

```text
User clicks "Create Folder"
        ↓
React Frontend
        ↓
POST /filesystem/mkdir/
        ↓
Django URL Router
        ↓
create_directory View
        ↓
FileSystemService.create_directory()
        ↓
Directory Model
        ↓
PostgreSQL Database
        ↓
Success Response
        ↓
React Updates UI
```

---

# 🔐 Authentication Flow

```text
User Login
      ↓
JWT Token Generated
      ↓
Frontend Stores Token
      ↓
Authorization Header
      ↓
Backend Verifies Token
      ↓
request.user Available
      ↓
Protected APIs Accessible
```

Example Header:

```http
Authorization: Bearer <JWT_TOKEN>
```

---

# 📁 File Creation Flow

```text
Frontend
    ↓
Create File API
    ↓
View Layer
    ↓
FileSystemService
    ↓
File Model
    ↓
PostgreSQL
    ↓
Response
```

---

# 🗑️ File Deletion Flow

Instead of permanently deleting files:

```text
File Selected
      ↓
Delete API
      ↓
RecycleBinItem Created
      ↓
Original File Deleted
      ↓
History Updated
      ↓
Logs Updated
      ↓
Success Response
```

---

# ♻️ Recycle Bin Flow

```text
Deleted File
      ↓
Recycle Bin
      ↓
Restore Request
      ↓
File Recreated
      ↓
Original Location Restored
```

---

# 🔍 Search Flow

```text
User Search
      ↓
Search API
      ↓
SearchService
      ↓
Directory Query
      ↓
File Query
      ↓
Combined Result
      ↓
Frontend Display
```

---

# 📜 History Module

Stores user actions such as:

```text
mkdir Documents
touch notes.txt
mv file.txt Docs
rm notes.txt
restore notes.txt
```

Purpose:

* Audit Trail
* User Activity Tracking

---

# 📊 Logging Module

Stores system logs:

```text
CREATE_FILE
CREATE_DIRECTORY
MOVE_FILE
DELETE_FILE
RESTORE_FILE
ERROR
```

Purpose:

* Debugging
* Monitoring
* Tracking System Events

---

# 🛡️ Security Implementation

Every file and folder belongs to a user.

Example:

```python
owner=request.user
```

Query Protection:

```python
Directory.objects.filter(owner=request.user)
```

Result:

```text
User A cannot access User B data.
```

---

# 🗄️ Database Models

## UserProfile

```text
User
Role
```

## Directory

```text
Name
Owner
Parent Directory
Created Time
```

## File

```text
Name
Content
Owner
Directory
```

## RecycleBinItem

```text
Owner
Item Name
Item Type
Parent ID
Original ID
```

## History

```text
User
Command
Timestamp
```

## Logs

```text
User
Action
Description
Timestamp
```

---

# 🚀 Deployment

## Backend

* Render Web Service
* Gunicorn
* PostgreSQL Database

## Frontend

* Vercel / Netlify / Render Static Site

---

# 🧪 API Modules

### Users API

* Register User
* Login User
* Current User
* Update User

### Filesystem API

* Create Folder
* Create File
* Move File
* Move Directory
* Delete File
* List Directory
* Search

### Recycle Bin API

* Restore File
* View Recycle Bin

### History API

* View User History

### Logs API

* View System Logs

---

# 🎯 Key Backend Concepts Used

* REST APIs
* JWT Authentication
* Django ORM
* PostgreSQL
* Service Layer Architecture
* Role-Based Access Control
* Recycle Bin Mechanism
* Activity History Tracking
* Centralized Logging
* Cloud Deployment

---

# 👨‍💻 Author

** Abhishek Kannaujiya **

B.Tech (CSIT)

Backend Developer | Java | JavaScript | Django | React | PostgreSQL

---

# ⭐ Future Enhancements

* File Upload Support
* File Download Support
* Folder Sharing
* User Roles & Permissions
* Real-Time Collaboration
* Cloud Storage Integration
* Admin Dashboard
