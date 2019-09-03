![alt text](https://raw.githubusercontent.com/samanseifi/pyStaticA/master/logo.png "Logo Title Text 1")

pyStaticA: A simple engineering code for analysing froce-displacement type data from either performance testing of mechanical constructs or materials testings such as tensile, bending, torsion etc where the charachterstic curve has a linear portion with a well defined mudulus followed by a non-linear portion with a yield point defined as the limit of linear portion. This type of response is quite common in industrial design such as in aerospace, medical devices etc.

The method for finidng the yield is the offset method with the amount `offset-value` given as an input by the user into the input file. The modulus (a.k.a stiffness) is calculated based on two given points hopefully on the linear part of the curve with `x` values of `x-val1` and `x-val2`.

The code takes a text file as an input with multiple lines. Each line must have the following format:

`filename offset-value x-val1 x-val2`

filename: The path to a `csv` or `txt` file consists of two columns of data (`xy_data`).

offset value: The value for which the offset calculation is based on. For example, for typical stress-strain data of a tensile test the offset is `0.1` percent.

x-val1:

x-val2:


The software takes an input file contatins line of information linking xy-data in `csv` to the given offset points.

