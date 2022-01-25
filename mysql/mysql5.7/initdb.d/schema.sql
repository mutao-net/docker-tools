create table users( 
  id integer PRIMARY KEY AUTO_INCREMENT
  , name varchar (20) NOT NULL
  , register_date TIMESTAMP NOT NULL default current_timestamp
  , update_time TIMESTAMP NOT NULL default current_timestamp on update current_timestamp
) ENGINE = InnoDB DEFAULT CHARSET = utf8;