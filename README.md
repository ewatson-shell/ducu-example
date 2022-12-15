# ducu-example

Data plotter is a file which plots all of the original files.
bsfc_power_additions and plots.py is a file which tries to add the BSFC and Power columns to the data tables. 
The reason not before was there were issues with exceptions.


manual_cleaner.py 
cleans the parts of the data which would have an impact on EOT and SOT.

In the data file: 
-----------------
- raw is the full raw initial file.
- raw_to_csv -> only the relevant data extrapolated from the raw excel sheet and converted to csv then saved to file. Additionally as files read in, fuel column, block and run column created for future processing and documentation.
- raw_to_csv_processed -> taking out any issues with strings such as 'True', adding in Power, BSFC columns. (need to note how much data withdrawn at this stage.)
- csv_processed_filtered -> using the parameters given by the client to filter the csv.
- csv_processed_cleaned_final -> csv files after manual cleaning.


In the graphs file:
-------------------
- pre - when the data is first read in checking how it looks for important parameters.
- mid - after the filtering according to the parameters given by client.
- post - after manual filtering, which filters out any possible behaviours which could have impacted the result. 

The data and graphs file have been added to share drive. 


Scripts File:
-------------

Order of Python files to be run:
----------------------------------


To do further (with more time):
------------------------------
- add filepaths to a config file and read them in under those names into the folders.
- Utilise importing functions from functions folder and reduce repeated code.
