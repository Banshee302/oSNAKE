# oSNAKE Programming Language

You must install JRE (Java runtime Enviroment) first to be able to use oSNAKE, heres the dependency links:
Java JRE:
https://www.java.com/en/download/

Please credit the oSNAKE programming language if your using it if you can, just a text file saying made in oSNAKE is good enough.

# Documentation

*Variables*
oSNAKE recognises only numerical values as variables, for example;
DATA=1
which then is held in the script and parsed as a variable which could then be called like this;
(example)
if DATA=1 then print ("oSNAKE Script!")

and then the output should be;
"oSNAKE Script!" if DATA=1.

you can change and update variables when certain lines finish, for example;
DATA=1
if DATA=1 then print ("Hello!") DATA=2
if DATA=2 then print ("World!")

this should output this:
Hello!
World!

Every script needs a Variable to function, oSNAKE does not allow string variables, strictly integers

# JVM

oSNAKE utilizes JVM and java bytecode for speed and efficiency.

You must have JRE or JDK installed to run oSNAKE

**IF YOU PLAN ON BUILDING OSNAKE FROM SOURCE YOU WILL NEED JAVAC WHICH YOU NEED JDK FOR**