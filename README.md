# Weather Application

This Flask web application fetches current weather data using the OpenWeatherMap API based on user-selected or automatically detected location.

## Installation and Setup

Clone the repository:

git clone https://github.com/BehzadHassan/Weather-Application
cd Weather-Application

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Open your browser and navigate to http://localhost:5000 to view the application.

## Usage

- Enter a city name in the search box to see the current weather data for that city.
- Click on "Use Current Location" to fetch weather data based on your current IP address.

## File Structure

project/
│
├── app.py                # Flask application
├── requirements.txt      # Python dependencies
├── templates/            # HTML templates
│   ├── index.html        # Main HTML template
|── static/               # Css and other Static files
│   ├── style.css         # Styling CSS File
│   └── background.jpg    # Background Picture
└── README.md             # Project documentation

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.

## Contact

For any questions or suggestions, feel free to contact:
- Behzad Hassan
- behzadhassan967@gmail.com

## Acknowledgments

- Flask
- OpenWeatherMap API
- geopy
- ipapi.co
