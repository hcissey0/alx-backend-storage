-- This ranks the origin of bands ordered by nnumbers
SELECT origin, SUM(nb_fans) AS nfans
FROM metal_bands
GROUP BY origin
ORDER BY nfans DESC;
