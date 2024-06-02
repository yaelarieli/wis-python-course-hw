#HW7

These codes download data from NCBI. To run it, you need to give the following line:
python hw7.py  TERM NUMBER
where TERM is the item you are looking for and NUMBER is to upload up to a number of items.
For example:
python hw7.py Lion 3

############################## 

The main code is hw7.py
The functions for the program are in func_for_hw7.py

search_ncbi(termx,numberx) - given TERM, NUMBER search in the NCBI web for the database.
fetch_ncbi(doc_id,filename) - Save each item in its own file
new_items_csv(filename,termx,numberx,total) - save in a csv file: the date, the search term, the number asked for and the total number of items found.
