-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Generation Time: Sep 02, 2022 at 01:06 PM
-- Server version: 5.7.39
-- PHP Version: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pynance`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `rowid` int(11) NOT NULL,
  `user` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `username` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `api_key` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `api_secret` varchar(250) COLLATE utf8_unicode_ci NOT NULL,
  `token` varchar(250) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`rowid`, `user`, `username`, `password`, `email`, `api_key`, `api_secret`, `token`) VALUES
(1, 'itplayground', 'itplayground', '$2b$10$mq1vLswKvuAto3ZAAZ8Ztue2RV9sgc1XWUcYnwV.hjEtiaRLknJde', 'pentagonps4@gmail.com', 'q3aMFjySMjwXbFfrwAAn64n4gvmroqGl78RvLs7dGXPI6DMtVkulYeWAdCWEycSw', 'nHkYxsm6TRvbizMUyYdoNHzuaGGSiEYAakeYklfHMPus2wJW493rJDSkTy6G95rO', '1234');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`rowid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `rowid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
