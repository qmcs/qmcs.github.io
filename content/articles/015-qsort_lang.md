#Comparing languages with Quicksort

Title: Comparing Languages with Quicksort
Date: 2014-04-20
Tags: Quicksort, languages, speed
Category: languages
Author: Filip Ter

Language speed is often a major factor when determining how useful a programming language can be. Some applications rely on languages that can execute a large amount of instructions in a short amount of time, and programmers may in some cases use languages which have many unpleasant features, just because they can execute an algorithm faster. It would be interesting to see how some languages would fare when it comes to how long it takes them to execute the same algorithm. 

-- PELICAN_END_SUMMARY --

I decided to conduct a comparison of programming languages by using them to implement an algorithm and then timing how long each one would take to execute. For the purposes of this article, a faster program is one which can execute an implementation of an algorithm in less time. The algorithm used was quicksort, which is a well-known sorting algorithm invented by Tony Hoare in 1961.[^thoare] The algorithm is recursive, and it works by finding a pivot value in an array, moving all elements smaller than it to one side and the larger ones to the other, this process is repeated on the sub-sections around the pivot until the whole array is sorted. 

Following up from my previous article, I thought of using the Mersenne Twister[^mt] algorithm to generate random 32bit integers that I would then sort using quicksort in 5 different languages, specifically: C[^c], C++[^cpp], Java[^java], Python 3[^py], and PHP[^php]. For the quicksort algorithm, I found a reasonably good pseudo-code description of it on Wikipedia.[^wiki] Using a Java implementation of Mersenne Twister[^mtjava], I generated 7 files all containing pseudo-random 32bit ints. The files contained 100 to 100 million integers, with each file containing 10 times as many integers as the previous one. Using the description from Wikipedia, I then implemented the algorithm in the 5 languages used in the test, adding functions for reading the numbers from files and printing them for checking.  In the actual test each program was to read the contents of the file, store them in an array, sort the array using quicksort, and finally print a message that the array was sorted. The time of execution would be measured by the Bash time function.[^bashtime] This was mainly done so that the same function would be measuring all programs,  as using timing from different languages might produce unreliable results. In order to obtain more precise results each run instance of sorting was done 10 times, and the average time was taken. In an effort to automate the task slightly more, I wrote a Bash script that would run each instance of the program 10 times, time it and write down the sum to a file.[^bashscript] Then another program would read the values, divide them, and format the output into a csv table.[^writetable]

As for my initial expectations, they coincided with the usual belief about these languages. I expected the compiled languages(C, C++, Java) to be faster, while the interpreted languages should be slower. This basically follows common knowledge about these languages, but the point of the test is to see how they would actually compare, and how significant the difference would be. 
	
* The table which contains the average times for all runs of each program.

| Language | Time taken to sort 10^2 integers (seconds) | Time taken to sort 10^3 integers (seconds) | Time taken to sort 10^4 integers (seconds) | Time taken to sort 10^5 integers (seconds) | Time taken to sort 10^6 integers (seconds) | Time taken to sort 10^7 integers (seconds) | Time taken to sort 10^8 integers (seconds) |
|----------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|
| C        | 0.0020                                      | 0.0030                                      | 0.0092                                     | 0.0227                                     | 0.2242                                     | 2.5311                                     | 27.8197                                    |
| C++      | 0.0037                                     | 0.0055                                     | 0.0111                                     | 0.0573                                     | 0.5693                                     | 5.9676                                     | 62.1247                                    |
| Java     | 0.0603                                     | 0.0813                                     | 0.1079                                     | 0.2279                                     | 0.8806                                     | 7.2826                                     | 71.9754                                    |
| Python 3 | 0.0145                                     | 0.0170                                     | 0.0458                                     | 0.3803                                     | 4.8301                                     | 60.1167                                    | 757.3374                                   |
| PHP      | 0.0092                                     | 0.0161                                     | 0.1014                                     | 1.1316                                     | 13.9871                                    | 174.4720                                    | 2091.9820                                   |

* A graph which shows how long each language took to sort the numbers in the file with 100 million integers

<img src="https://raw.githubusercontent.com/Filip-Ter/QSortTest/master/LangGraph.png" alt="Graph comparing time taken to sort 100 million integers for 5 languages"width="100%" height="350px" align="right"/>


The results, of this test agree with the general belief that interpreted languages tend to be far slower than compiled ones. For example PHP took slightly over half an hour to do the same thing that took 27 seconds in C. I did expect that there would be a greater difference between the times of Java and C++. Perhaps part of the reason for this is that I tried to avoid the use of C libraries for file I/O in C++ which tend to be faster than actual C++ ones.

While this test showed interesting outcomes, it has many weaknesses. One of these is the use of libraries for file I/O, this means that the test was also measuring the implementation of the libraries, which could have affected the results. For example if a file I/O library in Java was better written than the other ones, it could give that language a skewed advantage. Another issue with this test is that it only considers languages which have their syntax influenced by C, and have many major similarities. It would have been interesting to conduct the test while including languages, which are less similar to one another, for example some of the functional languages. Also it might have been better to conduct this in a virtual environment, as it is less likely for other processes to interfere with the execution of the programs. 

If anything this little comparison shows how it is useful to have knowledge of the features of different programming languages. For example, Python is a language which is really pleasant to code in, and allows for elegant solutions, however it would not be a good idea to use it in performance-intensive applications. Knowing about differences like this between different programming languages will allow one to make sensible choices when having to implement a solution to some problem. After all the programming languages we have are just tools, which can be used to implement some solution that the programmer comes up with.


####Footnotes

[^thoare]: <http://cs.stanford.edu/people/eroberts/courses/soco/projects/2008-09/tony-hoare/quicksort.html>

[^mt]: <http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html>

[^c]: My C implementation of Quicksort (ANSI C, compiled with gcc): <https://github.com/Filip-Ter/QSortTest/blob/master/QsortC.c>

[^cpp]: My C++ Quicksort implementation (compiled with g++): <https://github.com/Filip-Ter/QSortTest/blob/master/Qsort.cc>

[^java]: My Java Quicksort implementation, complied and executed with jdk 8: <https://github.com/Filip-Ter/QSortTest/blob/master/Qsort.java>

[^py]: My Python Quicksort implementation(Python 3.3.4): <https://github.com/Filip-Ter/QSortTest/blob/master/Qsort.py>

[^php]: My PHP Quicksort implementation: <https://github.com/Filip-Ter/QSortTest/blob/master/Qsort.php>

[^mtjava]: Official Java implementation of Mersenne Twister: <http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/VERSIONS/JAVA/MTRandom.java>

[^wiki]: The pseudocode description of the algorithm that is implemented in my programs: <http://en.wikipedia.org/wiki/Quicksort#In-place_version>

[^bashtime]: The bash built-in time function was used, so not /usr/bin/time (GNU time)

[^bashscript]: The script used to run and time the programs: <https://github.com/Filip-Ter/QSortTest/blob/master/TestTime.sh>

[^writetable]: The script used to format the output of time and print a csv table: <https://github.com/Filip-Ter/QSortTest/blob/master/WriteTable.py>


