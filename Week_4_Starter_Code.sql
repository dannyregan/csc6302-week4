/* Week 4 Starter Code
Run in MySQL Workbench every time you test your program  */

/* DO NOT ADD CUSTOM SQL CODE */

DROP DATABASE IF EXISTS `mrc`;
CREATE DATABASE IF NOT EXISTS `mrc`; 
USE `mrc`;

DROP TABLE IF EXISTS `vessels`;

CREATE TABLE `vessels` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `CostPerHour` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`ID`)
);

INSERT INTO `vessels` VALUES 
	(1,'Ocean Voyager',200.00),
	(2,'Sea Breeze',100.00),
    (3,'The Warrior',150.00);


DROP TABLE IF EXISTS `passengers`;

CREATE TABLE `passengers` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `getsSeasick` tinyint DEFAULT NULL,
  PRIMARY KEY (`ID`)
);

INSERT INTO `passengers` VALUES 
	(1,'Emily Clark','456 Pine St, Rivertown, MA, 23456','978-555-5678',NULL),
	(2,'Michael Lee','789 Maple Ave, Beachside, MA, 34567','978-555-8765',NULL),
    (3,'Jessica Adams','654 Birch Rd, Seaside, MA, 56789','978-555-8760',NULL),
    (4,'Sarah Johnson','321 Elm St, Townsville, MA, 45678','978-555-4321',NULL),
    (5,'John Smith','123 Oak St, Cityville, MA, 01234','413-555-1234',NULL);


DROP TABLE IF EXISTS `trips`;

CREATE TABLE `trips` (
  `vesselID` int NOT NULL,
  `passengerID` int NOT NULL,
  `dateandtime` datetime NOT NULL,
  `lengthoftrip` decimal(5,2) NOT NULL,
  `totalpassengers` int NOT NULL,
  PRIMARY KEY (`vesselID`,`passengerID`,`dateandtime`),
  FOREIGN KEY (`vesselID`) REFERENCES `vessels` (`ID`),
  FOREIGN KEY (`passengerID`) REFERENCES `passengers` (`ID`)
);

INSERT INTO `trips` VALUES 
	(1,1,'2025-03-01 09:00:00',3.00,3),
	(1,1,'2025-03-02 10:00:00',2.00,3),
    (1,1,'2025-03-05 11:30:00',3.50,3),
    (1,1,'2025-03-09 09:30:00',1.50,3),
    (1,2,'2025-03-03 11:00:00',4.00,6),
    (1,2,'2025-03-04 09:30:00',2.00,6),
    (1,2,'2025-03-10 10:30:00',3.00,6),
    (1,2,'2025-03-12 08:45:00',3.50,6),
    (1,2,'2025-03-14 07:00:00',3.00,6),
    (2,3,'2025-03-06 07:00:00',2.00,2),
    (2,3,'2025-03-10 08:00:00',2.00,2),
    (2,3,'2025-03-11 09:30:00',2.00,2),
    (2,4,'2025-03-03 12:30:00',2.50,4),
    (2,4,'2025-03-04 07:45:00',3.00,4),
    (2,4,'2025-03-09 07:00:00',3.00,4),
    (2,4,'2025-03-15 11:30:00',3.50,4),
    (3,5,'2025-03-02 08:30:00',1.50,5),
    (3,5,'2025-03-10 12:00:00',2.50,5);

CREATE VIEW AllTrips AS
	SELECT 
	  Trips.DateAndTime,
	  Trips.LengthOfTrip,
	  Vessels.Name AS Vessel,
	  Passengers.Name AS Passenger,
	  Passengers.Address,
	  Passengers.Phone,
	  Trips.TotalPassengers,
	  CONCAT('$', FORMAT(Trips.LengthOfTrip * Vessels.CostPerHour, 2)) AS Cost
	FROM Trips
	JOIN Passengers ON Trips.PassengerID = Passengers.ID
	JOIN Vessels ON Trips.VesselID = Vessels.ID
	ORDER BY Trips.DateAndTime;
    
