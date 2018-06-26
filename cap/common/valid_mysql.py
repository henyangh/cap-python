#coding:utf-8
__author__ = 'admin'
# --------------------------------
# Created by admin  on 2016/11/11.
# ---------------------------------
from warnings import filterwarnings
import MySQLdb
filterwarnings('ignore', category = MySQLdb.Warning)
import  MySQLdb
# create  table sql list
create_table_sql_list=[
            '''CREATE TABLE  if not EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
)  ;''',

    '''CREATE TABLE if not EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_a7792de1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;''',

    '''CREATE TABLE if not EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_e4470c6e` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8; ''',

'''CREATE TABLE if not EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;''',

'''CREATE TABLE if not EXISTS  `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`),
  CONSTRAINT `group_id_refs_id_f0ee9890` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_831107f1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;''',

    '''CREATE TABLE if not EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_f2045483` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;''',

    '''CREATE TABLE  if not EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_fbfc09f1` (`user_id`),
  KEY `django_admin_log_e4470c6e` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;''',

    '''CREATE TABLE  if not EXISTS  `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;''',

    '''CREATE TABLE if not EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;''',

    '''CREATE TABLE if not EXISTS  `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;''',

            '''INSERT ignore  INTO auth_permission (id, name, content_type_id, codename) VALUES
   (1, 'Can add permission', 1, 'add_permission')  ,
   (2, 'Can change permission', 1, 'change_permission')  ,
   (3, 'Can delete permission', 1, 'delete_permission')  ,
   (4, 'Can add group', 2, 'add_group')  ,
   (5, 'Can change group', 2, 'change_group')  ,
   (6, 'Can delete group', 2, 'delete_group')  ,
   (7, 'Can add user', 3, 'add_user')  ,
   (8, 'Can change user', 3, 'change_user')  ,
   (9, 'Can delete user', 3, 'delete_user')  ,
   (10, 'Can add content type', 4, 'add_contenttype')  ,
   (11, 'Can change content type', 4, 'change_contenttype')  ,
   (12, 'Can delete content type', 4, 'delete_contenttype')  ,
   (13, 'Can add session', 5, 'add_session')  ,
   (14, 'Can change session', 5, 'change_session')  ,
   (15, 'Can delete session', 5, 'delete_session')  ,
   (16, 'Can add site', 6, 'add_site')  ,
   (17, 'Can change site', 6, 'change_site')  ,
   (18, 'Can delete site', 6, 'delete_site')  ,
   (19, 'Can add log entry', 7, 'add_logentry')  ,
   (20, 'Can change log entry', 7, 'change_logentry')  ,
   (21, 'Can delete log entry', 7, 'delete_logentry')  ,
   (22, 'Can add worker', 8, 'add_worker')  ,
   (23, 'Can change worker', 8, 'change_worker')  ,
   (24, 'Can delete worker', 8, 'delete_worker')  ,
   (25, 'Can add repo', 9, 'add_repo')  ,
   (26, 'Can change repo', 9, 'change_repo')  ,
   (27, 'Can delete repo', 9, 'delete_repo')  ,
   (28, 'Can add pub log', 10, 'add_publog')  ,
   (29, 'Can change pub log', 10, 'change_publog')  ,
   (30, 'Can delete pub log', 10, 'delete_publog')  ,
   (31, 'Can add 计划任务', 11, 'add_crontask')  ,
   (32, 'Can change 计划任务', 11, 'change_crontask')  ,
   (33, 'Can delete 计划任务', 11, 'delete_crontask')  ,
   (34, 'Can add 计划任务', 12, 'add_deamontask')  ,
   (35, 'Can change 计划任务', 12, 'change_deamontask')  ,
   (36, 'Can delete 计划任务', 12, 'delete_deamontask')  ,
   (37, 'Can add 运行日志', 13, 'add_runlog')  ,
   (38, 'Can change 运行日志', 13, 'change_runlog')  ,
   (39, 'Can delete 运行日志', 13, 'delete_runlog');''',
    '''insert ignore into django_site values(1,"example.com","example.com");'''
    '''
    INSERT ignore  INTO auth_user (id, username, first_name, last_name, email, password, is_staff,
     is_active, is_superuser, last_login, date_joined) VALUES (
     1, 'admin', '', '', '18749679769@163.com', 
     'pbkdf2_sha256$10000$1X58MsOvjyOa$/S7paomFlNanSgEyuwG0QqaFlOVf97DepE0O5eD3YQo=', 
     1, 1, 1, '2018-06-05 15:39:13', '2018-06-05 15:39:13');''',

    '''INSERT ignore INTO cap_group (id, name, addtime) VALUES (1, '默认', 1528706232);''',
    '''INSERT ignore INTO django_content_type (id, name, app_label, model) VALUES 
        (1, 'permission', 'auth', 'permission'),
         (2, 'group', 'auth', 'group'),
         (3, 'user', 'auth', 'user'),
        (4, 'content type', 'contenttypes', 'contenttype'),
        (5, 'session', 'sessions', 'session'),
         (6, 'site', 'sites', 'site'),
         (7, 'log entry', 'admin', 'logentry'),
         (8, 'worker', 'cap', 'worker'),
         (9, 'repo', 'cap', 'repo'),
         (10, 'pub log', 'cap', 'publog'),
         (11, '计划任务', 'cap', 'crontask'),
         (12, '计划任务', 'cap', 'deamontask'),
         (13, '运行日志', 'cap', 'runlog');'''
    '''INSERT ignore INTO django_site (id, domain, name) VALUES (1, 'example.com', 'example.com');'''
]

def valid(host,port,db,user,passwd):
    for i in create_table_sql_list:
        conn = MySQLdb.connect(host=host, port=port, user=user, db=db, passwd=passwd, charset="utf8")
        cursor = conn.cursor()
        try:
            cursor.execute(i)
        except Exception as e :
            print i ,str(e)
            return False
        cursor.close()
        conn.commit()
        conn.close()
    return True


