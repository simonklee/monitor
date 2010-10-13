# mon.seido.org

Web-interface for displaying sensor data for my photovoltaic wireless-sensor
project.

## Overview

#. Retrieve sensor-data with HTTP GET using the URI hierarchical path. 
#. Use JavaScript Object Notation(JSON) as the data-interchange format.
#. Ability to use charts as a graphical representation for data.

## To do

* Finish the _readserial.py_ code which is responsible for getting the data from
  the transmitting format, and storing it in the database. 
* Add the ability to view charts real-time
* Add the ability to filter search "from-date -- to-date". The current implementation just
  supports "from-date -- today"

## Related projects

The code for the uC will be published in a once it's in a more complete stage. 
