CREATE TABLE IF NOT EXISTS indexer(id INT PRIMARY KEY AUTO_INCREMENT, 
                                   ts TIMESTAMP, 
                                   word TINYTEXT, 
                                   position INT,
                                   pos VARCHAR(8));
