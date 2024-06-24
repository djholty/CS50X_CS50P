-- Keep a log of any SQL queries you execute as you solve the mystery.

.schema -- to get a sense of the data stored in the database

-- query the crime_scene_reports table to find the description of the crime
SELECT * FROM crime_scene_reports
WHERE year = 2021 AND month = 7 AND day = 28 AND street = "Humphrey Street";

/* | 295 | 2021 | 7     | 28  | Humphrey Street | Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |
   | 297 | 2021 | 7     | 28  | Humphrey Street | Littering took place at 16:36. No known witnesses. */

-- query the interview database for the 3 witness interviews
SELECT * FROM interviews WHERE year = 2021 AND month = 7 AND day = 28;

/*
| 161 | Ruth    | 2021 | 7     | 28  | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
| 162 | Eugene  | 2021 | 7     | 28  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
| 163 | Raymond | 2021 | 7     | 28  | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
The thief then asked the person on the other end of the phone to purchase the flight ticket. |
*/

-- query the security logs at 10 AM
SELECT * FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10;
/*
+-----+------+-------+-----+------+--------+----------+---------------+
| id  | year | month | day | hour | minute | activity | license_plate |
+-----+------+-------+-----+------+--------+----------+---------------+
| 258 | 2021 | 7     | 28  | 10   | 8      | entrance | R3G7486       |
| 259 | 2021 | 7     | 28  | 10   | 14     | entrance | 13FNH73       |
| 260 | 2021 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       |
| 261 | 2021 | 7     | 28  | 10   | 18     | exit     | 94KL13X       |
| 262 | 2021 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       |
| 263 | 2021 | 7     | 28  | 10   | 19     | exit     | 4328GD8       |
| 264 | 2021 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
| 265 | 2021 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |
| 266 | 2021 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |
| 267 | 2021 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       |
| 268 | 2021 | 7     | 28  | 10   | 35     | exit     | 1106N58       |
| 269 | 2021 | 7     | 28  | 10   | 42     | entrance | NRYN856       |
| 270 | 2021 | 7     | 28  | 10   | 44     | entrance | WD5M8I6       |
| 271 | 2021 | 7     | 28  | 10   | 55     | entrance | V47T75I       |
+-----+------+-------+-----+------+--------+----------+---------------+
*/

-- query security logs at 9 to see when the car arrived in the parking lot
SELECT * FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 9;
/*
+-----+------+-------+-----+------+--------+----------+---------------+
| id  | year | month | day | hour | minute | activity | license_plate |
+-----+------+-------+-----+------+--------+----------+---------------+
| 254 | 2021 | 7     | 28  | 9    | 14     | entrance | 4328GD8       |
| 255 | 2021 | 7     | 28  | 9    | 15     | entrance | 5P2BI95       |
| 256 | 2021 | 7     | 28  | 9    | 20     | entrance | 6P58WS2       |
| 257 | 2021 | 7     | 28  | 9    | 28     | entrance | G412CB7       |
+-----+------+-------+-----+------+--------+----------+---------------+
*/


