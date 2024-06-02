from func_for_hw7 import search_ncbi,fetch_ncbi,new_items_csv
import sys



def main():
    if len(sys.argv) != 3:
        exit(f"Usage: {sys.argv[0]} FILENAME")
    termx = sys.argv[1]
    numberx = sys.argv[2]
    csvfilename = 'search_results.csv'

    Idlist,total = search_ncbi(termx,numberx) # search for the ncbi items , given term and number.
    for id in Idlist:
        filename1= f"{termx}_{id}"
        print(filename1)
        fetch_ncbi(id,filename1)
    
    new_items_csv(csvfilename,termx,numberx,total)


main()