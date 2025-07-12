from multiprocessing import Pool
import pandas as pd
def df_parallelize_run(func, t_split):
    '''
    实现多线程并行计算
    '''
    num_cores = np.min([N_CORES,len(t_split)])
    pool = Pool(num_cores)
    df = pd.concat(pool.map(func, t_split), axis=1)
    pool.close()
    pool.join()
    return df
