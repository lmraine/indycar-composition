# IndyCar Composition Lab

In this lab, you will be extending the IndyCar example from class using composition and aggregation to model a car's wheels, the IndyCar teams, and a race. 

## Set Up
<ol>
	<li>Create new anaconda environment using these commands</li>
	<ul>
		<li>conda create --name indycar_lab python=3.13.1</li>
		<li>conda activate indycar_lab</li>
	</ul>
	<li>Pull starter code from GitHub Classroom</li>
	<li>Open in VS code and switch to the indycar_lab anaconda environment</li>
	<li>When the lab is complete, push code to GitHub Classroom</li>
</ol>

## Instructions
<ol>
  <li><strong>Starter Code</strong></li>
  <p>The starter code include the Car, Driver, and Engine class we implemented together. You will add and extend to this starter code.</p>
  <li><strong>Wheel Class</strong></li>
  <p>The wheel class models the wheels of a car and should have the following attributes and methods:</p>
  <ol>
    <li>type (required)</li>
  </ol>
  <br>
  <li><strong>Car Class</strong></li>
  <p>Make the following additions to the car class</p>
  <ol>
    <li>Ensure a car has 4 wheels. (Hint: you will need to choose either composition or aggregation. Only one approach will be correct.)</li>
  </ol>
  <br>
  <li><strong>Team Class</strong></li>
  <p>The team class represents the different IndyCar teams. You will create a new class with the following attributes and methods:</p>
  <ol>
    <li>name (required)</li>
    <li>drivers: Ensure that a team can have multiple drivers. (Hint: you will need to choose either composition or aggregation. Only one approach will be correct.)</li>
    <li>add_driver() method: adds a driver to the team.</li>
    <li>list_drivers() method: returns the names of all the drivers on the team.</li>
  </ol>
  <br>
  <li><strong>Race Class</strong></li>
  <p>This class will structure a simulated race and will have the following attributes and methods:</p>
  <ol>
    <li>name (required)</li>
    <li>cars: Ensure that a race can have multiple cars (Hint: you will need to choose either composition or aggregation. Only one approach will be correct.)</li>
    <li>start() method: This method will return the cars and drivers in the race sorted by the car's horsepower in this format: "{make} {model} - {driver name}</li>
    <li>winner() method: randmoly chooses a winner and returns the winner of the race</li>
  </ol>
</ol>
</ol>

## Additional Notes
<ol>
  <li>All classes should be written in the car.py file. Do not create new files for each class.</li>
  <li>You will need to use the random module for the winner method.</li>
</ol>
