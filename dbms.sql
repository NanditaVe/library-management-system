USE sql12828123;

DROP TABLE IF EXISTS `books_records`;
CREATE TABLE `books_records` (
  `ISBN` int NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Publication` varchar(20) DEFAULT NULL,
  `Author` varchar(25) DEFAULT NULL,
  `Genre` varchar(20) DEFAULT NULL,
  `Quantity` int DEFAULT NULL,
  `Date_of_purchase` date DEFAULT NULL,
  `Price` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`ISBN`)
);

INSERT INTO `books_records` VALUES (978950001,'Harry Potter','Bloomsbury','J.K.Rowling','Fantasy',8,'2019-11-17',499.00),(978950002,'Encyclopedia','Penguin Books','Denis Diderot','Science',5,'2018-01-23',999.00),(978950003,'Hardy Boys','Wanderer books','Franklin.W','Fiction',10,'2019-12-10',299.00),(978950004,'The Great Adventure','Penguin Books','John Smith','Fiction',4,'2016-09-19',399.00),(978950005,'The Silent Waters','HarperCollins','Emma Watson','Romance',1,'2019-11-14',499.00),(978950006,'Tech in the 21st Century','TechPress','Daniel Brown','Technology',9,'2022-10-23',249.00),(978950007,'Journey to the Unknown','Random House','Sarah Lee','Mystery',10,'2018-10-15',350.00),(978950008,'Digital Dreams','Pearson','Michael Clarke','Science Fiction',7,'2014-12-12',275.00),(978950009,'Fictional Realities','Oxford Press','Anna Green','Fiction',3,'2015-10-15',180.00),(978950010,'The Mind of a Genius','Wiley','Robert Davis','Biography',5,'2017-01-10',799.00),(978950011,'History Revisited','Cambridge','James Walker','History',2,'2020-03-13',650.00),(978950012,'Cooking with Love','Gourmet Publishing','Lily White','Cookbook',4,'2018-05-26',599.00),(978950013,'The Painted Sky','Artistic Press','Chloe Mitchell','Fantasy',6,'2019-07-20',200.00),(978950014,'Once Upon a Time','Scholastic','Michael John','Children''s',8,'2015-02-15',199.00),(978950015,'The Old Mansion','Vintage Books','Olivia Stone','Horror',10,'2016-01-20',675.00),(978950016,'Beyond the Stars','AstroPress','Lucas Scott','Space Fiction',5,'2017-07-17',800.00),(978950017,'Understanding AI','TechWorld','Sophia Williams','Technology',3,'2016-02-27',299.00),(978950018,'The Desert Mirage','Desert Books','Liam Roberts','Adventure',9,'2018-12-29',150.00),(978950019,'Whispers in the Wind','Scribe Publications','Ella Wilson','Romance',3,'2020-07-19',600.00),(978950020,'Secrets of the Sea','Oceanic Press','Ethan King','Non-fiction',7,'2019-08-25',799.00),(978950021,'Shadows of Time','Eclipse Press','Natalie Gray','Thriller',10,'2016-06-16',499.00),(978950022,'The Electric Soul','Volt Publications','Victor Ford','Science Fiction',6,'2020-09-28',500.00),(978950023,'City of Secrets','Urban Press','Jessica Brown','Crime',7,'2019-05-05',999.00),(978950024,'Quantum Leap','Quantum Books','Johnathan Clark','Science',1,'2016-12-11',300.00),(978950025,'The Golden Key','Sunrise Publishing','Rebecca Adams','Fantasy',1,'2021-12-21',675.00),(978950026,'The Wild Path','Earthly Press','William Harris','Nature',8,'2019-04-25',220.00),(978950027,'Into the Abyss','Deep Books','Gabrielle Taylor','Horror',9,'2021-09-08',850.00),(978950028,'The Secret Garden','Green House','Charlotte White','Classic',4,'2018-10-18',1199.00),(978950029,'Uncharted Waters','BlueOcean Press','Andrew Moore','Adventure',2,'2017-06-18',525.00),(978950030,'The Hidden World','Mystery House','Grace Lee','Fantasy',5,'2017-08-14',750.00);

DROP TABLE IF EXISTS `student_records`;
CREATE TABLE `student_records` (
  `Admno` int NOT NULL,
  `Student_Name` varchar(30) NOT NULL,
  `Class` varchar(5) DEFAULT NULL,
  `Section` varchar(5) DEFAULT NULL,
  `Roll_No` int DEFAULT NULL,
  `Book_Issued` varchar(50) DEFAULT NULL,
  `Issue_Date` date DEFAULT NULL,
  `Return_Status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Admno`)
);

INSERT INTO `student_records` VALUES (3301,'Ayush Patel','VIII','A',18,'Hardy Boys','2023-11-17','Pending'),(3302,'Ankit singh','VIII','B',11,NULL,NULL,NULL),(3303,'Sonali Verma','VIII','B',33,'Harry Potter','2024-09-14','Pending'),(3304,'Rajesh Kumar','VIII','A',22,'Deep Books','2023-08-12','Returned'),(3305,'Tanmay Bhatt','IX','A',1,'Digital Dreams','2024-03-12','Pending'),(3306,'Asish Chanchalani','IX','B',41,'Quantum Leap','2024-05-22','Pending'),(3307,'Tanmay Singh','IX','A',29,NULL,NULL,NULL),(3308,'Rohini Verma','IX','B',10,'The Golden Key','2024-08-14','Returned'),(3309,'Mansi Singh','X','A',19,'Encyclopedia','2024-06-22','Returned'),(3310,'Shreya Rajput','X','B',48,'Shadows of Time','2024-08-06','Returned'),(3311,'Lakshya verma','X','B',6,NULL,NULL,NULL),(3312,'Shaurya Gupta','X','B',16,'Once Upon a Time','2024-11-11','Pending'),(3313,'Aryan Rajput','XI','B',22,'History Revisited','2024-09-01','Pending'),(3314,'Sanchay Singh','XI','A',26,'Harry Potter','2024-09-10','Pending'),(3315,'Divyam Patel','XI','A',41,NULL,NULL,NULL),(3316,'Gourav Sarkar','XI','B',18,'The Silent Waters','2024-06-19','Returned'),(3317,'LuvKush','XII','A',13,'The Secret Garden','2024-02-19','Returned'),(3318,'Diljit Dosanjh','XII','B',33,NULL,NULL,NULL),(3319,'Adarsh Singh','XII','A',27,'The Old Mansion','2024-08-30','Pending'),(3320,'Shivansh Roy','XII','B',17,'Beyond The Stars','2024-10-30','Pending');

DROP TABLE IF EXISTS `teacher_records`;
CREATE TABLE `teacher_records` (
  `Id_No` int NOT NULL,
  `Teacher_Name` varchar(30) NOT NULL,
  `Book_Issued` varchar(50) DEFAULT NULL,
  `Issue_Date` date DEFAULT NULL,
  `Return_Status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`Id_No`)
);

INSERT INTO `teacher_records` VALUES (100101,'Mr.Kamlesh Mehra','Fictional Realities','2024-01-28','Returned'),(100102,'Mr.Shreyas Das','Beyond the Stars','2024-08-15','Pending'),(100103,'Mrs.Meenal Bajpai',NULL,NULL,NULL),(100104,'Mr.Parth Grover','City of Secrets','2024-07-30','Pending'),(100105,'Mr.Ashutosh Tripathi',NULL,NULL,NULL),(100106,'Mrs.Ankita Kashyap',NULL,NULL,NULL),(100107,'Mr.Harish Sahu','Quantum Leap','2023-12-24','Returned'),(100108,'Mrs.Ayushi Kamra','City of Secrets','2024-10-16','Pending'),(100109,'Mr.Ravindra Tiwari',NULL,NULL,NULL),(100110,'Mrs.Shilpa Rathee','Into the Abyss','2024-02-25','Pending');
