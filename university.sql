-- Create the university database
CREATE DATABASE IF NOT EXISTS university;
USE university;

-- Create the Companies table
CREATE TABLE IF NOT EXISTS Companies (
    CompanyID INT PRIMARY KEY AUTO_INCREMENT,
    CompanyName VARCHAR(255) NOT NULL,
    Industry VARCHAR(100),
    Description TEXT,
    Website VARCHAR(255),
    ContactEmail VARCHAR(255)
);

-- Insert data into the Companies table
INSERT INTO Companies (CompanyName, Industry, Description, Website, ContactEmail)
VALUES
    ('Google', 'Technology', 'A leading multinational technology company specializing in Internet-related services and products.', 'https://www.google.com.mx/', '[email address removed]'),
    ('Microsoft', 'Technology', 'A multinational technology corporation that develops, manufactures, licenses, supports, and sells computer software.', 'https://www.microsoft.com/en-us/store/b/pc', '[email address removed]'),
    ('Amazon', 'Technology, Retail', 'A multinational technology company focusing on e-commerce, cloud computing, digital streaming, and artificial intelligence.', 'https://www.amazon.com/', '[email address removed]'),
    ('McKinsey & Company', 'Consulting', 'A global management consulting firm that advises businesses on strategy, marketing, operations, and organization.', 'https://www.mckinsey.com/', '[email address removed]'),
    ('J.P. Morgan Chase', 'Finance', 'A leading global financial services firm offering investment banking, asset management & consumer banking.', 'https://www.jpmorganchase.com/', '[email address removed]');

-- Create the JobRoles table
CREATE TABLE IF NOT EXISTS JobRoles (
    JobRoleID INT PRIMARY KEY AUTO_INCREMENT,
    CompanyID INT,
    RoleName VARCHAR(100) NOT NULL,
    EligibilityCriteria TEXT,
    Salary DECIMAL(10, 2),
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID) ON DELETE CASCADE
);

-- Insert data into the JobRoles table
INSERT INTO JobRoles (CompanyID, RoleName, EligibilityCriteria, Salary)
VALUES
    (1, 'Software Engineer', 'Strong programming skills in Java, Python or C++. Excellent problem-solving skills.', 120000.00),
    (2, 'Software Development Engineer (SDE)', 'Strong algorithms and data structures knowledge. Experience with cloud platforms.', 135000.00),
    (3, 'Product Manager', 'Strong analytical and communication skills. Experience with product development life cycle.', 110000.00),
    (4, 'Business Analyst', 'Excellent analytical and communication skills. Experience with data analysis tools.', 100000.00),
    (5, 'Investment Banking Analyst', 'Strong financial modeling and analytical skills. Excellent communication and teamwork abilities.', 85000.00);

-- Create the Placements table with additional information
CREATE TABLE IF NOT EXISTS Placements (
    PlacementID INT PRIMARY KEY AUTO_INCREMENT,
    JobRoleID INT,
    Year INT,
    NumberOfStudents INT,
    RoleName VARCHAR(100), -- Additional field
    EligibilityCriteria TEXT, -- Additional field
    Salary DECIMAL(10, 2), -- Additional field
    FOREIGN KEY (JobRoleID) REFERENCES JobRoles(JobRoleID) ON DELETE CASCADE
);

-- Insert data into the Placements table
INSERT INTO Placements (JobRoleID, Year, NumberOfStudents, RoleName, EligibilityCriteria, Salary)
VALUES
    (1, 2022, 20, 'Software Engineer', 'Strong programming skills in Java, Python or C++. Excellent problem-solving skills.', 120000.00),
    (2, 2022, 10, 'Software Development Engineer (SDE)', 'Strong algorithms and data structures knowledge. Experience with cloud platforms.', 135000.00),
    (3, 2022, 12, 'Product Manager', 'Strong analytical and communication skills. Experience with product development life cycle.', 110000.00),
    (4, 2022, 15, 'Business Analyst', 'Excellent analytical and communication skills. Experience with data analysis tools.', 100000.00),
    (5, 2022, 3, 'Investment Banking Analyst', 'Strong financial modeling and analytical skills. Excellent communication and teamwork abilities.', 85000.00);

-- Display the updated Placements data
SELECT * FROM Placements;

-- Drop the ContactEmail field from the Companies table
ALTER TABLE Companies
DROP COLUMN ContactEmail;


