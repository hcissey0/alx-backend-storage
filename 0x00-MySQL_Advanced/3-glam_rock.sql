-- Lists all bands with glam rock as their style
SELECT band_name, COALESCE(2022 - formed - 2, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
AND split IS NULL
ORDER BY lifespan DESC;
