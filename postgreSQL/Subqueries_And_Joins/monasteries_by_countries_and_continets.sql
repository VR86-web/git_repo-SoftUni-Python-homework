UPDATE countries
SET
	country_name = 'Burma'
WHERE
	country_name = 'Myanmar';

INSERT INTO monasteries(monastery_name,country_code)
VALUES
	(
	'Hanga Abbey',
	(SELECT
		country_code
	FROM
		countries
	WHERE
	country_name = 'Tanzania')
	);

SELECT
	c.continent_name,
	cs.country_name,
	count(m.country_code) AS monasteries_count
FROM
	continents AS c
JOIN
	countries AS cs
USING
	(continent_code)
LEFT JOIN
	monasteries AS m -- left cause there can be countries with no monasteries
USING
	(country_code)
WHERE cs.three_rivers IS NOT TRUE
GROUP BY
	cs.country_name,
	c.continent_name
ORDER BY
	monasteries_count DESC,
	country_name;