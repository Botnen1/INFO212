# 212
Assignment in INFO212
Dette er oblig 4 i INFO212


Oppgavetekst:


 INFO212 22H / System Development
Assignment 04
Purpose
The purpose of this exercise is:
 PracEcing Django!webAPI development Tasks
In this exercise you will pracEce collaboraEve soKware development and version control us- ing Git.
- One team member creates a remote repository containing a Django project and all neces- sary files.
- All team members should implement a part of the Django project which is described in more detail below. One of the purposes of this exercise is to practice collaborative work on GitHub, so all team members should clone the remote repository and create a local copy of the project on their computer.
- Changes are pushed to the GitHub repository.
WebAPI development with Django res<ul framework
In this exercise you will have to implement WebAPIs for a car rental company. In this exercise you may consider that customers rent cars for non-determinisEc Eme. For simplicity you do not need to consider the date/Eme of rental. For example, if a car #1 is available, it can be rented to a customer John. If car #1 is booked for John, it cannot be booked by any other customer. Again, if John has booked a car, he cannot book any other car. If John returns car #1, he is allowed to rent other cars.
Following funcEonaliEes must be implemented.
- Create, Read, Update and Delete ‘Cars' with basic informaEon e.g., make, model, year, lo-
caEon, status (i.e., available, booked, rented, damaged)
- Create, Read, Update and Delete ‘Customer’ with basic informaEon e.g., name, age, ad-
dress.
- Create, Read, Update and Delete ‘Employee’ with basic informaEon e.g., name, address,
branch.
- Implement an endpoint ‘order-car’ where a customer-id, car-id is passed as parameters.
The system must check that the customer with customer-id has not booked other cars. The system changes the status of the car with car-id from ‘available’ to ‘booked’.
•
• PracEcing Git/Github

 - Implement an endpoint ‘cancel-order-car’ where a customer-id, car-id is passed as para- meters. The system must check that the customer with customer-id has booked for the car. If the customer has booked the car, the car becomes available.
- Implement an endpoint ‘rent-car’ where a customer-id, car-id is passed as parameters. The system must check that the customer with customer-id has a booking for the car. The car’s status is changed from ‘booked’ to ‘rented’.
- Implement an endpoint ‘return-car’ where a customer-id, car-id is passed as parameters. Car’s status (e.g., ok or damaged) during the return will also be passed. The system must check that the customer with customer-id has rented the car. The car’s status is changed from ‘booked’ to ‘available’ or ‘damaged’.
- Use postman to check the funcEonality of your implementaEon. What to submit
Each team should submit zip file containing the Django project and a readme file with Git- Hub repository address.
