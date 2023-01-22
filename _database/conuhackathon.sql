-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 22, 2023 at 01:49 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `conuhackathon`
--

-- --------------------------------------------------------

--
-- Table structure for table `fruits`
--

CREATE TABLE `fruits` (
  `id` int(11) NOT NULL,
  `fruit` varchar(50) NOT NULL,
  `cur_price` float NOT NULL,
  `best_price` float NOT NULL,
  `best_price_url` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `fruits`
--

INSERT INTO `fruits` (`id`, `fruit`, `cur_price`, `best_price`, `best_price_url`) VALUES
(1, 'apple', 0, 0.7, 'https://www.superc.ca/en/aisles/fruits-vegetables/fruits/apples-pears/apple/p/4129'),
(2, 'banana', 0, 0.29, 'https://www.superc.ca/en/aisles/fruits-vegetables/fruits/bananas-plantains/banana/p/4011'),
(3, 'orange', 0, 1.64, 'https://www.superc.ca/en/aisles/fruits-vegetables/fruits/citrus-fruits/seedless-navel-orange/p/3156'),
(4, 'kiwi', 0, 0.99, 'https://www.superc.ca/en/aisles/fruits-vegetables/fruits/avocadoes-exotic-fruits/kiwi/p/4030');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `fruits`
--
ALTER TABLE `fruits`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `fruits`
--
ALTER TABLE `fruits`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