-- get list of all license plates that left the parking lot within 10 minutes of the theft at 10:15
SELECT * FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >15 AND minute <26;
/*
+-----+------+-------+-----+------+--------+----------+---------------+
| id  | year | month | day | hour | minute | activity | license_plate |
+-----+------+-------+-----+------+--------+----------+---------------+
| 260 | 2021 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       |
| 261 | 2021 | 7     | 28  | 10   | 18     | exit     | 94KL13X       |
| 262 | 2021 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       |
| 263 | 2021 | 7     | 28  | 10   | 19     | exit     | 4328GD8       |
| 264 | 2021 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
| 265 | 2021 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |
| 266 | 2021 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |
| 267 | 2021 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       |
+-----+------+-------+-----+------+--------+----------+---------------+
*/
-- get information on people with the above license plates from parking lot
SELECT * FROM people WHERE license_plate IN
(SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >15 AND minute <26);
/*
+--------+---------+----------------+-----------------+---------------+
|   id   |  name   |  phone_number  | passport_number | license_plate |
+--------+---------+----------------+-----------------+---------------+
| 221103 | Vanessa | (725) 555-4692 | 2963008352      | 5P2BI95       |
| 243696 | Barry   | (301) 555-4174 | 7526138472      | 6P58WS2       |
| 396669 | Iman    | (829) 555-5269 | 7049073643      | L93JTIZ       |
| 398010 | Sofia   | (130) 555-0289 | 1695452385      | G412CB7       |
| 467400 | Luca    | (389) 555-5198 | 8496433585      | 4328GD8       |
| 514354 | Diana   | (770) 555-1861 | 3592750733      | 322W7JE       |
| 560886 | Kelsey  | (499) 555-9472 | 8294398571      | 0NTHK55       |
| 686048 | Bruce   | (367) 555-5533 | 5773159633      | 94KL13X       |
+--------+---------+----------------+-----------------+---------------+
*/
SELECT bakery_security_logs.activity, bakery_security_logs.license_plate, people.name FROM people
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE bakery_security_logs.year = 2021
AND bakery_security_logs.month = 7
AND bakery_security_logs.hour = 10
AND bakery_security_logs.minute >= 15
AND bakery_security_logs.minute <=25
AND bakery_security_logs.activity = "exit";
/*
+----------+---------------+-----------+
| activity | license_plate |   name    |
+----------+---------------+-----------+
| exit     | 5P2BI95       | Vanessa   |
| exit     | 94KL13X       | Bruce     |
| exit     | 6P58WS2       | Barry     |
| exit     | 4328GD8       | Luca      |
| exit     | G412CB7       | Sofia     |
| exit     | L93JTIZ       | Iman      |
| exit     | 322W7JE       | Diana     |
| exit     | 0NTHK55       | Kelsey    |
| exit     | 11J91FW       | Noah      |
| exit     | PF37ZVK       | Kathleen  |
| exit     | 1M92998       | Alice     |
| exit     | XE95071       | Christine |
| exit     | IH61GO8       | Karen     |
| exit     | 8P9NEU9       | Alexander |
+----------+---------------+-----------+
*/

-- get list of account numbers from the ATM withdrawals on Leggett Street on July 28, 2021
SELECT account_number
FROM atm_transactions
WHERE year = 2021
AND month = 7
AND day = 28
AND atm_location = "Leggett Street"
AND transaction_type = "withdraw";
/*
+----------------+
| account_number |
+----------------+
| 28500762       |
| 28296815       |
| 76054385       |
| 49610011       |
| 16153065       |
| 25506511       |
| 81061156       |
| 26013199       |
+----------------+
*/

SELECT people.name, atm_transactions.transaction_type FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.year = 2021
AND atm_transactions.month = 7
AND atm_transactions.day = 28
AND atm_location = "Leggett Street"
AND atm_transactions.transaction_type = "withdraw";

/*
+---------+------------------+
|  name   | transaction_type |
+---------+------------------+
| Bruce   | withdraw         |
| Diana   | withdraw         |
| Brooke  | withdraw         |
| Kenny   | withdraw         |
| Iman    | withdraw         |
| Luca    | withdraw         |
| Taylor  | withdraw         |
| Benista | withdraw         |
+---------+------------------+
*/

-- Add caller name and receiver name to table to see who made the phone calls
ALTER TABLE phone_calls
ADD caller_name text;
ALTER TABLE phone_calls
ADD receiver_name text;

UPDATE phone_calls
SET caller_name = people.name
FROM people
WHERE phone_calls.caller = people.phone_number;

UPDATE phone_calls
SET receiver_name = people.name
FROM people
WHERE phone_calls.receiver = people.phone_number;

SELECT caller, caller_name, receiver, receiver_name FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND duration <60;

