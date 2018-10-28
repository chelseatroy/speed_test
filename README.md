# speed_test
An example speed comparison of matrix elementwise multiplication in Python, C, and Numpy


To run on a mac, compile the c with:
`$ gcc -shared -Wl,-install_name,testlib.so -o testlib.so -fPIC testlib.c
`
Then run
`python main.py`
