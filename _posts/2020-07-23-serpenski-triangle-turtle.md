---
layout: post
title:  "Serpenski Triangle with Python Turtle"
date:   2020-07-23
categories: python turtle fractals
---
When I was first learning to program in Python on a professional level
in Udacity's Fullstack Web Developer nanodegree program back in 2016,
one of the course modules had us try to draw our name with the Python
turtle module. As a bonus exercise, you could then try to draw a fractal.

One of the fractals I later learned was called the Serpenski triangle. I tried
to have my turtle draw it "3 levels deep" and it kind of worked. With further 
research on Wikipedia I found that there is an equation which calculates dots
on a plane in a chaotic manner but those points fall on a Serpenski triangle.
I decided to code it up and it worked! There is a [YouTube video][serpenski-youtube]
of the original script running which looks really cool.

Unfortunately I wrote this before I learned about version control and git, so the
code is long gone. With this post I am going to try to write a similar script again.

Pseudocode:
- Import the turtle module
- Instantiate a turtle
- Start an infinite loop
	- Use equation to calculate next point
	- Move the turtle to the next point
	- Place a dot at the point

Here we go. First we import the turtle module and get a window set up:
{% highlight python %}
import turtle
window = turtle.Screen()
window.bgcolor("black")
window.title("Serpenski Triangle")
{% endhighlight %}

Then we instantiate a turtle. We will call her Sherry.
{% highlight python %}
sherry = turtle.Turtle()
{% endhighlight %}

[serpenski-youtube]: https://www.youtube.com/watch?v=yiOh2H67CL4