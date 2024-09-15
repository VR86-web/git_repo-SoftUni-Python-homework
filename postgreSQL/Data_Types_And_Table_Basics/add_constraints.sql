ALTER TABLE minions_info

ADD CONSTRAINT unique_containt
UNIQUE (id, email),

ADD CONSTRAINT banana_check
CHECK (banana > 0);

-- ALTER TABLE minions_info

-- ADD CONSTRAINT UQ_id_email
-- UNIQUE (id, email),

-- ADD CONSTRAINT CK_banana_is_positive
-- CHECK (banana > 0);