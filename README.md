# Domain Naming

## Usage
With some few python scripts, you can know how many domain names are available to the tld of your choice.  
<br>
1. Clone this repo.
2. Have python3, and at the venv or globally: tqdm, requests, beautifulsoup4
<br>
Note: requests and beautifulsoup4 are used to fetch and parse at the /inputfiles/scripts directory. 
<br>
3. Input file: Have a DNS register kind of file at directory /inputfiles/ (shaped like dummy.txt). Best place to get those files is the ICANN website, CDZ, but cannot be used as is.

```
input file shape:
aaaa.dev.	10800	in	ns	ns.placeholder.tld
```
<br>
4. Set the tld value at /proc_to_db/control_vars.py

```
tld = ".dev"
```
<br>
5. At the project root, activate venv:

```
$ source venvname/bin/activate
```
<br>
6. Move to /proc_to_db/ as scripts use that path location

```
$ cd proc_to_db
```
<br>
7. Create a sqlite db from the input file:

```
$ python3 01_create_sqlite_db_with_domain_column_from_inputfiles.py
```
<br>
8. Check what was created: 

```
$ python3 u01_what_tables_exist_within_created_db.py
```
<br>
9. Generate all possible combinations of domain names for name length <integer> within range (defined at the script file):

```
$ python3 02_generate_all_possible_combinations.py <integer>
as
$ python3 02_generate_all_possible_combinations.py 3
```
<br>
10. Check what was created: 

```
$ python3 u01_what_tables_exist_within_created_db.py
```

When you are done seeding the sqlite db file, deactivate the venv, go back to the project root where you have the prisma/prisma.scheme file, and run:

```
$ npx prisma db push
```

<br>
Long script names can be fast typed in terminal with:  

python3 01 --> tab: will autocomplete nearest match.  
python3 u01 --> tab: will autocomplete nearest match.  
<br>

### Example outputs for utility scripts (that print to terminal):

$ python3 u01_what_tables_exist_within_created_db.py
```
Table: registered_domain_names_table: Columns: ['id', 'domain_name'], Rows: 822523
Table: all_combs_length_3: Columns: ['id_comb', 'combination'], Rows: 47952
Table: all_combs_length_2: Columns: ['id_comb', 'combination'], Rows: 1296
Table: all_combs_length_4: Columns: ['id_comb', 'combination'], Rows: 1772928
```

$ python3 u02_count_row_groups_from_registered_domain_names_table.py

```
domain name length: 30, are registered: 15
domain name length: 31, are registered: 11
domain name length: 32, are registered: 411303
domain name length: 33, are registered: 5
domain name length: 34, are registered: 1
```

$ python3 u03_verify_shape_of_a_table.py

```
(1, 'dev')
(2, '0--0.dev')
(3, '0-0-0-0.dev')
(4, '0-0.dev')
(5, '0-1.dev')
(6, '0-2.dev')
(7, '0-3.dev')
(8, '0-9.dev')
(9, '0-day.dev')
(10, '0-matter.dev')
```

$ python3 u04_does_this_exist_in_table.py
(value_to_find = "aaaa")

```
Value found in table: all_combs_length_4 [column: combination]
```

## Motivation
Why. My motivation for this was three-fold: 
* I needed focused practice with python, SQL and SQLite,
* I am creating domain names for my projects,
* I am trying to solve a mystery of rogue inbound hosts (DNSSEC).

## What is "naming"?
Naming is a process used in marketing, sales, and business to create names for brands.  
When you are building a web project eventually you will have to create a domain name for it. Some people even build a business around it.  
Brand names are quite difficult to reach the 'correct' name, but worst part is that all dictionary words are already registered as domain names.  
So, you will have better luck with neologisms or phrases.  
With brands, besides the domain name you will have to deal with the trademark registration. Trademark availability is another subject.  

## What is "domain naming"?
Domain naming is an approach to find a name to choose for the domain name of your website, or brand if applied, using the process of the naming discipline.  
With domain names you can register the same name at different tld, but are caveats to that (from spam to phishing, to not nefarious uses, to trademark infringements).  
At the old days of the ".com" ."net" large brands could afford to register all domain names for all tlds, but these days is just not feasible, which prompted the creation of brand tlds. 