WITH
	subscriptions_ordered AS (
	SELECT *
	FROM subscriptions
	ORDER BY subscription 
	)
	, subscriptions_grouped AS (
	SELECT
		customer_id,
		JSON_ARRAYAGG(subscription) AS subscriptions,
		JSON_LENGTH(JSON_ARRAYAGG(subscription)) AS num_subscriptions
	FROM 
		subscriptions_ordered
	GROUP BY 1
	)
SELECT
	subscriptions,
	num_subscriptions,
	COUNT(*) AS num_accounts
FROM subscriptions_grouped
GROUP BY 1, 2
;