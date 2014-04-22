Title: Comparing Languages with Quicksort
Date: 2014-04-20
Tags: Quicksort, languages, speed
Category: languages
Author: Filip Ter

Language speed is often a major factor when determining how useful a programming language can be. Some applications rely on languages that can execute a large amount of instructions in a short amount of time, and programmers may in some cases use languages which have many unpleasant features, just because they can execute an algorithm faster. It would be interesting to see how some languages would fare when it comes to how long it takes them to execute the same algorithm. 

-- PELICAN_END_SUMMARY --

I decided to conduct a comparison of programming languages by using them to implement practically the same task and then timing how long each one would take to execute. For the purposes of this article, a faster program is one which can execute an implementation of an algorithm in less time. The algorithm used was quicksort, which is a well-known sorting algorithm invented by Tony Hoare in 1961.[<sup>1</sup>](#thoare) It is recursive, and it works by finding a pivot value in an array, moving all elements smaller than it to one side and the larger ones to the other, this process is repeated on the sub-sections around the pivot until the whole array is sorted.

Following up from my previous article, I thought of using the Mersenne Twister[<sup>2</sup>](#mt) algorithm to generate random 32bit integers that I would then sort using quicksort in 7 different implementations, specifically: C[<sup>3</sup>](#c), C++[<sup>4</sup>](#cpp), Java[<sup>5</sup>](#java), Python 3[<sup>6</sup>](#py), Python with PyPy[<sup>6</sup>](#py), Jython[<sup>6</sup>](#py), and PHP[<sup>7</sup>](#php). For the quicksort algorithm, I found a pseudo-code description of it on Wikipedia[<sup>8</sup>](#wiki). Using a Java implementation of Mersenne Twister[<sup>9</sup>](#mtjava), I generated 7 files all containing pseudo-random positive 32-bit integers. The files contained 100 to 100 million integers, with each file containing 10 times as many integers as the previous one. Using the description from Wikipedia, I then implemented the algorithm in the 5 languages used in the test, adding functions for reading the numbers from files and printing them for checking.  In the actual test each program was to read the contents of the file, store them in an array, sort the array using quicksort, and finally print a message that the array was sorted. The time of execution would be measured by the Bash time function.[<sup>10</sup>](#bashtime) This was mainly done so that the same function would be measuring all programs,  as using timing from different languages might produce unreliable results. In order to obtain more precise results each instance of sorting was done 5 times, and the average time was taken. In an effort to automate the task slightly more, I wrote a Bash script that would run each instance of the program 5 times, and time the execution for each run, it would then calculate the average of the times and write to a CSV table.[<sup>11</sup>](#bashscript) 

As for my initial expectations, they coincided with the usual belief about these languages. I expected the compiled languages(C, C++, Java) to be fast, and the interpreted languages to be slower. This basically follows common knowledge about these languages, but the point of the test is to see how they would actually compare, and how significant the differences would be. When it comes to the Python variants I thought that PyPy would be the fastest out of them as it was designed specifically to make python code run faster, and uses just-in-time(jit) compilation. 
	
* The table which contains the average times for all runs of each program.


<table>
	<thead>
		<tr>
			<th></th>
			<th colspan="7" align="center">Seconds taken to sort array</th>
		</tr>
		<tr>
			<th>Language</th>
			<th>10^2 integers</th>
			<th>10^3 integers</th>
			<th>10^4 integers</th>
			<th>10^5 integers</th>
			<th>10^6 integers</th>
			<th>10^7 integers</th>
			<th>10^8 integers</th>
		</tr>
	</thead>
	<tbody>	
<tr><td>C</td><td>0.0030</td><td>0.0020</td><td>0.0045</td><td>0.0235</td><td>0.2115</td><td>2.2315</td><td>23.4800</td></tr>
<tr><td>C++</td><td>0.0020</td><td>0.0030</td><td>0.0040</td><td>0.0245</td><td>0.2130</td><td>2.2295</td><td>23.4535</td></tr>
<tr><td>Java</td><td>0.1390</td><td>0.1690</td><td>0.2550</td><td>0.3735</td><td>1.4050</td><td>9.9225</td><td>95.5925</td></tr>
<tr><td>Python 3</td><td>0.0700</td><td>0.0440</td><td>0.0810</td><td>0.4890</td><td>5.6820</td><td>73.1470</td><td>989.4360</td></tr>
<tr><td>PyPy2.2.1</td><td>0.3210</td><td>0.0540</td><td>0.1320</td><td>0.2240</td><td>1.5340</td><td>9.1640</td><td>94.2570</td></tr>
<tr><td>PHP</td><td>0.2520</td><td>0.0760</td><td>0.1210</td><td>0.6650</td><td>7.5990</td><td>96.5950</td><td>1198.0580</td></tr>
<tr><td>Jython</td><td>2.0810</td><td>1.6210</td><td>2.3460</td><td>2.8450</td><td>9.5880</td><td>88.1560</td><td>1585.4810</td></tr>
</tbody>
</table>

* A graph which shows how long each language took to sort the numbers in the file with 100 million integers

![Graph comparing time taken to sort 100 million integers for 5 languages](/content/static/images/lang_graph.png)

The results, of this test agree with the general belief that interpreted languages tend to be far slower than compiled ones. C and C++ were almost the same, which could be partly because the same IO libraries were used for those languages. PyPy turned out to be practically 10 times faster than CPython, which was much more than I had expected. This could be because the jit compilation starts making a greater difference with a greater number of ints. Jython was the slowest out of all, which is not surprising at all since it is running Python code on top of the Java Virtual Machine. 

While this test showed interesting outcomes, it has many weaknesses. One of these is the use of libraries for file I/O, this means that the test was also measuring the implementation of the libraries, which could have affected the results. For example if a file I/O library in Java was better written than the other ones, it could give that language a skewed advantage. Another issue with this test is that it only considers languages which have their syntax influenced by C, and have many major similarities. It would have been interesting to conduct the test while including languages, which are less similar to one another, for example some of the functional languages.

If anything this little comparison shows how useful it is to have knowledge of the features of different programming languages. For example, Python is a language which is really pleasant to code in, and allows for elegant solutions, however it would not be a good idea to use it in performance-intensive applications. Knowing about differences like this between different programming languages will allow one to make sensible choices when having to implement a solution to some problem. After all the programming languages we have are just tools, which can be used to implement some solution that the programmer comes up with.



####Footnotes

<a id="thoare">1</a>: <http://cs.stanford.edu/people/eroberts/courses/soco/projects/2008-09/tony-hoare/quicksort.html>

<a id="mt">2</a>: <http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/emt.html>

<a id="c">3</a>: My C implementation of Quicksort (compiled with gcc): <https://github.com/Filip-Ter/QSortTest/blob/master/QsortC.c>

<a id="cpp">4</a>: My C++ Quicksort implementation (compiled with g++): <https://github.com/Filip-Ter/QSortTest/blob/master/Qsort.cc>

<a id="java">5</a>: My Java Quicksort implementation, complied and executed with jdk 8: <https://github.com/Filip-Ter/QSortTest/blob/master/Qsort.java>

<a id="py">6</a>: My Python Quicksort implementation, the same source file was used for Python 3.3.4, PyPy, and Jython: <https://github.com/Filip-Ter/QSortTest/blob/master/Qsort.py>

<a id="php">7</a>: My PHP Quicksort implementation: <https://github.com/Filip-Ter/QSortTest/blob/master/Qsort.php>

<a id="mtjava">8</a>:The pseudocode description of the algorithm that is implemented in my programs: <http://en.wikipedia.org/wiki/Quicksort#In-place_version> 

<a id="wiki">9</a>: Java implementation of Mersenne Twister: <http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/VERSIONS/JAVA/MTRandom.java>

<a id="bashtime">10</a>: The bash built-in time function was used, so not /usr/bin/time (GNU time)

<a id="bashscript">11</a>: The script used to run and time the programs: <https://github.com/Filip-Ter/QSortTest/blob/master/TestTime.sh>


