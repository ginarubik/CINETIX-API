DROP DATABASE IF EXISTS Movies;
CREATE DATABASE Movies;
USE Movies;

CREATE TABLE `ticket_purchase`(
`Movie_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
`Movie_title` VARCHAR(100),
`Age_restrictions` INT NOT NULL,
`Time` TIME NOT NULL,
`Price` DECIMAL(10, 2) NOT NULL,
`Seat_number` VARCHAR(20) NOT NULL,
`User_name` VARCHAR(100) NOT NULL
);

INSERT INTO `ticket_purchase`
VALUES 
(1, '57 Seconds', 16, '20:30', 5.50, '17C', 'John Doe'),
(2, 'A Haunting in Venice', 16, '20:00', 5.99, '11A', 'Jane Smith'),
(3, 'DogMan', 16, '20:15', 3.50, '9B', 'Mike Johnson'),
(4, 'The Exorcist: Believer', 18, '19:50', 6.99, '13F', 'Emily Williams'),
(5, 'The Nun II', 16, '22:15', 4.50, '14D', 'David Brown'),
(6, 'The Equalizer 3', 18, '22:30', 3.99, '6E', 'Lisa Davis');

--Requirement #5.Create a MySQL database with at least 1 table
