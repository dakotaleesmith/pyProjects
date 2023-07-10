CREATE TABLE IF NOT EXISTS subscriptions (
	id int NOT NULL AUTO_INCREMENT,
	customer_id VARCHAR(255) NOT NULL,
	subscription VARCHAR(255) NOT NULL,
	loaded_at DATETIME NOT NULL DEFAULT NOW(),
	PRIMARY KEY (id)
);

INSERT INTO subscriptions
	(customer_id, subscription)
VALUES 
	(1, 'literary_delights'),
	(1, 'skincare'),
	(1, 'international_snacks'),
	(1, 'self_care'),
	(2, 'literary_delights'),
	(2, 'international_snacks'),
	(2, 'skincare'),
	(3, 'self_care'),
	(3, 'international_snacks'),
	(4, 'international_snacks'),
	(4, 'self_care'),
	(4, 'literary_delights'),
	(4, 'skincare'),
	(5, 'self_care'),
	(6, 'international_snacks'),
	(6, 'self_care')
;