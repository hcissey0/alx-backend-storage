-- Createsa n index name score
CREATE INDEX idx_first_name_score ON names (LEFT(name, 1), score);
