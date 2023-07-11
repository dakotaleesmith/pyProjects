WITH
	subscriptions_grouped AS (
		SELECT
			customer_id,
			GROUP_CONCAT(subscription) AS subscriptions
		FROM 
			subscriptions
		GROUP BY 1
	)
SELECT
	subscriptions,
	COUNT(*) AS num_accounts
FROM subscriptions_grouped
GROUP BY 1
ORDER BY 1
;