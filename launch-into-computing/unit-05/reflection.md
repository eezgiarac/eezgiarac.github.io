# Reflection: SQL and NoSQL Storage Models

The electric vehicle dataset has a structured format containing country, country code, year and EV sales share. I consider SQL the more suitable primary storage model for this dataset. A relational database could define consistent data types and use a combined country-and-year key to prevent duplicate records. SQL queries would also make it straightforward to calculate averages, compare countries and examine changes across reporting years.

SQL has limitations. Its schema must normally be defined before data is stored, so structural changes may require database modifications. However, this restriction is useful for the current dataset because each record follows the same format and requires consistent validation.

NoSQL offers greater flexibility because records do not always need identical fields. This would be useful if an enterprise later combined the sales dataset with less structured information, such as charging-station logs, JSON messages, fault events or data from different vehicle manufacturers. NoSQL systems can also distribute large volumes of rapidly generated data across several servers. Their flexible structure, however, may make consistency checks and complex relationships more difficult.

For this use case, I would store the cleaned sales data in SQL because it is structured and intended for repeated comparison. NoSQL could provide additional storage for changing operational data. A combined approach would support reliable reporting while allowing the enterprise to process more varied EV and charging information.