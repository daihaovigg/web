-- MySQL dump 10.13  Distrib 5.6.21, for Win64 (x86_64)
--
-- Host: localhost    Database: awesome
-- ------------------------------------------------------
-- Server version	5.6.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `awesome`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `awesome` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `awesome`;

--
-- Table structure for table `blogs`
--

DROP TABLE IF EXISTS `blogs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blogs` (
  `id` varchar(50) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_image` varchar(500) NOT NULL,
  `name` varchar(50) NOT NULL,
  `summary` varchar(200) NOT NULL,
  `content` mediumtext NOT NULL,
  `created_at` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_created_at` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blogs`
--

LOCK TABLES `blogs` WRITE;
/*!40000 ALTER TABLE `blogs` DISABLE KEYS */;
INSERT INTO `blogs` VALUES ('001435836934503f4ca6c65c07545e88899a09ae64f72ee000','001435834742450da9544e700dd4969996882e5c8c91700000','daihao','http://www.gravatar.com/avatar/5e40f5b8d8591a2a0a30ba71143de859?d=mm&s=120','第一次博客','就是瞎写写','今天2015-07-02，写了博客，检查能否运行，恩',1435836934.50371),('001435845524976c8dcfabc64c34aa1aa588ae4877cae74000','001435834742450da9544e700dd4969996882e5c8c91700000','daihao','http://www.gravatar.com/avatar/5e40f5b8d8591a2a0a30ba71143de859?d=mm&s=120','WTF','To D','明天要出去',1435845524.9765),('001436251876990a751ff983a57458496fe20b3160a3b95000','001435834742450da9544e700dd4969996882e5c8c91700000','daihao','http://www.gravatar.com/avatar/5e40f5b8d8591a2a0a30ba71143de859?d=mm&s=120','test','sum','cont',1436251876.99043),('0014363290315567f53043bb8c44673ba0681dd60e3ebc9000','0014362530922689b5bdab2479042c18d56ccf41706010e000','augest','http://www.gravatar.com/avatar/cd5b4eeef6a370e0b4f3c342b1c28800?d=mm&s=120','test_augest','myhayt','mytest',1436329031.55679),('001436417569500e299cb9f990844bc80203e8cb4cc3a06000','0014362530922689b5bdab2479042c18d56ccf41706010e000','augest','http://www.gravatar.com/avatar/cd5b4eeef6a370e0b4f3c342b1c28800?d=mm&s=120','das','dsad','dasda',1436417569.50083),('00143641757556412c7d61d9cf4415fae74ab3d0e9e8563000','0014362530922689b5bdab2479042c18d56ccf41706010e000','augest','http://www.gravatar.com/avatar/cd5b4eeef6a370e0b4f3c342b1c28800?d=mm&s=120','dwa','sadsa','sazcdz',1436417575.56418),('001436417581048b5829898a5114f3bbfee7e6cb6dbbb07000','0014362530922689b5bdab2479042c18d56ccf41706010e000','augest','http://www.gravatar.com/avatar/cd5b4eeef6a370e0b4f3c342b1c28800?d=mm&s=120','dwadas','sdasd','zxcsca',1436417581.04849),('001436417586204aa0c19d9cdda48daa822541f275280a5000','0014362530922689b5bdab2479042c18d56ccf41706010e000','augest','http://www.gravatar.com/avatar/cd5b4eeef6a370e0b4f3c342b1c28800?d=mm&s=120','dwqrw','ewrwr','sdzfsdf',1436417586.20479),('0014364175920573c442befd9b242cfaeffd5ba18dc7bf8000','0014362530922689b5bdab2479042c18d56ccf41706010e000','augest','http://www.gravatar.com/avatar/cd5b4eeef6a370e0b4f3c342b1c28800?d=mm&s=120','eqweq','asdasd','safsafdsfsd',1436417592.05712),('0014364175968275b0dcf213d0e4ab4af2d0382641dd6cc000','0014362530922689b5bdab2479042c18d56ccf41706010e000','augest','http://www.gravatar.com/avatar/cd5b4eeef6a370e0b4f3c342b1c28800?d=mm&s=120','qweqw','asdsa','cxzz',1436417596.82739),('0014364176048489442c481d64c49d0aa4da7ba9fac66ab000','0014362530922689b5bdab2479042c18d56ccf41706010e000','augest','http://www.gravatar.com/avatar/cd5b4eeef6a370e0b4f3c342b1c28800?d=mm&s=120','dasdsasa','safsafsafsafsaf','asfsafsaf',1436417604.84885),('001436417617253d714870831c24008b1b9dd80cfa87187000','0014362530922689b5bdab2479042c18d56ccf41706010e000','augest','http://www.gravatar.com/avatar/cd5b4eeef6a370e0b4f3c342b1c28800?d=mm&s=120','gfhr','vbcnvb','nvnv',1436417617.25356),('001436417690232b59f6b3aa51b4dbe8086276602fdc00b000','001435836278400c90d8e5a91c64487b7c732499dc2d55c000','Administrator','http://www.gravatar.com/avatar/04e3d172f3a62c99dcf2f77d7de01d80?d=mm&s=120','dsgf','hhg','jhmg',1436417690.23273),('001436417694774622a5ccb87a446e9aadee0def65bf3cb000','001435836278400c90d8e5a91c64487b7c732499dc2d55c000','Administrator','http://www.gravatar.com/avatar/04e3d172f3a62c99dcf2f77d7de01d80?d=mm&s=120','gjgh','hgfg','hgfhfg',1436417694.77399),('001436417700138d2ea86d89b74482b98e86ddeba53a24f000','001435836278400c90d8e5a91c64487b7c732499dc2d55c000','Administrator','http://www.gravatar.com/avatar/04e3d172f3a62c99dcf2f77d7de01d80?d=mm&s=120','jh','gfhg','fgjfg',1436417700.1383),('00143641770540699998a15a63c475582887589b65ad53c000','001435836278400c90d8e5a91c64487b7c732499dc2d55c000','Administrator','http://www.gravatar.com/avatar/04e3d172f3a62c99dcf2f77d7de01d80?d=mm&s=120','fgjhjj','jgfjgf','gfhfgh',1436417705.4066),('001436417710435fb8767eff3014ca1864db49d660fcae5000','001435836278400c90d8e5a91c64487b7c732499dc2d55c000','Administrator','http://www.gravatar.com/avatar/04e3d172f3a62c99dcf2f77d7de01d80?d=mm&s=120','hfgh','jghjf','gfhgfhfg',1436417710.43589),('0014364185438831ad7f30ba47e47599aed1697896ae91f000','001435836278400c90d8e5a91c64487b7c732499dc2d55c000','Administrator','http://www.gravatar.com/avatar/04e3d172f3a62c99dcf2f77d7de01d80?d=mm&s=120','fds','fds','gd',1436418543.88356),('0014364185492742c20e276e20f4400b7a3c12409f6daa6000','001435836278400c90d8e5a91c64487b7c732499dc2d55c000','Administrator','http://www.gravatar.com/avatar/04e3d172f3a62c99dcf2f77d7de01d80?d=mm&s=120','j','gfj','hj',1436418549.27487),('001436418555798419bfee46ce2482ab7e909057dc2bc74000','001435836278400c90d8e5a91c64487b7c732499dc2d55c000','Administrator','http://www.gravatar.com/avatar/04e3d172f3a62c99dcf2f77d7de01d80?d=mm&s=120','ghfd','dfgrd','drgd',1436418555.79824),('00143641856164874383d54310c4769ad473de9aa242680000','001435836278400c90d8e5a91c64487b7c732499dc2d55c000','Administrator','http://www.gravatar.com/avatar/04e3d172f3a62c99dcf2f77d7de01d80?d=mm&s=120','dgr','dsawa','wad',1436418561.64858),('001436418567587c5e44338742d4310a301f68843868586000','001435836278400c90d8e5a91c64487b7c732499dc2d55c000','Administrator','http://www.gravatar.com/avatar/04e3d172f3a62c99dcf2f77d7de01d80?d=mm&s=120','jkhj','hjk','khj',1436418567.58692),('0014364185823239655fd991af843e78a31586c5c84d4d7000','001435836278400c90d8e5a91c64487b7c732499dc2d55c000','Administrator','http://www.gravatar.com/avatar/04e3d172f3a62c99dcf2f77d7de01d80?d=mm&s=120','y','wrwe','ewrwe',1436418582.32276),('001437274188665ca8ee0ad1f234b5890eb296acde514a0000','0014362530922689b5bdab2479042c18d56ccf41706010e000','augest','http://www.gravatar.com/avatar/cd5b4eeef6a370e0b4f3c342b1c28800?d=mm&s=120','MARKDOWN','test','<p>This is <a href=\"http://example.com/\" title=\"Title\">\nan example</a> inline link.</p>\n<b> haha </b>\n&lt;p&gt;\n##hahah',1437274188.66529),('001437307708930d124351a9f134a45a59d71275161b137000','0014362530922689b5bdab2479042c18d56ccf41706010e000','augest','http://www.gravatar.com/avatar/cd5b4eeef6a370e0b4f3c342b1c28800?d=mm&s=120','wd','awd','sdo',1437307708.93097);
/*!40000 ALTER TABLE `blogs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` varchar(50) NOT NULL,
  `blog_id` varchar(50) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_image` varchar(500) NOT NULL,
  `content` mediumtext NOT NULL,
  `created_at` double NOT NULL,
  `to_who` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_created_at` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES ('00143583699918650d69ed72f7c450996f8f2c8233639d6000','001435836934503f4ca6c65c07545e88899a09ae64f72ee000','001435836278400c90d8e5a91c64487b7c732499dc2d55c000','Administrator','http://www.gravatar.com/avatar/04e3d172f3a62c99dcf2f77d7de01d80?d=mm&s=120','图呢？？！！！',1435836999.18619,'daihao'),('001435845545475203b8dbd351e44e48e9c1bc5c44800f9000','001435845524976c8dcfabc64c34aa1aa588ae4877cae74000','001435834742450da9544e700dd4969996882e5c8c91700000','daihao','http://www.gravatar.com/avatar/5e40f5b8d8591a2a0a30ba71143de859?d=mm&s=120','啥？？',1435845545.47568,'daihao'),('0014363353066695f05ff9322f9458085e9b183ab134042000','001435845524976c8dcfabc64c34aa1aa588ae4877cae74000','001435834742450da9544e700dd4969996882e5c8c91700000','daihao','http://www.gravatar.com/avatar/5e40f5b8d8591a2a0a30ba71143de859?d=mm&s=120','hehe',1436335306.66871,'daihao'),('0014363354487575f6963652fb54c908671d8453d6415b1000','001435836934503f4ca6c65c07545e88899a09ae64f72ee000','0014362530922689b5bdab2479042c18d56ccf41706010e000','augest','http://www.gravatar.com/avatar/cd5b4eeef6a370e0b4f3c342b1c28800?d=mm&s=120','sha?',1436335448.75683,'daihao'),('0014364178128269f521e32343e4976989d677b8c6c1b1c000','0014364176048489442c481d64c49d0aa4da7ba9fac66ab000','001435836278400c90d8e5a91c64487b7c732499dc2d55c000','Administrator','http://www.gravatar.com/avatar/04e3d172f3a62c99dcf2f77d7de01d80?d=mm&s=120','hahdsakd',1436417812.82675,'augest'),('00143641783198522d331defd794a8ab24497783413fb1c000','00143641770540699998a15a63c475582887589b65ad53c000','0014362530922689b5bdab2479042c18d56ccf41706010e000','augest','http://www.gravatar.com/avatar/cd5b4eeef6a370e0b4f3c342b1c28800?d=mm&s=120','qwqwe',1436417831.98584,'Administrator');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `passwd` varchar(50) NOT NULL,
  `admin` tinyint(1) NOT NULL,
  `name` varchar(50) NOT NULL,
  `image` varchar(500) NOT NULL,
  `created_at` double NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_email` (`email`),
  KEY `idx_created_at` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('001435834742450da9544e700dd4969996882e5c8c91700000','daihao@qq.com','51185a9ce3dcd9b8b40eb39604a6336e67a4a66d',1,'daihao','http://www.gravatar.com/avatar/5e40f5b8d8591a2a0a30ba71143de859?d=mm&s=120',1435834742.45145),('001435836278400c90d8e5a91c64487b7c732499dc2d55c000','admin@exam.com','76b74d8b72aabce3388a30b40596d62547fb756e',0,'Administrator','http://www.gravatar.com/avatar/04e3d172f3a62c99dcf2f77d7de01d80?d=mm&s=120',1435836278.40204),('0014362530922689b5bdab2479042c18d56ccf41706010e000','augest@exam.com','1583ad27cc53ff0cce223fecca190a4bbfc8a59c',0,'augest','http://www.gravatar.com/avatar/cd5b4eeef6a370e0b4f3c342b1c28800?d=mm&s=120',1436253092.26826),('00143676537246231ce561b28ef45a897182b937719dfc4000','li@exam.com','fc3247d0ce5b94bef05fcfc9fc495649f53f651e',0,'li','/static/img/default.jpg',1436765372.46204),('001436957062754441c5d2a23d74ad7ad28775132b28eb7000','da@exam.com','0f55638f0a4d01254346551ffcc5753bddc81341',0,'da','/static/img/default.jpg',1436957062.75481),('001436969748570fc8dc42ac7b34eb7b8a8afbc86db6a3d000','dai@exam.com','ae3b56473ca7531d58d4ff99d855be66d4dfb69a',0,'dai','/HeadImgf500023e-2afb-11e5-8637-10bf483487c1.jpg',1436969748.57029),('0014369698967605a74d1e8f95c46c19f7279c307332088000','hao@exam.com','a6901676de43b39a4a8efcd36a17d9ea855f5f14',0,'dai','/HeadImg/4563a580-2afc-11e5-a26e-10bf483487c1.jpg',1436969896.76076),('001437008810664b007a89b8d284df080d9383edc0a9e84000','ha@exam.com','d9000c8cd835dec707360fb8d126e984859ac3de',0,'hao','/static/HeadImg/db3d99f8-2b56-11e5-ace1-10bf483487c1.jpg',1437008810.66478),('001437013316440100352a87e1e449f842e2401b6cedfd0000','lili@exam.com','25c76421e3980e81c11520462afbcdd9e03649b3',0,'管理员','/static/HeadImg/60b2f8b0-2b61-11e5-9d06-10bf483487c1.jpg',1437013316.4405),('001437014076944fb67afe948f147f2ba7a0fb0e5693111000','dada@exam.com','25a39bbb84723e95d2c7925daab655490c03a4f4',0,'管理','/static/img/default.jpg',1437014076.94599),('00143701411207236e081219f934c23b0a9e7cf84c81990000','asd@exam.com','79f0f9a58f036ac282fa7b7e250de77ff919ac18',0,'sdas','/static/img/default.jpg',1437014112.072),('0014370141918191f6ebdef205f42c583510f20878d9c63000','afafds@exam.com','1166aff0b9c99aa0ac9d7c5a9253021dc6bb2380',0,'fw','/static/img/default.jpg',1437014191.82056),('001437014407804d83455431a9f488e8a9e85acecee1077000','fsd@exam.com','e13e7d11ab3a236d43c0b7f27e056d739a3bf880',0,'sfs','/static/HeadImg/ed77d570-2b63-11e5-986e-10bf483487c1.jpg',1437014407.80592),('001437014436287e8e4286e51994811a55da835207be366000','sf@exam.com','56f6fdf705c1acd939722c0606461d4632e13ca4',0,'sf','/static/img/default.jpg',1437014436.28755);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-07-20 15:58:13
