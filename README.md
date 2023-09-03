# Flight-Deal-Notifier
## Overview
Flight Deal Notifier is an automated Python project that helps you discover and receive notifications about affordable flight deals. It employs Object-Oriented Programming (OOP) principles, API integration, Google Sheets interaction, and automation to simplify the process of finding budget-friendly flights.

## Key Features
OOP Structure: The project is organized using Object-Oriented Programming, with separate classes for data management, flight searching, and notifications.

API Integration: It integrates with various flight search APIs to retrieve real-time pricing and destination data.

Google Sheets Usage: Flight Deal Notifier interacts with Google Sheets to fetch and update flight data, ensuring accuracy and freshness.

Automation: The system automatically searches for flight deals, updates missing information, and sends real-time notifications when enticing deals are discovered.

## How It Works
Data Management (OOP): The DataManager class fetches flight price data from an external source, like Google Sheets. This class ensures that the data remains accurate and up-to-date.

API Integration: The FlightSearch class integrates with flight search APIs to search for deals. It retrieves IATA codes for cities, checks flight availability, and compiles comprehensive flight information.

Google Sheets Interaction: If any city lacks an IATA code, FlightSearch updates it using API calls and stores it back in Google Sheets.

Automated Deal Hunting: Flight Deal Notifier automates the process of searching for flight deals. It calculates travel dates, initiates flight searches, and identifies the best-priced flights.

Instant Notifications: When a great deal matching or surpassing the lowest expected price is found, the NotificationManager sends an SMS notification, ensuring you're informed in real time.

## Getting Started
To use this project, follow the setup instructions in the documentation. You'll need Python, API keys, and a few dependencies.
