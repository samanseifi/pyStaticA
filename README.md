![alt text](https://raw.githubusercontent.com/samanseifi/pyStaticA/master/logo.png "Logo Title Text 1")

**pyStatic** A is a simple engineering code for analysing any kind of force-displacement data that can be coming from in-_situe_ or in-_silico_ testing of mechanical constructs or materials characterization testings such as tensile, bending, torsion etc where the charachterstic curve has a linear portion with a well defined mudulus followed by a non-linear portion with a yield point defined as the limit of linear portion. This type of response is quite common in industrial design such as in aerospace, medical devices etc.

The method for finidng the yield is the offset method with the amount `offset-value` given as an input by the user into the input file. The modulus (a.k.a stiffness) is calculated based on two given points hopefully on the linear part of the curve with `x` values of `x-val1` and `x-val2`.

The code takes a text file as an input with multiple lines. Each line must have the following format:

`<filename> <offset-value> <x-val1> <x-val2>`

`<filename>`: The path to the data file consists of two columns of data (`xy_data`). Note: It can handle both `csv` and `txt` files.

`<offset value>`: The value for which the offset calculation is based on. For example, for typical stress-strain data of a tensile test the offset is `0.1` percent.

`<x-val1>`: First value of the x-axis which the stiffness slope is calculated. 

`<x-val2>`: Second value of the x-axis which the stiffness slope is calculated.


The software takes an input file contains line of information linking xy-data in `csv` to the given offset points.

Plotting example shows the offset line, and the points for calculating the stiffness:

![](https://raw.githubusercontent.com/samanseifi/pyStaticA/master/plot0.png "Logo Title Text 1")
![](https://raw.githubusercontent.com/samanseifi/pyStaticA/master/plot1.png "Logo Title Text 1")