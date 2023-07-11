SELECT 
	customer_id, 
	subscription, 
	ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY subscription) AS alphabetical_order
FROM subscriptions
;