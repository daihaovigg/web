use awesome;
create table if not exists audiolist(
	`id` varchar(50) not null,
	`src` varchar(200) not null,
	`name` varchar(200) not null,
	`created_at` real not null,
	key `idx_created_at` (`created_at`),
	primary key (`id`)
)engine=innodb default charset=utf8;

create table if not exists videolist(
	`id` varchar(50) not null,
	`src` varchar(200) not null,
	`name` varchar(200) not null,
	`created_at` real not null,
	key `idx_created_at` (`created_at`),
	primary key (`id`)
)engine=innodb default charset=utf8;