/*
+----------------+-------------+----------------+---------------+
|     caller     | caller_name |    receiver    | receiver_name |
+----------------+-------------+----------------+---------------+
| (130) 555-0289 | Sofia       | (996) 555-8899 | Jack          |
| (499) 555-9472 | Kelsey      | (892) 555-8872 | Larry         |
| (367) 555-5533 | Bruce       | (375) 555-8161 | Robin         |
| (499) 555-9472 | Kelsey      | (717) 555-1342 | Melissa       |
| (286) 555-6063 | Taylor      | (676) 555-6554 | James         |
| (770) 555-1861 | Diana       | (725) 555-3243 | Philip        |
| (031) 555-6622 | Carina      | (910) 555-3251 | Jacqueline    |
| (826) 555-1652 | Kenny       | (066) 555-9701 | Doris         |
| (338) 555-6650 | Benista     | (704) 555-2131 | Anna          |
+----------------+-------------+----------------+---------------+
*/

SELECT id, hour, minute, origin_airport_id, destination_airport_id
FROM flights
WHERE year = 2021
AND month = 7
AND day = 29
ORDER BY hour ASC
LIMIT 1;

+----+------+--------+-------------------+------------------------+
| id | hour | minute | origin_airport_id | destination_airport_id |
+----+------+--------+-------------------+------------------------+
| 36 | 8    | 20     | 8                 | 4                      |
+----+------+--------+-------------------+------------------------+

-- update flights table so that the city is in the columns instead of numbers
UPDATE flights
SET origin_airport_id = airports.city
FROM airports
WHERE flights.origin_airport_id = airports.id;

UPDATE flights
SET destination_airport_id = airports.city
FROM airports
WHERE flights.destination_airport_id = airports.id;

-- get destination airport
SELECT origin_airport_id, destination_airport_id FROM flights
WHERE id = 36;
/*
+-------------------+------------------------+
| origin_airport_id | destination_airport_id |
+-------------------+------------------------+
| Fiftyville        | New York City          |
+-------------------+------------------------+
*/

SELECT flights.destination_airport_id, name, phone_number,
license_plate from people
JOIN passengers ON people.passport_number = passengers.passport_number
JOIN flights ON flights.id = passengers.flight_id
WHERE flights.id = 36
ORDER BY flights.hour ASC;
/*
+------------------------+--------+----------------+---------------+
| destination_airport_id |  name  |  phone_number  | license_plate |
+------------------------+--------+----------------+---------------+
| New York City          | Doris  | (066) 555-9701 | M51FA04       |
| New York City          | Sofia  | (130) 555-0289 | G412CB7       |
| New York City          | Bruce  | (367) 555-5533 | 94KL13X       |
| New York City          | Edward | (328) 555-1152 | 130LD9Z       |
| New York City          | Kelsey | (499) 555-9472 | 0NTHK55       |
| New York City          | Taylor | (286) 555-6063 | 1106N58       |
| New York City          | Kenny  | (826) 555-1652 | 30G67EN       |
| New York City          | Luca   | (389) 555-5198 | 4328GD8       |
+------------------------+--------+----------------+---------------+
*/
--Find name that exists in ATM calls, parking lots, flights to NYC, etc
SELECT name FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
JOIN flights ON flights.id = passengers.flight_id
WHERE (flights.year = 2021 AND flights.month = 7 AND flights.day = 29 AND flights.id = 36)
AND name IN
(SELECT phone_calls.caller_name FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND duration < 60)
AND name IN
(SELECT people.name FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.year = 2021
AND atm_transactions.month = 7
AND atm_transactions.day = 28
AND atm_location = "Leggett Street"
AND atm_transactions.transaction_type = "withdraw")
AND name IN
(SELECT people.name FROM people
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE bakery_security_logs.year = 2021
AND bakery_security_logs.month = 7
AND bakery_security_logs.hour = 10
AND bakery_security_logs.minute >= 15
AND bakery_security_logs.minute <=25
AND bakery_security_logs.activity = "exit");

