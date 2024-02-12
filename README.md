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
1. Have installed tqdm (at the venv or globally)  
2. Have a text file with a column of domain names at each row, like the dummy text "icann_tld_dev_global_list.txt"
3. Open control_vars.py and set the tld variable. "tld" stands for top level domain. In this case I am using ".dev" as tld.
4. At control_vars.py set the char_length variable. This is the length of the domain name you want to query.
5. At control_vars.py set the input_file path to the file you want to query.
6. python3 01_seed_only_domain_column_from_inputfile.py
7. python3 02_create_table_from_db_by_char_length.py
8. python3 03_create_table_all_combinations_at_char_length.py
<br>
Long script names can be fast typed in terminal with: python3 01 --> tab: will autocomplete nearest match  
<br>
9. Utility scripts: u01, u02, u03, u04. Will print to terminal.  
10. Janitor scripts do sqlite cleanup.  
<br>
control_vars.py: store variable inputs that can change.  
Set char_length there before running any script. 
Warning: Each char_length integer increment will demand higher system resources.

## Requires
pip install tqdm  
(I've set up progress bars).  

### First: Get a file, somewhere
This repository uses a dummy.txt file because you can use your own output url files from nmap scans _of your local network_, or get a tld file by requesting access from the ICANN website (create an account, free) which is more polite.  

I use an ICANN CDZ file, but you can use any txt file as input data source of domain names that contain 1 column with the string shape: domainname.tld  
As txt files are super slow to query, I made some python scripts to convert it to sqlite file db (later will be a remote postgres db).  

### Second: Run the scripts from 01 to 03
* 01
* 02
* 03

### Third: Query the db, output data