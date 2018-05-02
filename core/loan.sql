-- ���ڴ������˵���û��ı���Ҫ���user���mobile�������ؼ���
DROP TABLE IF EXISTS `t_loan_mobiles`;
CREATE TABLE `t_loan_mobiles` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `mobile` varchar(11) DEFAULT NULL,
  `verify_status` int(11) DEFAULT NULL,
  `loan_status` int(11) DEFAULT NULL,
  `verify_time` datetime DEFAULT NULL,
  `loan_time` datetime DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mobile` (`mobile`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- �û��Ĵ��������
DROP TABLE IF EXISTS `t_loan_records`;
CREATE TABLE `t_loan_records` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_no` varchar(20) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `sex` varchar(4) DEFAULT NULL,
  `birth` varchar(20) DEFAULT NULL,
  `age` smallint(6) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `ip` varchar(20) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `credit` varchar(11) DEFAULT NULL,
  `agree` varchar(11) DEFAULT NULL,
  `custom` varchar(200) DEFAULT NULL,
  `subchannel` varchar(40) DEFAULT NULL,
  `status` smallint(11) DEFAULT NULL,
  `code` varchar(20) DEFAULT NULL,
  `policy_id` varchar(20) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `phone` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- �û��Ĵ���������
DROP TABLE IF EXISTS `t_loan_results`;
CREATE TABLE `t_loan_results` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `record_id` bigint(20) DEFAULT NULL,
  `loan_status` smallint(6) DEFAULT NULL,
  `error_msg` varchar(50) DEFAULT NULL,
  `loan_com` varchar(20) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `record_id` (`record_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
