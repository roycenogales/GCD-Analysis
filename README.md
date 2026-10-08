# GCD-Analysis  

## Description  
This project showcases an in depth analysis of three algorithms used to find the Greatest Common Divisor of two numbers. The three algorithms used are Euclid's algorithm, Consecutive Integer Checking, and Prime Factorization.  

## Prerequisites  
Make sure to have python3 installed.  
```sudo apt-get install python3```  

## To Run  
To run one file, use:  
```python3 {filename}.py```  

## Modify Values  
Within each Python file, there are values that can be altered to get similar effects to those seen in Paper 1 and the Graphs. In the main function, modify the values following the   
```random.randint()```  

Within this line:  

```print(timeit.timeit('m = random.randint(1000000,2000000); n = random.ra\
ndint(500000,999999); start(m,n)', number=5, globals=globals()))```  

Modify these values by powers of 10 to get similar results.  