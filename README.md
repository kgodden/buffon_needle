# buffon_needle
A Monte Carlo Simulation of Buffon's Needle to Estimate Pi _without_ using the value of Pi or any trigonometry functions (written in Python 2.7)

I have been interested in Buffon's needle ever since I read the book 'Mathematics and the Imagination' (https://en.wikipedia.org/wiki/Mathematics_and_the_Imagination) as a child.  I used to spend many happy hours throwing matchsticks onto lined paper counting the number of hits and misses and I was eventually able determine that the value of Pi is about 3! ;-)

A description of the Buffon's Needle problem can be found here: https://en.wikipedia.org/wiki/Buffon%27s_needle_problem

Later when I learned about Monte Carlo simulation in University I thought that Buffon's Needle was a perfect candidate.  I fairly quickly wrote some code and got a reasonably satisfactory estimate for Pi.  However one thing didn't seem right to me, my code referenced the value of Pi as part of it's calculations - this annoyed me as it was supposed to be estimating the value of Pi in the first place (in a way its self-referential)

I looked at other simulations that I could find on-line and they all either referenced Pi or used the trigonometry functions!

I thought that it would be quite easy to reformulate the code without Pi or acos() & asin() and the other trig functions, but I couldn't figure out how to, eventually I gave up.

Years later I came across a method for randomly picking a point on a circle with uniform distribution, it occurred to me that this is just what I needed to reformulate my simulation without any Pi or trig references.  The method is summarised here:


http://mathworld.wolfram.com/CirclePointPicking.html


That's what this code attempts to do it uses this method to randomly throw the needles, it is a bit slower than using the traditional method but seems to work well enough, and now I can relax for a bit!  I don't know if it is mathematically coherent but I am happy enough with it for now as it seems to give similar results to traditional methods.  If I were being thorough I should compare the random distributions produced by both methods...

PS I also found this [paper](http://www.dca.iag.usp.br/material/cfmraupp/Climatologia-1/Wang2014.pdf) which mentions the (as they call it) paradox of the self referential simulation techniques (calculating Pi by referencing Pi).  They present an algorithm for removing this paradox, which I haven't quite got my head around yet!

For a less involved monet carlo simulation for estimating Pi, please see:

https://github.com/kgodden/monte_carlo_pi

Please note that it is believed that both methods can be used when stranded on a dessert island for estimating Pi to one or two decimal places! ;-)
