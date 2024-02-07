from typing import List
Tensor=List
def shape(tensor:Tensor)->List[int]:
    sizes:list[int]=[]
    while isinstance(tensor,list):
        sizes.append(len(tensor))
        tensor=tensor[0]
    return sizes

x= shape([1,2,3])
print("Tensor shape: ",x)
x= shape([[1,2],[3,4],[5,6],[7,8]])
print("Tensor shape: ",x)

def is_1d(tensor:Tensor)->bool:
    return not isinstance(tensor[0],list)

def tensor_sum(tensor:Tensor)->float:
    if is_1d(tensor):
        return sum(tensor)
    else:
        return sum(tensor_sum(ten_i)for ten_i in tensor)
    
print("Tensor sum: ",tensor_sum([1,2,3]))
print("Tensor sum: ",tensor_sum([[1,2],[3,4]]))

from typing import Callable
def tensor_apply(f:Callable[[float],float],tensor:Tensor)->Tensor:
    if is_1d(tensor):
        return[f(x)for x in tensor]
    else:
        return[tensor_apply(f,tens_i)for tens_i in tensor]
    
print("Tensor apply: ",tensor_apply(lambda x:x+1,[1,2,3]))
print("Tensor apply: ",tensor_apply(lambda x:2*x,[[1,2],[3,4]]))

def mean_absolute_error(pred_val,act_val):
    abs_diff=[abs(pred-act)for pred,act in zip(pred_val,act_val)]
    return sum(abs_diff)/len(abs_diff)

