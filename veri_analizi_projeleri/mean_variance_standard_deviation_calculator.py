import numpy as np

def calculate(list):
    

    rs_list = np.array(list).reshape((3,3))

    calculations = {}

    calculations['mean'] = [rs_list.mean(axis=0).tolist(), rs_list.mean(axis=1).tolist(), np.mean(rs_list).tolist()]
    calculations['variance'] = [rs_list.var(axis=0).tolist(), rs_list.var(axis=1).tolist(), np.var(rs_list).tolist()]
    calculations['standard deviation'] = [rs_list.std(axis=0).tolist(), rs_list.std(axis=1).tolist(), np.std(rs_list).tolist()]
    calculations['max'] = [rs_list.max(axis=0).tolist(), rs_list.max(axis=1).tolist(), np.max(rs_list).tolist()]
    calculations['min'] = [rs_list.min(axis=0).tolist(), rs_list.min(axis=1).tolist(), np.min(rs_list).tolist()]
    calculations['sum'] = [rs_list.sum(axis=0).tolist(), rs_list.sum(axis=1).tolist(), np.sum(rs_list).tolist()]

    if len(list) != 9:
      raise ValueError("List must contain nine numbers.")


    return calculations