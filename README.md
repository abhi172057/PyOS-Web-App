# PyOS Web App

A web-based Operating System simulation built using **Django REST Framework** and **React.js**.

---

# Overview

PyOS is a browser-based operating system simulator that provides file management functionalities similar to a real OS.

Users can:

* Create folders
* Create files
* Move files
* Move folders
* Delete files
* Restore deleted files
* Search files and folders
* View command history
* View system logs
* Manage data through a modern React UI

---

# Tech Stack

## Frontend

* React.js
* React Router
* Axios
* CSS

## Backend

* Django
* Django REST Framework
* SQLite

---

# Project Architecture

```text
┌─────────────────┐
│ React Frontend  │
└────────┬────────┘
         │ HTTP Request
         ▼
┌─────────────────┐
│ Django URLs     │
└────────┬────────┘
         ▼
┌─────────────────┐
│ Views Layer     │
└────────┬────────┘
         ▼
┌─────────────────┐
│ Service Layer   │
└────────┬────────┘
         ▼
┌─────────────────┐
│ Models Layer    │
└────────┬────────┘
         ▼
┌─────────────────┐
│ SQLite Database │
└─────────────────┘
```

---

# Request Flow

```text
React
  ↓
API Call
  ↓
urls.py
  ↓
views.py
  ↓
service.py
  ↓
models.py
  ↓
Database
  ↓
Response
  ↓
React UI Update
```

---

# Modules

## 1. Users Module

Handles:

* Login
* Registration
* User Roles

Files:

```text
users_api/
```

---

## 2. File System Module

Handles:

* Create Folder
* Create File
* List Directory
* Move File
* Move Folder
* Delete File

Files:

```text
filesystem_api/
```

---

## 3. Recycle Bin Module

Handles:

* Deleted files
* Restore file
* Permanent delete

Files:

```text
recyclebin_api/
```

---

## 4. History Module

Stores all executed commands.

Examples:

```text
mkdir Projects
touch notes.txt
mv notes.txt Documents
rm notes.txt
```

Files:

```text
history_api/
```

---

## 5. Logs Module

Stores system events.

Examples:

```text
CREATE_FILE
DELETE_FILE
MOVE_FILE
RESTORE_FILE
```

Files:

```text
logs_api/
```

---

# Database Design

## Directory

```text
id
name
owner
parent
created_at
```

---

## File

```text
id
name
content
owner
directory
created_at
```

---

## RecycleBinItem

```text
id
owner
item_name
item_type
content
parent_id
deleted_at
```

---

# Implemented Features

## File Explorer

* Browse folders
* Browse files
* Breadcrumb navigation

---

## File Operations

* Create file
* Open file
* Move file
* Delete file

---

## Folder Operations

* Create folder
* Open folder
* Move folder

---

## Recycle Bin

* Soft delete
* Restore
* Permanent delete

---

## Search

Search files and folders instantly.

---

## History

Track all commands executed by the user.

---

## Logs

Track all system actions.

---

# Security Layer

Implemented through:

```text
FileSystemSecurity
```

Checks:

* Ownership validation
* Read permissions
* Write permissions

---

# Example Flow

## Create File

```text
User clicks Create File
      ↓
React sends POST request
      ↓
Django URL
      ↓
View
      ↓
FileSystemService.create_file()
      ↓
File Model
      ↓
Database
      ↓
History Log
      ↓
System Log
      ↓
Response
      ↓
UI Refresh
```

---

# Future Enhancements

* Rename File
* Rename Folder
* Delete Folder
* Download File
* Upload File
* Share Files
* Admin Dashboard
* Real-time Notifications

---

# Author

Abhishek Arya

B.Tech CSIT

Dronacharya Group of Institutions

Greater Noida
