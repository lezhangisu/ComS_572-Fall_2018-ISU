## Lab1 Programs
### 1. Solution to Intranets Searching

"solver.py" is the program that works on synthetic intranets.

Change the "folder" variable to corresponding relative path containing "intranets/" folder before running.

Run:

```
python solver.py num1 num2
```

Where `num1` is the index number of intranets (1, 5, or 7 in this case).

And `num2` is the mode (0 = single-algorithm mode, 1 = multi-algorithm mode).

### 2. Solution to World Wide Web Searching

"real_web.py" is the program that works on the WWW pages.

By default, it parses webpages from Wikipedia. It only parses the webpages within Wikipedia domain.

The default starting page is [https://en.wikipedia.org/wiki/Sports](https://en.wikipedia.org/wiki/Sports), query words are "Paolo Cesare Maldini".

You can change your query words and initial page in the .py file before you run it.

Run:
```
python real_web.py
```
