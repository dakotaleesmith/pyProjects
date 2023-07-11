SELECT 
	customer_id, 
	subscription, 
	ROW_NUMBER() OVER(ORDER BY subscription) AS alphabetical_row_num
FROM subscriptions
;