# Movie Recommendation System

A comprehensive Movie Recommendation System built using collaborative filtering and content-based filtering techniques. This project leverages various machine learning algorithms to provide personalized movie recommendations to users based on their preferences and past interactions.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The Movie Recommendation System is designed to suggest movies to users based on their individual preferences. The system combines both collaborative filtering (user-based and item-based) and content-based filtering to generate recommendations. The goal is to enhance the user experience by providing relevant and personalized movie suggestions.

## Features

- **Collaborative Filtering**: Utilizes user-item interactions to recommend movies.
- **Content-Based Filtering**: Analyzes movie metadata to find similar movies.
- **Hybrid Approach**: Combines collaborative and content-based filtering for improved recommendations.
- **User-Friendly Interface**: Simple and intuitive interface for users to get recommendations.

## Installation

To get a local copy up and running, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/shovanpaul48/Movie-Recommendation-system.git
    ```

2. Navigate to the project directory:
    ```sh
    cd Movie-Recommendation-system
    ```

3. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On MacOS/Linux:
        ```sh
        source venv/bin/activate
        ```

5. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the application, follow these steps:

1. Ensure that your virtual environment is activated.
2. Run the main application:
    ```sh
    python main.py
    ```

3. Open your web browser and go to `http://localhost:5000` to access the application.

## Dataset

The system uses a dataset containing movie information and user ratings. You can download the dataset from [MovieLens](https://grouplens.org/datasets/movielens/).

## Technologies Used

- Python
- Flask (for the web interface)
- Pandas and NumPy (for data manipulation)
- Scikit-Learn (for machine learning algorithms)
- Jupyter Notebook (for experimentation and visualization)

## Contributing

Contributions are welcome! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature/YourFeature
    ```
3. Make your changes.
4. Commit your changes:
    ```sh
    git commit -m 'Add some feature'
    ```
5. Push to the branch:
    ```sh
    git push origin feature/YourFeature
    ```
6. Open a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Shovan Paul - [@shovanpaul48](https://github.com/shovanpaul48)

Project Link: [https://github.com/shovanpaul48/Movie-Recommendation-system](https://github.com/shovanpaul48/Movie-Recommendation-system)
