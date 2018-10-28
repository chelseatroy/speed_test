# speed_test
An example speed comparison of matrix elementwise multiplication in Python, C, and Numpy


To run on a mac, compile the c with:
`$ gcc -shared -Wl,-install_name,multiply.so -o multiply.so -fPIC multiply.c
`
Then run
`python main.py`
