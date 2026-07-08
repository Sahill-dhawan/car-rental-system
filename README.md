# 🚗 Modern Car Rental System

A full-stack MERN (MongoDB, Express, React, Node.js) application for renting cars. Built with production-ready architecture, robust security, and real-time features, making it an excellent demonstration of advanced web development patterns.

## ✨ Key Features

### 🔐 Advanced Authentication
- **Multi-Method Login:** Users can log in using traditional Passwords, Email OTPs, or Phone Number OTPs.
- **Mock SMS Architecture:** Implements a production-like SMS OTP architecture (bypassing Twilio costs for demonstration purposes by routing OTPs securely to backend server logs).

### 💳 Payments & Invoicing
- **Razorpay Integration:** Secure end-to-end payment flow using the Razorpay gateway.
- **Dynamic PDF Invoices:** Utilizes `pdfkit` to automatically generate and stream beautifully formatted PDF receipts for users after successful payments.

### ⚡ Real-Time Interactions
- **WebSocket Notifications:** Integrated with `Socket.io` to provide the Admin Dashboard with instant, real-time popup notifications the second a new booking is paid for—no page refresh required.

### 📊 Admin Dashboard
- **Analytics & Data Visualization:** Interactive charts powered by `recharts` to track revenue, bookings, and user growth.
- **Fleet Management:** Full CRUD operations for managing the car inventory, including image uploads and availability toggling.

### 🔍 Search & Filtering
- **Advanced Filtering:** Users can filter available cars by Transmission Type, Price Range, Brand, and Category for a seamless browsing experience.

---

## 🛠️ Tech Stack

### Frontend
- **React.js** (Hooks, Context, Router)
- **Redux Toolkit** (State Management)
- **Vanilla CSS** (Custom, responsive, modern UI)
- **Recharts** (Data visualization)
- **React Hot Toast** (Alerts & notifications)
- **Socket.io-client** (Real-time updates)

### Backend
- **Node.js & Express.js** (REST API architecture)
- **MongoDB & Mongoose** (Database & ODM)
- **Socket.io** (WebSocket server)
- **Razorpay** (Payment processing)
- **PDFKit** (Dynamic PDF generation)
- **Bcrypt & JWT** (Security & Authentication)

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Node.js and MongoDB installed on your system.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sahill-dhawan/Car-Rental-System.git
   cd Car-Rental-System
   ```

2. **Install Backend Dependencies:**
   ```bash
   cd backend
   npm install
   ```

3. **Install Frontend Dependencies:**
   ```bash
   cd ../frontend
   npm install
   ```

4. **Environment Variables:**
   Create a `.env` file in the `backend` directory and configure the following:
   ```env
   PORT=5001
   MONGODB_URI=your_mongodb_connection_string
   JWT_SECRET=your_jwt_secret
   CLIENT_URL=http://localhost:3000
   
   # Razorpay (For payments)
   RAZORPAY_KEY_ID=your_razorpay_key
   RAZORPAY_KEY_SECRET=your_razorpay_secret
   
   # Email configuration (For OTPs)
   EMAIL_USER=your_gmail_address
   EMAIL_PASS=your_google_app_password
   ```

### Running the Application

1. **Start the Backend Server:**
   ```bash
   cd backend
   node server.js
   # Server will run on http://localhost:5001
   ```

2. **Start the Frontend Development Server:**
   ```bash
   cd frontend
   npm start
   # Application will open at http://localhost:3000
   ```

---

## 📱 Usage Guide & Testing

- **Testing Phone/Email OTPs:** When you request an OTP during login, check the terminal where your backend (`server.js`) is running. The mock architecture will print the 6-digit OTP code directly in the console!
- **Testing Real-Time Notifications:** Open the Admin Dashboard (`http://localhost:3000/admin`) in one browser window, and log in as a regular user in an Incognito window. Book a car and complete the payment—you will instantly see a live notification pop up on the Admin Dashboard!
- **Downloading Invoices:** Navigate to "My Bookings" as a user. For any booking marked as `Paid`, click the "Download Invoice" button to generate a PDF receipt.

---
*Built for excellence in modern web development.*
