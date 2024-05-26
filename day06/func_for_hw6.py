import statistics

def get_iter_rows(ws,row):
    result=[]
    for cell in row:
        result.append(cell.value)
    return result

def mean_of_row(ws,row,wb):
        #try
        row_vec = get_iter_rows(ws,row) # get a vector of the values of each row
        mean_w = statistics.mean(row_vec[1:19])
        row_num = row_vec[0]+1
        ws[f'T{row_num}']=mean_w
        # except Exception as err:
        #     print(f"There was an error: {err}")
        wb.save("wprcl2.xlsx")



def mean_of_row_for_test(ws,row):
        row_vec = get_iter_rows(ws,row) # get a vector of the values of each row
        mean_w = statistics.mean(row_vec[1:19])
        row_num = row_vec[0]+1
        ws[f'T{row_num}']=mean_w
        return(mean_w)
