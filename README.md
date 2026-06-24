#### License
MIT

# Library Management System

A Library Management System built using the Frappe Framework to automate library operations including book catalog management, member management, book issue/return tracking, overdue fine calculation, fine collection, reporting, and dashboard monitoring.

## Overview

This application digitizes and streamlines day-to-day library operations by providing:

* Book Catalog Management
* Member Management
* Book Issue & Return
* Overdue Detection
* Fine Management
* Reporting & Dashboard
* Role-Based Access

## Features

### Book Catalog Management

* Manage books with ISBN, author, category, and rack location.
* Track total and available copies.
* Automatic stock updates on issue and return.
* Book availability status tracking.

### Member Management

* Member registration and profile management.
* Membership validity tracking.
* Outstanding fine tracking.
* Member activity history.

### Book Issue & Return

* Issue books to members.
* Automatic due date generation based on Library Settings.
* Prevent issuing books when stock is unavailable.
* Return processing with automatic stock restoration.
* Overdue status tracking.

### Fine Management

* Automatic fine generation for overdue books.
* Fine amount calculation based on configurable per-day rate.
* Partial fine payment support.
* Fine waiver support.
* Outstanding balance calculation.
* Fine payment tracking.

### Reports

* Overdue Books Report
* Fine Collection Report
* Member Activity Report

### Dashboard

Workspace dashboard includes:

* Total Books
* Available Books
* Books Issued
* Overdue Books
* Members
* Pending Fines
* Fine Amount Outstanding

## System Workflow

### Book Issue

1. Select Member
2. Select Book
3. System validates available copies
4. Due date generated automatically
5. Available copies reduced

### Book Return

1. Return date recorded
2. Overdue days calculated
3. Fine generated if applicable
4. Available copies restored
5. Fine Management entry created

### Fine Management

* Pending
* Partially Paid
* Paid
* Waived

Outstanding amount is calculated automatically.

## Modules

### Master Data

* Book Category
* Books
* Library Member
* Library Settings

### Transactions

* Book Issue
* Fine Management

### Reports

* Overdue Books Report
* Fine Collection Report
* Member Activity Report

## Technology Stack

* Frappe Framework v14
* Python
* MariaDB
* JavaScript

## Installation

```bash
bench get-app library_management
bench --site [site-name] install-app library_management
```

## Roles

### Library Administrator

* Full access to all modules

### Library Staff

* Manage books
* Manage members
* Issue and return books

### Accounts Staff

* Manage fines
* Track payments
* View reports

### Management

* Dashboard access
* Reports access

## Future Enhancements

* ERPNext Accounting Integration
* Email Notifications for Overdue Books
* Barcode-Based Book Tracking
* Book Reservation System
* Advanced Analytics Dashboard

## Screenshot

### Workspace Dashboard

<img width="1366" height="577" alt="image" src="https://github.com/user-attachments/assets/5a1eeb2e-755a-48ba-bb70-a0645bf5eb0d" />


### Book Management

<img width="1711" height="567" alt="image" src="https://github.com/user-attachments/assets/ba08e279-ab39-40eb-8341-e6f491354c0a" />


### Book Issue
<img width="1711" height="567" alt="image" src="https://github.com/user-attachments/assets/a78b50ce-f3ac-4b74-90c6-d8aef1e85507" />


### Fine Management

<img width="1711" height="567" alt="image" src="https://github.com/user-attachments/assets/7912a064-37ef-488a-a39a-5ddff1249d46" />


### Reports

<img width="1123" height="565" alt="image" src="https://github.com/user-attachments/assets/11007638-ea1b-4e50-9bcb-5969c87dac7f" />

<img width="1123" height="565" alt="image" src="https://github.com/user-attachments/assets/28d1dad4-16b5-4253-8c56-00bc5dd70757" />

<img width="1123" height="565" alt="image" src="https://github.com/user-attachments/assets/7b150b5b-8edd-4d52-b8bc-6fc505d2679a" />


## Author

Sujeet Kumar

Built as part of a Library Management System assignment using the Frappe Framework.
