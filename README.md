# Description
This repo is to document & create a tutorial to learn **Python**. Below is a list of useful links and definitions that may be of use. My focus is on the basics and branching out to work with data collection and analysis. 

## <a id="toc"></a>Table of Contents
   * [What is Python](#what)
   * [Why Learn Python](#why)
   * [Getting Started](#start)
   * [The Fundamentals](#basics)
   
## <a id="advice"></a> Personal Coding Advice & Experience
  #### Why Coding? 
   * Learn something new daily with a vast surplus of information & constant advancements in technology.
   * Career is in high demand AKA high salary. Rewards are priceless even without the high salary.
   * Flexibility to work remotely and save time on commutes.
   * Freedom to pursue personal projects and improve quality of life.
   * Community is enthusiastic to share wealth of knowledge with fellow developers.
   
  #### Keys to Success
   * Get ready to a master at Google. No need to memorize everything.   
   * Accept and embrace failure quickly. Avoid trying to be a perfectionist.
   * Troubleshooting and debugging mistakes thoroughly to find a solution is important for learning.
   * Type the code out until you feel comfortable enough to copy paste. Practice makes perfect.
   * You are essentially learning how to learn on the first go around.  
   * Be very specific in your questions and always research before asking.
   * Write easy to read code and use proper indentation. 
    * [Clean Code With Uncle Bob](https://www.youtube.com/watch?v=-1CuAiKdBQs) 

***
## <a id="what"></a>What is Python?
  * Interpreted language that runs on *Windows* , *Mac OS X*, *Linux*, etc.
  * Supports object-oriented, procedural, and functional programming. 
  * Supports basic data types such as strings and numbers and complex data types like lists and dictionaries.
  * Strongly typed but is also dynamically typed, meaning you are freed from worrying about variable declarations.
 
  [Python Landing Page](https://www.python.org/) <br />
  [What is Python?](https://www.python.org/doc/essays/blurb/)

###### [TOC](#toc)
***
## <a id="why"></a>Why Learn Python?

  ##### EASY TO USE 
   * Focus on programming concepts versus learning syntax.
   * User friendly documentation and installation.
   * Developers contribute religiously to community by creating Python libraries.
  ##### POWERFUL
   * Google, Dropbox, Spotify all use Python.
   * Allows for cross-platform compatibility.
   * Suited for rapid delivery and maintenance. 
   * Python developers tend to have higher salaries than other languages. 
  ##### VERSATILE
   * Client and server side capabilities.
   * Used for machine learning, game engines, artificial intelligence and data science.
  ##### [TOC](#toc)

***
## <a id="start"></a>Getting Started
  *Personal preference but executable file download is the simplest option. Download and install Python based off your operating system and system type.*

  #### WINDOWS DOWNLOAD
   * [Windows Download](https://www.python.org/downloads/windows/)
   * [YouTube](https://www.youtube.com/watch?v=i-MuSAwgwCU)

  #### MAC OS X DOWNLOAD
   * [Mac OS X Download](https://www.python.org/downloads/mac-osx/)
   * [YouTube](https://www.youtube.com/watch?v=TgA4ObrowRg)

  #### IDE SELECTION
   *Choose and download the IDE of your choosing. I pay for `JetBrains ItelliJ` because I love it.*
   * [IDE Download Options](https://www.guru99.com/python-ide-code-editor.html)  
     
  #### [TOC](#toc)
***
## <a id="basics"></a>The Fundamentals

  #### VARIABLES  
  *When a program is running, everything the program needs is stored into the computer's memory. In Python, a variable is a reserved location in memory to store values. In a program it gives data to the computer for processing.* 
  <br />
  <br />
  
  <details>
    <summary>Rules for Variable Names</summary>
    <ul>
        <li>Must begin with a letter(upper or lower case) or an underscore_ character</li>
        <li>Can contain letters, numbers or underscore characters but can not begin with a number</li>
        <li>Variables are case sensitive so example and Example refer to 2 different variables</li>
        <li>Variables are names/labels that are bound to a value with the use of =.</li>
        <li><a href="https://realpython.com/python-variables/#object-references">Variables Explained</a></li>
    </ul>
  </details>
   
   #### DATA TYPES
   *Strongly typed but is also dynamically typed, meaning you are freed from worrying about variable declarations. Python's built-in data types include:* 
   1. numeric
   2. iterator
   3. sequence(also iterators)
   4. mapping
   5. file
   6. class
   7. exception
    
   <details>
       <summary>Strings</summary>
       <ul>
           <li>Strings are a sequence of characters, and a derived data type.</li>
           <li>Immutable: Once they are defined, they cannot be changed. </li>
           <li>Built-in Python methods such as `replace()`, `join()`,`split()`, etc.</li>
       </ul>
   </details>
   <details>
      <summary>Numeric</summary>
      <p>Keep in mind it is important to understand the difference in the different numeric types.</p>
      <h4>int</h4>
      <ul>
          <li>Whole numbers with no fractional part or decimals.</li>
          <li>Computations using integers are significantly faster than using floating point numbers.</li>
          <li>Python 3 has no maximum size limitation for ints. You will run out of memory before you can can exceed the size limit.</li>
          <li>Python 2 used to have a long for large numbers but has been replaced by int in latest edition.</li>
      </ul>
      <h4>float</h4>
      <ul>
        <li>Real numbers or numbers having a fractional part after the decimal.</li>
        <li>Max float value on 64 bit computer is 1.797e308 or move the decimal 308 places right</li>
        <li>Minimum float value is 2.25e-308 or 307 zeros before the decimal point.</li>
        <li>52 digits of precision generally enough, but if you require more precision you can use a Decimal data type.</li>
      </ul>
      <h4>complex</h4>
      <p>Contain a real and an imaginary part, based on square root of -1. More for advanced mathematics/engineering topics.</p>
   </details>
     
  ##### [TOC](#toc)             
***
## Authors
**Muhammet Aydin** [Muhammet Aydin](https://github.com/muhammeta7)
