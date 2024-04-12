# BrokersHub_DRF_Backend

## Description
This repository contains the Django backend for the TechManTejas platform, a service for managing email communications and user interactions within various modules like advertising, brokerage, and user requirements.

## Installation

To set up the project environment:

1. Ensure you have Python 3.8+ and pip installed.
2. Clone the repository to your local machine.
3. Navigate to the project directory and install dependencies with `pip install -r requirements.txt`.
4. Set up your local settings by creating a `.env` file with necessary configurations.

## Usage

To install dependencies:

    pip install -r requirements.txt

To run the Django server locally:

    python manage.py runserver

Navigate to `http://localhost:8000/` to view the application.

## Folder Structure

- `advertisement` - Contains templates and logic for email handling related to advertisements.
- `brokershub` - Manages broker-specific email communications.
- `deal` - Backend services for deal management.
- `otp` - Functionality for one-time password generation and verification.
- `requirement` - Manages user-submitted requirements.
- `static` - Static files for the Django application.
- `user` - User management and authentication services.
- `utils` - Utility scripts and helper functions.

Root-level files like `requirements.txt`, `manage.py`, and SSL certificates are used for project configuration and setup.

## Contributing

We welcome contributions! Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the [LICENSE](LICENSE.md) - see the file for details.

## Contact

For any queries or technical issues, please open an issue on this repository or contact us at [contact@example.com](mailto:contact@example.com).