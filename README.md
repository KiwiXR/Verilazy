# Verilazy
A semi-supervised verilog code generator for lazy people like me
## Usage
To view usage, run ``python verilazy.py -h``
```
$ python3 verilazy.py -h
usage: python verilazy.py [-b int] [-f str] [-s str] [-c int] [-o str]
[str lines]

Verilazy: Verilog Lazy Code Generator

optional arguments:
  -h, --help            show this help message and exit
  -b BATCH, --batch BATCH
                        batch size of formats
  -f FORMAT, --format FORMAT
                        format of single line
  -s SIGN, --sign SIGN  pair of sign for replacement
  -c COUNTER, --counter COUNTER
                        maximum value of auto counter
  -o OUTFILE, --output OUTFILE
                        output file

format: {<n> : number, <s> : string, <c> : auto counter} Note that numbers are same as strings except for extra type check
```
## Example
### Case 1:
```
$ python3 verilazy.py -b 2 -c 2
Namespace(batch=2, counter=2, format='', output='', sign='<>')
reg [2:0] light_<c>;
assign light_<c> = sig<n>_<s>;
INFO: 2 formats read.
>> reg [2:0] light_0;
a
ERROR: Wrong number of params! [0 Expected]
>> reg [2:0] light_0;
INFO: 0 params to be filled [Retry 1/10]

>> assign light_0 = sig<n>_<s>;
h h
ERROR: Wrong type of param 0: h [Integer Expected]
>> assign light_0 = sig<n>_<s>;
INFO: 2 params to be filled [Retry 1/10]
1 h
<< reg [2:0] light_0;
<< assign light_0 = sig1_h;
INFO: Round 1 OK.

>> reg [2:0] light_1;

>> assign light_1 = sig<n>_<s>;
0 l
<< reg [2:0] light_1;
<< assign light_1 = sig0_l;
INFO: Round 2 OK.

INFO: All work done!
SUM UP:

reg [2:0] light_0;
assign light_0 = sig1_h;
reg [2:0] light_1;
assign light_1 = sig0_l;

```
### Case 2:
```
$ python3 verilazy.py -b 1 -f 'wire [3:0] digital_<c>' -o 'out.txt'
Namespace(batch=1, counter=1, format='wire [3:0] digital_<c>', output='out.txt', sign='<>')
INFO: 1 formats read.
>> wire [3:0] digital_0

<< wire [3:0] digital_0
INFO: Round 1 OK.

INFO: All work done!
SUM UP:

wire [3:0] digital_0

```