# buffon_needle
A Monte Carlo Simulation of Buffon's Needle to Estimate Pi _without_ using the value of Pi or any trigonometry functions (written in Python 2.7)

I have been interested in Buffon's needle ever since I read the book 'Mathematics and the Imagination' (https://en.wikipedia.org/wiki/Mathematics_and_the_Imagination) as a child.  I used to spend many happy hours throwing matchsticks onto lined paper counting the number of hits and misses and I was eventually able determine that the value of Pi is about 3! ;-)

A description of the Buffon's Needle problem can be found here: https://en.wikipedia.org/wiki/Buffon%27s_needle_problem

Later when I learned about Monte Carlo simulation in University I thought that Buffon's Needle was a perfect candidate.  I fairly quickly wrote some code and got a reasonably satisfactory estimate for Pi.  However one thing didn't seem right to me, my code referenced the value of Pi as part of it's calculations - this annoyed me as it was supposed to be estimating the value of Pi in the first place!

I looked at other simulations that I could find on-line and they all either referenced Pi or used the trigonometry functions!

I thought that it would be quite easy to reformulate the code without Pi or acos() & asin() and the other trig functions, but I couldn't figure out how to, eventually I gave up.

Years later I came across a method for randomly picking a point on a circle with uniform distribution, it occurred to me that this is just what I needed to reformulate my simulation without any Pi or trig references.  The method is summarised here:


http://mathworld.wolfram.com/CirclePointPicking.html


That's wha tthis code attempts to do, it is a bit slower than using the traditional method but seems to work well enough, and now I can relax for a bit!
