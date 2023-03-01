-- Active: 1677629176492@@127.0.0.1@5432@backend_system@public

CREATE TABLE Vehicle_Category(
  "Category_Id" SERIAL NOT NULL ,
  "Name" VARCHAR(10),
  "Description" VARCHAR(255),
  PRIMARY KEY ("Category_Id")
);

CREATE TABLE Vehicle (
  "Vehicle_Id" SERIAL NOT NULL ,
  "Category_Id" INT,
  "Vehicle_Name" VARCHAR(50),
  "Vehicle_Price" FLOAT,
  PRIMARY KEY ("Vehicle_Id"),
  FOREIGN KEY ("Category_Id") REFERENCES Vehicle_Category("Category_Id")
);

CREATE TABLE Customer (
  "Customer_Id" SERIAL NOT NULL,
  "First_Name" VARCHAR(20) NOT NULL,
  "Last_Name" VARCHAR(20) NOT NULL,
  "Email" VARCHAR(30) NOT NULL,
  "Phone" VARCHAR(20) NOT NULL,
  "Address" VARCHAR(255) NOT NULL,
  "Created_On" DATE DEFAULT NOW() NOT NULL,
  "Updated_On" DATE DEFAULT NULL,
  PRIMARY KEY ("Customer_Id")
);

CREATE TABLE Booking (
  "Booking_Id" SERIAL NOT NULL,
  "Customer_Id " INT,
  "Vehicle_Id" INT,
  "State" INT NOT NULL DEFAULT 0 CHECK ("State" IN (0, 1)), 
  "Hire_Date" DATE DEFAULT NOW(),
  "Return_Date" DATE,
  PRIMARY KEY ("Booking_Id"),
  FOREIGN KEY ("Customer_Id ") REFERENCES Customer("Customer_Id"),
  FOREIGN KEY ("Vehicle_Id") REFERENCES Vehicle("Vehicle_Id")

);


CREATE TABLE Invoice (
  "Invoice_Id" SERIAL NOT NULL ,
  "Customer_Id" INT,
  "Booking_Id" INT,
  "Total" FLOAT,
  "Created_On" DATE DEFAULT NOW(),
  PRIMARY KEY ("Invoice_Id"),
  FOREIGN KEY ("Customer_Id") REFERENCES Customer("Customer_Id"),
  FOREIGN KEY ("Booking_Id") REFERENCES Booking("Booking_Id")
);

CREATE TABLE Email_Text(
  "Email_Text_Id" SERIAL NOT NULL,
	"Email" varchar(20) NOT NULL,
	"Text" varchar(255) NOT NULL, 
	"Created_On" DATE DEFAULT NOW(), 
	PRIMARY KEY ("Email_Text_Id")
);