CREATE VIEW TotalRevenuebyVessel AS
	SELECT
		Vessel, concat('$',sum(cast(replace(Cost,'$','') AS Decimal(10,2)))) AS TotalRevenue
	FROM alltrips
    GROUP BY Vessel;

/* Functions */

DROP FUNCTION IF EXISTS getVesselID;    
Delimiter $$

CREATE FUNCTION getVesselID(myVesselName VARCHAR(50))
RETURNS INT DETERMINISTIC
BEGIN
	DECLARE foundVesselID INT;
    SELECT ID INTO foundVesselID 
    FROM Vessels
    WHERE Name = myVesselName;
	
    IF foundVesselID is null
    THEN SET foundVesselID = -1;
    END IF;

    RETURN foundVesselID;
END$$

Delimiter ; 


DROP FUNCTION IF EXISTS getPassengerID;    
Delimiter $$

CREATE FUNCTION getPassengerID(myPassengerName VARCHAR(50))
RETURNS INT DETERMINISTIC
BEGIN
	DECLARE foundPassengerID INT;
    SELECT ID INTO foundPassengerID 
    FROM Passengers
    WHERE Name = myPassengerName;
	
    IF foundPassengerID is null
    THEN SET foundPassengerID = -1;
    END IF;

    RETURN foundPassengerID;
END$$

Delimiter ; 

/* Procedures */

DROP PROCEDURE IF EXISTS addPassenger;

DELIMITER $$

CREATE PROCEDURE addPassenger(IN passName VARCHAR(50), passAddress VARCHAR(50), passPhone VARCHAR(50))

BEGIN
	DECLARE foundPassengerID INT;
    
	SELECT getPassengerID(passName) INTO foundPassengerID;
    
    IF foundPassengerID = -1
    THEN INSERT INTO Passengers (name, address, phone)
    VALUES (passName, passAddress, passPhone);
    END IF;
    
    SELECT getPassengerID(passName) AS PassengerID;
    
END$$

DELIMITER ;


DROP PROCEDURE IF EXISTS addVessel;

DELIMITER $$

CREATE PROCEDURE addVessel(IN myVesselName VARCHAR(50), myVesselCPH DECIMAL(6,2))

BEGIN
	DECLARE foundVesselID INT;
    
	SELECT getVesselID(myVesselName) INTO foundVesselID;
    
    IF foundVesselID = -1
    THEN INSERT INTO Vessels (name, CostPerHour)
    VALUES (myVesselName, myVesselCPH);
    END IF;
    
    SELECT getVesselID(myVesselName) AS VesselID;
    
END$$

DELIMITER ;


DROP PROCEDURE IF EXISTS addTrip;

DELIMITER $$

CREATE PROCEDURE addTrip(myVesselName VARCHAR(50), myPassengerName VARCHAR(50), myDateandTime DATETIME,
						 myLengthofTrip decimal(5,2), myTotalPassengers INT)

BEGIN
	DECLARE foundVesselID INT;
    DECLARE foundPassengerID INT;
    DECLARE missingData INT;
    
	SELECT GETVESSELID(myVesselName) INTO foundVesselID;
	SELECT GETPASSENGERID(myPassengerName) INTO foundPassengerID;
    
    IF foundVesselID = -1 AND foundPassengerID = -1
		THEN SELECT -3 AS NotFound;
    ELSEIF foundPassengerID = -1
		THEN SELECT -2 AS NotFound;
    ELSEIF foundVesselID = -1
		THEN SELECT -1 AS NotFound;
    ELSE INSERT INTO trips
		VALUES(foundVesselID, foundPassengerID, myDateandTime, myLengthofTrip, myTotalPassengers);
	END IF;
    
END;$$

DELIMITER ;


/* DO NOT ADD CUSTOM SQL CODE */
