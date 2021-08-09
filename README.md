# friendly_styles

Pygments compatible styles used with [friendly](https://github.com/friendly-traceback/friendly).

Two styles are defined: one suitable for black (or very dark) background
and another for white (or very pale) background. 

These styles are defined in such a way that code highlighted by 
[Rich](https://github.com/willmcgugan/rich) use consistent colours whether
the code is highlighted by Rich base on some `repr` bypassing Pygments
or done by Pygments.

![Example of highlighting](example.png)
