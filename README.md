<div align="center">

# ChronoTube: Fetch and organize YouTube videos by query 📹✨

</div>

ChronoTube is an API that fetches and organizes the latest YouTube videos based on a specified search query. It continuously polls the YouTube API to gather video data, including titles, descriptions, publish dates, and thumbnail URLs, storing this information in a database. The API provides a paginated response of the stored videos, sorted in reverse chronological order. ChronoTube is designed for scalability and performance, with support for multiple API keys to manage quota limits efficiently.

## 🔗 Links

- Link to the documentation: [SwaggerHub hosted docs](https://app.swaggerhub.com/apis/DIVIJS75_1/ChronoTube/v1)
- Link to the dashboard: [ChronoTube Dashboard](https://github.com/dvjsharma/ChronoTube_Client)
- Link to a video demo: [ChronoTube Demo](https://drive.google.com/drive/folders/1XIPPzRPNPOA-hBTvK0OD70gl6-rXFoVe?usp=sharing)

## 💻Tech Stack

- **Django**: Web framework for building the API.
- **Django REST framework**: Toolkit for building Web APIs.
- **Celery**: Distributed task queue for background processing.
- **Redis**: In-memory data structure store for Celery.
- **MySQL**: Relational database for storing video data.
- **Docker**: Containerization platform for packaging the application.
- **Swagger UI**: API documentation tool for interactive API exploration.
- **YouTube Data API**: API for fetching YouTube video data.
- **Flake8**: Linting tool for enforcing code style and quality.

## ✅ Task List

 - [x] **Background Fetching**: Used Celery to implement asynchronous tasks that continuously fetch the latest YouTube videos every 10 seconds based on a query.
 - [x] **Data Storage**: Stores video details (id, title, description, publish date, thumbnail URLs) in a MySQL database with proper indexing (title, desc, publishedAt) for optimized queries.
 - [x] **Fetch API**: Provides a paginated GET API, sorted in descending order by publish date.
 - [x] **Pagination**: Provided `total`, `pages`, `next`, and `previous` fields in the response to represent the total number of videos, total pages, and URLs for the next and previous pages for easy navigation through the video list.
 - [x] **Docker Support**: Provided Docker configuration to easily set up and run the application in a containerized environment.
 - [x] **Swagger UI**: Integrated Swagger UI for comprehensive API documentation, enabling easy interaction with and testing of the API endpoints.
 
 ### Additional Tasks

 - [x] **Multiple Key Support**: Implemented round-robin API key rotation to efficiently manage YouTube Data API quotas. When one API key's quota is exhausted, the system automatically switches to the next available key, ensuring uninterrupted data fetching.
 - [x] **Dashboard**: Implemented a basic UI to access the functionalities.
 - [x] **Searching & Sorting**: Implemented search and sort functionality that allows filtering videos by keywords in titles and descriptions. Results are returned in reverse chronological order based on the published date, with the ability to switch between ascending or descending order.

## 🚀Getting Started

### Versions

This project was developed using `Python V3.11.4` and `Pip V24.2`. It is recommended to install and use the same versions to prevent any unforeseen errors during setup or execution.

### Installation

1. **Clone this repository:**

    ```bash
    git clone https://github.com/dvjsharma/ChronoTube.git
    cd ChronoTube
    ```

2. **Setup virtual environment and install dependencies**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Set up environment variables**

  - Create a `.env` file in the root directory and copy the content from `.env.example` into it.
  - Fill in the required values for YouTube API keys, MySQL database credentials, etc.

4. **Run database migrations**

    ```bash
    python manage.py migrate
    ```

5. **Run Celery worker and beat for background tasks in new terminals:**

      ```bash
      # NOTE: Run both of these in seperate terminals with same virtual enviroment as the app.
      celery -A ChronoTube worker --loglevel=info   
      celery -A ChronoTube beat --loglevel=info   
      ```

6. **Run the Django development server:**

    ```bash
    python manage.py runserver
    ```
7. The API should now be accessible at http://127.0.0.1:8000/. You can explore the available endpoints using the Swagger UI at `/swagger/`.