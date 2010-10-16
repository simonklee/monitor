# mon.seido.org

Web-interface for displaying sensor data for my photovoltaic wireless-sensor
project.[1](http://mon.sedio.org/)

## Overview

1. Retrieve sensor-data with HTTP GET using the URI hierarchical path. 
2. Use JavaScript Object Notation(JSON) as the data-interchange format.
3. Ability to use charts as a graphical representation for data.
4. _utils/readserial.py_ can be used to transfer data from tty to db.

## To do

* Add the ability to view charts real-time.
* Add the ability to filter search "from-date -- to-date". The current implementation
  supports "on-date".

## Related projects

The code for the uC will be published in a once it's in a more complete stage. 
