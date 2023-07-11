WITH 
	subscriptions_ordered AS (
		SELECT 
			customer_id, 
			subscription, 
			ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY subscription) AS alphabetical_order
		FROM subscriptions
	)
SELECT
	customer_id,
	JSON_ARRAYAGG(subscription) AS subscriptions
FROM 
	subscriptions_ordered
GROUP BY 1
;