# Carpark Boomgate Automatic Numberplate Recognition System
### Built by Ronan Dean for 2021 Q1/2 Electronics assigment

## Recognition system
### Files
The recognition folder contains the recognition_processing python file which is based off PyImageSearches method to find license plates and send them to tesseract OCR. This must be installed on system, and is currently configured to use a custom trained model for the fake license plate font used. 
The recognitiondriver.py is used to read in photos from an input (the photos folder) and process them thru the recognition_processing file. 
For this to work opencv must be built from source. 

## Database system
Still a work in progress, however it uses mongodb running locally to build a database of numberplates. 
The databasedriver.py has 3 options to find, insert and exit cars from the car park. Once identification is working better, this will be intergrated into the recognition system. 