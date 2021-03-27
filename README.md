# MyPBot

### How to execute

* Create a virtual environment for the dependencies
* Run ``requirements.txt`` inside your env
* Download browser driver

___

_I suppose you have already installed python on your system, this code works on both Windows and Linux/Mac_

___

### First Step, environment.
_On your preference terminal_

* Install package
    > ``pip install virtualenv``
* Create the virtual environment
    > `` virtualenv venv ``
* Activate the virtual environment
    >Windows:  `` venv\Scripts\activate ``  
    Linux:  `` source venv/bin/activate ``
 

### Second Step, Setup environment.
_Inside your environment_

* Install all dependencies listed on requirements file
    > `` pip install requirements.txt `` 

### Third Step, Webdriver.
_This is will handle the browser for us_

* Search on Google the webdriver compatible with you personal browser, then download then 
    > On my case chromedriver 89, https://chromedriver.chromium.org/downloads  
    Drivers available: ChromeDriver, GeckoDriver, MS Edge WebDriver. 
                                                                                             
    