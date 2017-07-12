import sqlite3

conn = sqlite3.connect('types.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE exercise_log (body_part TEXT,
                                            exercise_name TEXT,
                                            num_sets INT,
                                            set1_weight INT,
                                            set1_reps INT,
                                            set2_weight INT,
                                            set2_reps INT,
                                            set3_weight INT,
                                            set3_reps INT,
                                            set4_weight INT,
                                            set4_reps INT,
                                            set5_weight INT,
                                            set5_reps INT,
                                            notes TEXT)''')
print("Table created successfully")
conn.close()
