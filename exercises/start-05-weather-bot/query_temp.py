
from promptflow import tool
import requests
import re

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(city_name: str) -> str:
    # wttr.in API URL
    base_url = f"https://wttr.in/{city_name}"
    
    # Parameters for the API request
    params = {
        "format": "%t",  # Get only the temperature
    }
    
    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for HTTP error responses
        
        # Get the temperature from the response text
        temperature = response.text.strip()
        
        # Remove any '+' or arithmetic symbols
        clean_temperature = re.sub(r'[+\-*/]', '', temperature)
        
        return f"The current temperature in {city_name} is {clean_temperature}."
    except requests.exceptions.RequestException as e:
        print(f"Error querying the temperature: {e}")
