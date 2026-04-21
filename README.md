## Task CLI Manager

A robust, modular Command Line Interface (CLI) tool designed to manage tasks efficiently with local JSON persistence. This project demonstrates clean architecture by separating input validation, utility logic, and command control.

## 📂 Project Structure

The project is organized into several modules to ensure a clean separation of concerns and avoid circular dependencies:

.
├── config.py       # Centralized configuration (Database path)
├── exceptions.py   # Custom error handling and validation exceptions
├── Input.py        # Data validation and model definitions (Input class)
├── Utils.py        # File I/O and data persistence operations
├── controller.py   # Command logic (Commands class)
└── run.py          # Entry point and main application loop


## Features

- CRUD Operations: Easily add, update, delete, and list tasks.

- Data Validation: Custom exceptions for description length and status updates (via @property setters).

- Persistence: All tasks are saved automatically to a local database.json file.

- Timestamps: Every task tracks createdAt and lastUpdate times automatically using ISO format.

- Robustness: Built-in error handling for invalid command lengths and unrecognized commands.

- Modular Design: Uses a one-way dependency chain to prevent circular imports.

##  Usage


1. clone the project using : 
    `https://github.com/trippinganymess/TaskCLI`

Run the application from your terminal:

    `python3 run.py`


Available Commands

The CLI uses a colon-separated format (command:arg1:arg2...):

Command

Format

Description

    Add

    add:status:description

    Creates a new task (e.g., add:todo:read book)

Update

    update:ID:status:description

    Modifies an existing task by ID

Delete

    delete:ID

    Removes a task by its unique ID

List

    `ls`

Displays all tasks in a formatted table

Exit

    exit

Closes the application

Note: Valid statuses are: todo, in-progress, done.

## 🧠 Architecture Concepts

Read-Modify-Write Cycle

This project utilizes a Read-Modify-Write cycle to manage state in a local file. Every time a task is added, updated, or deleted, the application loads the entire JSON file into memory, performs the operation on the list of dictionaries, and then writes the entire structure back to disk.
