# Domain Naming: Choosing domain name by availability
## Motivation
Why. My motivation for this was three-fold: 
* I needed focused practice with python and SQL,
* I am creating domain names for local my projects,
* I am trying to solve a mystery of rogue inbound hosts.

## What is "naming"?
Naming is a process used in marketing, sales, and business to create names for brands.  
When you are building a web project eventually you will have to create a domain name for it. Some people even build a business around it.  
Brand names are quite difficult to reach the 'correct' name, but worst part is that all dictionary words are already registered as domain names.  
So, you will have better luck with neologisms or phrases.  
With brands, besides the domain name you will have to deal with the trademark registration. Trademark availability is another subject.  

## What is "domain naming"?
Domain naming is an approach to find a name to choose for the domain name of your website, or brand if applied, using the process of the naming discipline.  
With domain names you can register the same name at different tld, but are caveats to that (from spam to phishing, to not nefarious uses, to trademark infringements).  
At the old days of the ".com" ."net" large brands could afford to register all domain names for all tlds, but these days is just not feasible, which prompted the creation of 'vanity' tlds.  

## Usage
With some few python scripts, you can know how many domain names are available to the tld of your choice.  
<br>
1. Clone this repo. Directory structure: /proc_to_db/ and /inputfiles/, and files.
2. Have python3 and tqdm (at the venv or globally)  
3. At directory /inputfiles/ have a text file with domain names rows (shaped like dummy.txt)
4. At directory /proc_to_db/ open in code editor control_vars.py and set the tld variable.
5. At control_vars.py set the char_length variable. This is the length of the domain name you want to query.
6. At control_vars.py set the input_file path to the file at /inputfiles/ you want to process.
7. Move to /proc_to_db/ as scripts use that path location (cd proc_to_db)
8. python3 01_seed_only_domain_column_from_inputfile.py
9. python3 02_what_tables_exist_in_db_and_rows.py (will print to terminal).
10. python3 03_create_table_all_combinations_at_char_length.py
11. Utility scripts: u01, u02, u03.
12. Janitor scripts: sqlite cleanup.
<br>
Long script names can be fast typed in terminal with:  

python3 01 --> tab: will autocomplete nearest match.  
python3 u01 --> tab: will autocomplete nearest match.
<br>
control_vars.py stores variable inputs that can change. Later will be a control panel.
Set char_length there before running any script. 
Warning: Each char_length integer increment will demand higher system resources.

## Requires
pip install tqdm  
(I've set up progress bars).  
python3

## Example output from script u03 for db domain name table with different char lengths for a tld
```
length: 30, are registered: 152
length: 31, are registered: 191
length: 32, are registered: 412333
length: 33, are registered: 982
length: 34, are registered: 11
```
