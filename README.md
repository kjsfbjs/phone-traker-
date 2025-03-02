Sahil Musani
Freshen 


Phone tracker 
By sahil 
Phone Lookup Tool by Sahil
Description
This tool allows users to look up details about a phone number using the NumLookup API. It provides information such as country, carrier, and line type. Additionally, it includes a reverse social media lookup feature that generates search links for platforms like Facebook, LinkedIn, Twitter, Instagram, and TikTok.
The tool includes both CLI and GUI modes, allowing users to choose their preferred interface.

Features
✅ Lookup phone number details (carrier, country, line type) ✅ Reverse social media lookup (Facebook, LinkedIn, Twitter, Instagram, TikTok) ✅ Dark mode GUI with dynamic updates ✅ CLI mode with rich table output ✅ Lookup history is saved for later reference ✅ View carrier location on an interactive map

Installation
Prerequisites
Ensure you have Python 3.7+ installed.
Install Required Dependencies
pip install requests rich folium pillow

Usage
CLI Mode
Run the script with a phone number:
python script.py --cli +11234567890
This will output the phone details and social media search links.
GUI Mode
Run the script without any arguments:
python script.py
Enter the phone number in the GUI and click "Lookup" to get the details.

Configuration
Update the API_KEY in the script with your NumLookup API Key before running the tool:
API_KEY = "YOUR_NUMLOOKUP_API_KEY"

Troubleshooting
FileNotFoundError: 'phone_icon.png' not found
Ensure the file exists in the same directory or replace it with a placeholder.
Invalid API Key Error
Double-check and replace API_KEY with a valid key from NumLookup.

Future Enhancements
🚀 Add email lookup capabilities 🚀 Implement additional carrier tracking features 🚀 Expand social media lookup to more platforms

License
This project is licensed under the MIT License. You are free to use, modify, and distribute it as long as you include the original license.

Author
Sahil

Enjoy using the Phone Lookup Tool! 🚀
