
%load_ext sql

#Retrieving All Data.
%%sql
select * from astronauts;

#Counting Astronauts by Status.
Select status, count(status) as Number
from astronauts
group by status;

#Counting Astronauts by Military Branch.
Select Military_Branch, count(Military_Branch) as Number
from astronauts
group by Military_Branch;

#Top 5 Military Ranks Among Astronauts.
Select Military_Rank, count(Military_Rank) as Number
from astronauts
group by Military_Rank
order by Number desc
limit 5;

#Count of Astronauts by Gender.
Select Gender, count(Gender) as Number
from astronauts
group by Gender;

#Average Life Expectancy of Astronauts.
select round(avg(life_Expectancy)) Average_Life_Expectancy from (
select 
    case 
    when status ='Deceased' then (year(Death_Date) - year(Birth_Date))
    else (2023- year(Birth_Date)) end as life_Expectancy
    from astronauts) a;

#Average Life Expectancy of Female Astronauts.
select round(avg(life_Expectancy)) FemaleAverage_Life_Expectancy from (
select 
    case 
    when status ='Deceased' then (year(Death_Date) - year(Birth_Date))
    else (2023- year(Birth_Date)) end as life_Expectancy
    from astronauts
where gender='Female') a;

#Average Life Expectancy of Male Astronauts.
select round(avg(life_Expectancy)) MaleAverage_Life_Expectancy from (
select 
    case 
    when status ='Deceased' then (year(Death_Date) - year(Birth_Date))
    else (2023- year(Birth_Date)) end as life_Expectancy
    from astronauts
where gender='Male') a;

#Top 10 Graduate Majors Among Astronauts.
Select Graduate_Major, count(Graduate_Major) as Number
from astronauts
group by Graduate_Major
order by Number desc
limit 10;

#Astronaut Education Statistics.
select count(*) as Number_of_Astronauts, 
count(Undergraduate_Major) as Astronauts_with_Undergraduate_Degrees,
count(Graduate_Major) as Astronauts_with_Graduate_Degrees
from astronauts;

#Top 5 States of Birth for Astronauts.
select STATE,NUMBER from (
select SUBSTRING_INDEX(Birth_Place, ',', -1) as STATE, count(*) NUMBER 
from astronauts 
group by State ) a
order by NUMBER desc
limit 5;

#Average Space Flights and Spacewalks per Astronaut.
select round(avg(Space_Flights),2) as Average_Number_Of_Space_Flight,
round(avg(Space_Walks),2) as Average_Number_Of_Space_Walks
from astronauts;


