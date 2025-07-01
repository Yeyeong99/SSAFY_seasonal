SELECT store.name AS stroe, product.name AS product, MAX(amounts) AS max_total_amount
FROM 
	(
		SELECT store_id, product_id, SUM(quantity * product.unit_price) AS amounts
		FROM sell INNER JOIN product ON product.id = product_id
		GROUP BY product_id, store_id
		ORDER BY amounts ASC
	) AS t1
INNER JOIN store ON store.id = store_id INNER JOIN product ON product.id = product_id
GROUP BY store_id
ORDER BY store_id, product_id;
