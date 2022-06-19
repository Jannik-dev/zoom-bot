# !!! Use with caution, no warranty !!!

Zoom Bot enables you to manage your Zoom meetings in one place. It fakes user inputs, so don't use the mouse or keyboard while the bot enters the zoom data!

[![Watch the video](https://img.youtube.com/vi/s1vb9bwupcE/maxresdefault.jpg)](https://youtu.be/s1vb9bwupcE)

# Installation
The project uses the Edge web driver. If you want to use another browser than Edge, please change it accordingly. For more information, please refer to this page:
https://pypi.org/project/webdriver-manager/

### Important!
Depending on the browser and language you are using, the images may have to be adjusted.

## Packages
Python and pip have to be installed and setup.

Install required packages with the following command:

```pip install -r requirements.txt```

## Deploy
Use this command to build the executable.

```pyinstaller --onefile main.pyw```

# Run the application
Adjust the meeting-data.json and you are ready to go.