/*
+-------+
| name  |
+-------+
| Bruce |
+-------+
*/



-- get information on people with the above account numbers from the ATM withdrawal
SELECT * FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id WHERE bank_accounts.account_number IN
   ...> (SELECT account_number FROM atm_transactions WHERE year = 2021
   AND month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw");
/*
+--------+---------+----------------+-----------------+---------------+----------------+-----------+---------------+
|   id   |  name   |  phone_number  | passport_number | license_plate | account_number | person_id | creation_year |
+--------+---------+----------------+-----------------+---------------+----------------+-----------+---------------+
| 686048 | Bruce   | (367) 555-5533 | 5773159633      | 94KL13X       | 49610011       | 686048    | 2010          |
| 514354 | Diana   | (770) 555-1861 | 3592750733      | 322W7JE       | 26013199       | 514354    | 2012          |
| 458378 | Brooke  | (122) 555-4581 | 4408372428      | QX4YZN3       | 16153065       | 458378    | 2012          |
| 395717 | Kenny   | (826) 555-1652 | 9878712108      | 30G67EN       | 28296815       | 395717    | 2014          |
| 396669 | Iman    | (829) 555-5269 | 7049073643      | L93JTIZ       | 25506511       | 396669    | 2014          |
| 467400 | Luca    | (389) 555-5198 | 8496433585      | 4328GD8       | 28500762       | 467400    | 2014          |
| 449774 | Taylor  | (286) 555-6063 | 1988161715      | 1106N58       | 76054385       | 449774    | 2015          |
| 438727 | Benista | (338) 555-6650 | 9586786673      | 8X428L0       | 81061156       | 438727    | 2018          |
+--------+---------+----------------+-----------------+---------------+----------------+-----------+---------------+
*/

-- get common names from cars exiting parking lot and from the withdrawal at the ATM
SELECT name FROM people WHERE license_plate IN
(SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >15 AND minute <26)
INTERSECT
SELECT name FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id WHERE bank_accounts.account_number IN
(SELECT account_number FROM atm_transactions WHERE year = 2021
AND month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw");
/*
+-------+
| name  |
+-------+
| Bruce |
| Diana |
| Iman  |
| Luca  |
+-------+
*/

-- get caller phone numbers of people making a less than one minute phone call to find thief
SELECT caller FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;
/*
+----------------+
|     caller     |
+----------------+
| (130) 555-0289 |
| (499) 555-9472 |
| (367) 555-5533 |
| (499) 555-9472 |
| (286) 555-6063 |
| (770) 555-1861 |
| (031) 555-6622 |
| (826) 555-1652 |
| (338) 555-6650 |
+----------------+
*/

-- get list of people with the above phone numbers from the people table
SELECT name FROM people WHERE phone_number IN
(SELECT caller FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60);
/*
+---------+
|  name   |
+---------+
| Kenny   |
| Sofia   |
| Benista |
| Taylor  |
| Diana   |
| Kelsey  |
| Bruce   |
| Carina  |
+---------+
*/

-- Find the overlap of the phone callers with the ATM withdrawal people and parking lot people
SELECT name FROM people WHERE license_plate IN
(SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >15 AND minute <26)
INTERSECT
SELECT name FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id WHERE bank_accounts.account_number IN
(SELECT account_number FROM atm_transactions WHERE year = 2021
AND month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw")
INTERSECT
SELECT name FROM people WHERE phone_number IN
(SELECT caller FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60);
/*
+-------+
| name  |
+-------+
| Bruce |
| Diana |
+-------+
*/

SELECT * FROM phone_calls JOIN people.phone_number = phone_calls.caller ON WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;

-- get list of receivers for the phone call made
SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;
/*
+----------------+
|    receiver    |
+----------------+
| (996) 555-8899 |
| (892) 555-8872 |
| (375) 555-8161 |
| (717) 555-1342 |
| (676) 555-6554 |
| (725) 555-3243 |
| (910) 555-3251 |
| (066) 555-9701 |
| (704) 555-2131 |
+----------------+
*/


-- get names of those who received the phone calls.  These are potential accomplices
SELECT name FROM people WHERE phone_number IN
(SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60);
/*
+------------+
|    name    |
+------------+
| James      |
| Larry      |
| Anna       |
| Jack       |
| Melissa    |
| Jacqueline |
| Philip     |
| Robin      |
| Doris      |
+------------+
*/
-- get passport number of those who received the phone calls.  These are potential accomplices
SELECT passport FROM people WHERE phone_number IN
(SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60);


-- get the Fiftyville airport id
SELECT * FROM airports WHERE city = "Fiftyville";
/*
+----+--------------+-----------------------------+------------+
| id | abbreviation |          full_name          |    city    |
+----+--------------+-----------------------------+------------+
| 8  | CSF          | Fiftyville Regional Airport | Fiftyville |
+----+--------------+-----------------------------+------------+
*/


-- get list of all flight id's out of Fiftyville
SELECT id FROM flights WHERE year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = 8;
/*
+----+
| id |
+----+
| 18 |
| 23 |
| 36 |
| 43 |
| 53 |
+----+
*/

-- get passport numbers of all passengers on the flights out of fiftyville
SELECT passport_number FROM passengers WHERE flight_id IN
(SELECT id FROM flights WHERE year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = 8);
/*
+-----------------+
| passport_number |
+-----------------+
| 2835165196      |
| 6131360461      |
| 3231999695      |
| 3592750733      |
| 2626335085      |
| 6117294637      |
| 2996517496      |
| 3915621712      |
| 4149859587      |
| 9183348466      |
| 7378796210      |
| 7874488539      |
| 4195341387      |
| 6263461050      |
| 3231999695      |
| 7951366683      |
| 7214083635      |
| 1695452385      |
| 5773159633      |
| 1540955065      |
| 8294398571      |
| 1988161715      |
| 9878712108      |
| 8496433585      |
| 7597790505      |
| 6128131458      |
| 6264773605      |
| 3642612721      |
| 4356447308      |
| 7441135547      |
| 7894166154      |
| 6034823042      |
| 4408372428      |
| 2312901747      |
| 1151340634      |
| 8174538026      |
| 1050247273      |
| 7834357192      |
+-----------------+
*/
-- get passport numbers of potential thieves
SELECT passport_number FROM people WHERE name = "Bruce" OR name = "Diana";
/*
+-----------------+
| passport_number |
+-----------------+
| 3592750733      |
| 5773159633      |
+-----------------+
*/

--get passport numbers for potential accomplices that received the phone call
SELECT passport_number FROM people WHERE phone_number IN
(SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60);
/*
+-----------------+
| passport_number |
+-----------------+
| 2438825627      |
| 2312901747      |
|                 |
| 9029462229      |
| 7834357192      |
|                 |
| 3391710505      |
|                 |
| 7214083635      |
+-----------------+
*/

--Find overlap of accomplices passport numbers (from the phone call receivers) with flight list of all passports who flew on July 29 from Fiftyville airport
SELECT passport_number FROM people WHERE phone_number IN
(SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60)
INTERSECT
SELECT passport_number FROM passengers WHERE flight_id IN
(SELECT id FROM flights WHERE year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = 8);
/*
+-----------------+
| passport_number |
+-----------------+
| 2312901747      |
| 7214083635      |
| 7834357192      |
+-----------------+
*/

--Find the name of the the potential accomplices using the passport numbers
SELECT name FROM people WHERE passport_number IN
(
SELECT passport_number FROM people WHERE phone_number IN
(SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60)
INTERSECT
SELECT passport_number FROM passengers WHERE flight_id IN
(SELECT id FROM flights WHERE year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = 8)
);

/*
+---------+
|  name   |
+---------+
| Larry   |
| Melissa |
| Doris   |
+---------+
*/

-- Find overlap of thieves passport numbers with the all those passports on the flights on July 29,2021
SELECT passport_number FROM people WHERE name = "Bruce" OR name = "Diana"
INTERSECT
SELECT passport_number FROM passengers WHERE flight_id IN
(SELECT id FROM flights WHERE year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = 8);
/* Both bruce and Diana flew on the plane as both their passports overlapped
+-----------------+
| passport_number |
+-----------------+
| 3592750733      |
| 5773159633      |
+-----------------+
*/

-- Find the flight_id of the potential thief on flights leaving July 29 2021 leaving from Fiftyville
SELECT flight_id FROM passengers WHERE passport_number IN
(SELECT passport_number FROM people WHERE name = "Bruce" OR name = "Diana"
INTERSECT
SELECT passport_number FROM passengers WHERE flight_id IN
(SELECT id FROM flights WHERE year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = 8));
/*
+-----------+
| flight_id |
+-----------+
| 18        |
| 24        |
| 36        |
| 54        |
+-----------+
*/
-- Find intersection between accomplices passports and flights leaving Fiftyville airport on July 29, 2021
SELECT flight_id FROM passengers WHERE passport_number IN
(SELECT passport_number FROM people WHERE phone_number IN
(SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60)
INTERSECT
SELECT passport_number FROM passengers WHERE flight_id IN
(SELECT id FROM flights WHERE year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = 8));
/*
+-----------+
| flight_id |
+-----------+
| 17        |
| 17        |
| 25        |
| 36        |
| 37        |
| 53        |
| 53        |
+-----------+
*/

--Find overlapping flight_id between thief and accomplice
SELECT flight_id FROM (SELECT flight_id FROM passengers WHERE passport_number IN
(SELECT passport_number FROM people WHERE name = "Bruce" OR name = "Diana"
INTERSECT
SELECT passport_number FROM passengers WHERE flight_id IN
(SELECT id FROM flights WHERE year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = 8)))
WHERE flight_id IN
(SELECT flight_id FROM passengers WHERE passport_number IN
(SELECT passport_number FROM people WHERE phone_number IN
(SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60)
INTERSECT
SELECT passport_number FROM passengers WHERE flight_id IN
(SELECT id FROM flights WHERE year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = 8)));
/*
+-----------+
| flight_id |
+-----------+
| 36        |
+-----------+
*/

-- Find thief passport number on flight 36
SELECT passport_number FROM people WHERE name = "Bruce" OR name = "Diana"
INTERSECT
SELECT passport_number FROM passengers WHERE flight_id = 36;
/*
+-----------------+
| passport_number |
+-----------------+
| 5773159633      |
+-----------------+
*/

-- Find accomplice passport number on flight 36
SELECT passport_number FROM people WHERE phone_number IN
(SELECT receiver FROM phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60)
INTERSECT
SELECT passport_number FROM passengers WHERE flight_id = 36;
/*
+-----------------+
| passport_number |
+-----------------+
| 7214083635      |
+-----------------+
*/
-- Get the identity of the thief using the passport number
SELECT * FROM people WHERE passport_number = 5773159633;
/*
+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+
| 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |
+--------+-------+----------------+-----------------+---------------+
*/

-- Get the identity of the accomplice using the passport number
SELECT * FROM people WHERE passport_number = 7214083635;
/*
+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+
| 953679 | Doris | (066) 555-9701 | 7214083635      | M51FA04       |
+--------+-------+----------------+-----------------+---------------+
*/

-- Get destination info about flight id 36
SELECT * FROM airports WHERE id = (SELECT destination_airport_id FROM flights WHERE id = 36);
/*
+----+--------------+-------------------+---------------+
| id | abbreviation |     full_name     |     city      |
+----+--------------+-------------------+---------------+
| 4  | LGA          | LaGuardia Airport | New York City |
+----+--------------+-------------------+---------------+
*/